from scan_codes import ScanCodes
from collections import defaultdict
import pandas as pd

def update_features_dict(apk_name, d_features, d_new_features):
    # update features from a dictionary of api or permission
    # print(d_new_features)
    for feature, _ in d_new_features.items():
        d_features[feature].append(apk_name)

    return d_features

def update_features_list(apk_name, d_features, l_new_features):
    # update features from a list of api or permission
    # print(l_new_features)
    for feature in l_new_features:
        d_features[feature].append(apk_name)

    return d_features

def analysis_api(apk_name, d_api, d_methods):
    # update api
    # print(d_methods)
    for api, _ in d_methods.items():
        d_api[api].append(apk_name)

    return d_api

def analysis_permissions(apk_name, d_permission, l_permission):
    # update permission
    # print(l_permission)
    for p in l_permission:
        d_permission[p].append(apk_name)

    return d_permission

def convert_dict(l_apk_name, d_feature):
    # convert {feature: [apk_name]} => {feature: [0, 1, ...]}
    d_int_feature = defaultdict(list)
    for feature, apk_names in d_feature.items():
        for apk_name in l_apk_name:
            d_int_feature[feature].append(int(apk_name in apk_names))
    return d_int_feature

def output_csv(d_apk_name, d_int_api, d_int_permission):
    # concate api and permission, and output as a csv file
    # Todo: add class(Benign 0; Malicious: 1) for each apk
    d_apk_name.update(d_int_api)
    d_apk_name.update(d_int_permission)
    df_results = pd.DataFrame(data=d_apk_name)
    output_path = "../db/feature_api_permission.csv"
    df_results.to_csv(output_path, index=False)
    # print(d_apk_name)
    print_title("Output CSV file")
    print(f"Output Path: {output_path}")
    print(f"Total number of features: {len(df_results.columns)}" )
    print(f"Total number of samples: {len(df_results)}" )


def print_title(title=""):
    # print break line with title
    # ============== title =============
    total_len = 100
    if title:
        decoration = "=" * ((total_len - len(title) - 1) // 2)
        print(decoration + " " + title + " " + decoration)
    else:
        print("=" * 101)

def run(l_apk_name, dir_src):
    d_apk_name = {"apk_name": l_apk_name}
    # store api as dictionary {key: value} {api: list of apks}
    d_api = defaultdict(list)
    # store permission as dictionary {key: value} {permission: list of apks}
    d_permission = defaultdict(list)
    # Update dictionary of api and permission
    total_apks = len(l_apk_name)
    for i, apk_name in enumerate(l_apk_name):
        print_title()
        print_title(f"{i+1}/{total_apks} APK - {apk_name}")
        print_title()
        apk_src = dir_src + apk_name
        scan_codes = ScanCodes(apk_src)
        l_permission = scan_codes.get_permission_l()    # get permission as a list
        d_methods = scan_codes.get_all_methods_d()    # get methods as a dictionary
        d_api = update_features_dict(apk_name, d_api, d_methods)
        d_permission = update_features_list(apk_name, d_permission, l_permission)
        print("\n")
    # convert dict
    d_int_api = convert_dict(l_apk_name, d_api)
    d_int_permission = convert_dict(l_apk_name, d_permission)
    print(d_int_api)
    print(d_int_permission)
    # Output as a csv file
    # output_csv(d_apk_name, d_int_api, d_int_permission)

def main():
    print_title("Start Scanning...")
    l_apk_name = ["0a37f086841ff927ec8bee9f3bdb1048ecfba54b09aea400e980bd3ef301519d.77f09f214993016fbc747b5bafa5f94f", "0ac4aa9b5413666a2bd66b96faa0cc8e656144ffcd351101071f8d028970befa.2fd32776a17d88eaa6fb2bcd792695f0"]
    dir_src = "../../apps/apks_codes/"
    run(l_apk_name, dir_src)

if __name__ == '__main__':
    main()
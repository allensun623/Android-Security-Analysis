from .cdv_scan_codes import ScanCodes
from .cdv_scan_permission import ScanPermission
from collections import defaultdict
from os import scandir

# from .cdv_plugins import get_object
from .cdv_plugins import get_object_d
# from .cdv_plugins import get_event_object
from .cdv_plugins import get_event_object_d
from .output_csv import output_csv


def convert_event_obj(d_api):
    # sum up events and object belonging to an object
    # d_new_api {k, v} => {object:0, object2:0}
    d_new_api = get_object_d()
    # d_event_object {k, v} => {event1object1, event2: object1, object1:object1, ...}
    d_event_object = get_event_object_d()
    for k, v in d_api.items():
        d_new_api[d_event_object[k]] += v

    return d_new_api


def update_api(apk_name, d_features, d_new_features):
    # update features from a dictionary of api or permission
    # print(d_new_features)
    for feature in d_new_features.keys():
        d_features[feature].append(d_new_features[feature])

    return d_features


def update_permission(apk_name, d_features, l_new_features):
    # update features from a list of api or permission
    # print(l_new_features)
    for feature in l_new_features:
        d_features[feature].append(apk_name)

    return d_features


def convert_dict_bool(l_apk_name, d_feature):
    # convert {feature: [apk_names]} => {feature: binary}: {feature: [0, 1, 1, 0, ...]}
    d_int_feature = defaultdict(list)
    for feature, apk_names in d_feature.items():
        for apk_name in l_apk_name:
            d_int_feature[feature].append(int(apk_name in apk_names))
    return d_int_feature


def convert_dict_digit(l_apk_name, d_feature):
    # convert {feature: [apk_names]} => {feature: category}: {feature: [3, 1, 6, 4, ...]}
    d_int_feature = defaultdict(list)
    for feature, apk_names in d_feature.items():
        for apk_name in l_apk_name:
            d_int_feature[feature].append(int(apk_name in apk_names))
    return d_int_feature


def run_scan(dir_src, dir_output, main_folders, main_extentions, main_targets):
    """
    input: a list apk names and source directory
    output: csv files
    """
    l_apk_name = scan_folder(dir_src)
    d_apk_name = {"apk_name": l_apk_name}
    # store api as dictionary {key: value} => {api: list of apks}
    d_api_all = defaultdict(list)
    # store permission as dictionary {key: value} => {permission: list of apks}
    d_permission_all = defaultdict(list)
    # scan all apks and update dictionary of api and permission
    total_apks = len(l_apk_name)
    for i, apk_name in enumerate(l_apk_name):
        print_title()
        print_title(f"{i+1}/{total_apks} APK - {apk_name}")
        print_title()
        apk_src = dir_src + apk_name
        cvd_scan_codes = ScanCodes(apk_src, main_folders, main_extentions, main_targets)
        cdv_scan_permission = ScanPermission(apk_src)
        d_api = cvd_scan_codes.get_all_targets_d()
        d_api = convert_event_obj(d_api)  # sum up events and obj
        l_permission = cdv_scan_permission.get_permission_l()
        d_api_all = update_api(apk_name, d_api_all, d_api)  # concate all dict for api
        d_permission_all = update_permission(
            apk_name, d_permission_all, l_permission
        )  # concate all dict for permission
        print("\n")
    # print(d_api_all)
    # print(d_permission_all)
    d_int_permission_all = convert_dict_bool(l_apk_name, d_permission_all)
    # print(d_int_permission_all)
    # Output as csv files
    output_csv(d_apk_name, d_api_all, d_int_permission_all, dir_output)


def scan_folder(dir_path):
    # scan all subdirectories under a directory:
    # return names of subdirectories
    apk_dirs = [f.name for f in scandir(dir_path) if f.is_dir()]
    # get all paths of subdirectories
    # apk_dirs = [f.path for f in scandir(dir_path) if f.is_dir()]
    print(f"Source apks: {len(apk_dirs)}")
    return apk_dirs


def print_title(title=""):
    # print break line with title
    # ============== title =============
    total_len = 100
    if title:
        decoration = "#" * ((total_len - len(title) - 1) // 2)
        print(decoration + " " + title + " " + decoration)
    else:
        print("#" * 101)


# def main():
#     print_title("Start Scanning...")
#     # directory for apk source codes
#     dir_src = "../../apps/apks_codes/chirag/"
#     # directory for output csv
#     dir_output = "../db/cdv/"
#     # main source folder
#     main_folders = ["apktools/assets/www/"]
#     # main files for scanning
#     main_extentions = [".js", ".html", ".mustache"]
#     # main targets for scanning
#     main_targets = get_event_object()
#     # Hybrid apks
#     # l_apk_name = ["Instagram_v173.0.0.39.120_apkpure.com", "iBooks"]
#     run_scan(dir_src, dir_output, main_folders, main_extentions, main_targets)


# if __name__ == "__main__":
#     main()
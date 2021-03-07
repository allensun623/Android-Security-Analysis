from .cordova_scan_codes import CordovaScanCodes
from collections import defaultdict
import pandas as pd
import copy
from os import scandir
from pathlib import Path
from .output_csv import output_csv


def update_functions(apk_name, d_features, d_new_features):
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

def print_title(title=""):
    # print break line with title
    # ============== title =============
    total_len = 100
    if title:
        decoration = "#" * ((total_len - len(title) - 1) // 2)
        print(decoration + " " + title + " " + decoration)
    else:
        print("#" * 101)

def run_scan(l_apk_name, dir_src, dir_output):
    """
        input: a list apk names and source directory
        output: csv files
    """
    d_apk_name = {"apk_name": l_apk_name}
    # store api as dictionary {key: value} => {api: list of apks}
    d_api = defaultdict(list)
    # store permission as dictionary {key: value} => {permission: list of apks}
    d_permission = defaultdict(list)
    # scan all apks and update dictionary of api and permission
    total_apks = len(l_apk_name)
    for i, apk_name in enumerate(l_apk_name):
        print_title()
        print_title(f"{i+1}/{total_apks} APK - {apk_name}")
        print_title()
        apk_src = dir_src + apk_name
        cordova_scan_codes = CordovaScanCodes(apk_src)
        l_permission = cordova_scan_codes.get_permission_l()    # get permission as a list
        d_methods = cordova_scan_codes.get_all_methods_d()    # get methods as a dictionary
        d_api = update_functions(apk_name, d_api, d_methods)    # concate all dict for api
        d_permission = update_permission(apk_name, d_permission, l_permission)    # concate all dict for permission
        print("\n")
    # convert dict
    # d_int_api = convert_dict_bool(l_apk_name, d_api)
    d_int_permission = convert_dict_bool(l_apk_name, d_permission)
    # print(d_int_api)
    # print(d_int_permission)

    # Output as csv files
    output_csv(d_apk_name, d_api, d_int_permission, dir_output)

def scan_folder(dir_path):
    # scan all subdirectories under a directory:
    # return names of subdirectories
    apk_dirs = [f.name for f in scandir(dir_path) if f.is_dir()]
    # get all paths of subdirectories
    # apk_dirs = [f.path for f in scandir(dir_path) if f.is_dir()]
    print(f'Source apks: {len(apk_dirs)}')
    return apk_dirs

def main():
    print_title("Start Scanning...")
    # directory for apk source codes
    dir_src = "../../apps/apks_codes/chirag/"
    # directory for output csv
    dir_output = "../db/cdv/"
    # Hybrid apks
    # l_apk_name = ["Instagram_v173.0.0.39.120_apkpure.com", "iBooks"]
    l_apk_name = scan_folder(dir_src)
    run_scan(l_apk_name, dir_src, dir_output)

if __name__ == '__main__':
    main()
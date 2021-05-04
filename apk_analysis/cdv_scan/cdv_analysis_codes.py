from .cdv_scan_codes import ScanCodes
from .cdv_scan_permission import ScanPermission
from .cdv_scan_plugin_declaration import ScanPluginDeclaration
from .cdv_scan_apk import ScanAPK
from collections import defaultdict
from os import scandir
import json
# from .cdv_plugins import get_object
from .cdv_plugins import get_object_d

# from .cdv_plugins import get_event_object
from .cdv_plugins import get_event_object_d
from .cdv_plugins import get_plugin_object_d
from .cdv_plugins import get_plugin
from .cdv_plugins import get_plugin_d
from .cdv_plugins import get_plugin_permission_d
from .cdv_plugins import get_name_plugin_d
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


def plugin_permission_map(l_permission, l_plugin):
    # output {plugin1: 0/1, plugin2: 0/1 } AndroidManifest declares required permission for corresponsing plug
    print_title()
    d_plugin_permission = get_plugin_permission_d()
    d_plugin = {plugin: 0 for plugin in l_plugin}
    for plugin in l_plugin:
        # if all required permission declared in the obtained list
        if all(perm in l_permission for perm in d_plugin_permission[plugin]):
            d_plugin[plugin] = 1
    return d_plugin


def run_scan(dir_src, dir_output, main_folders, main_extentions, main_targets):
    """
    input: a list apk names and source directory
    output: csv files
        apk_name feature1 feature2 feature3...
        apk1     1         1         0
        apk2     1         0         1
        ...
    """
    # l_apk_name = scan_folder(dir_src)[:10] # change the value for testing
    l_apk_name = sorted(scan_folder(dir_src))
    l_main_folder_exist = []  # APKs don't contain target folder
    l_cdv_apk = []  # contains the list of cordova apks
    l_cdv_apk_xml = (
        []
    )  # the list of cordava apks contain neither config.xml not plugins.xml
    d_cdv_apk_undeclared_plugin = {}  # the dict of cordava apks with undeclared plugins
    # init dict
    d_api_all = defaultdict(
        list
    )  # store api as dictionary {key: value} => {api: list of apks}
    d_plugin_declare_all = defaultdict(
        list
    )  # store declared api as dictionary {key: value} => {api: list of apks}
    d_plugin_permission_declare_all = defaultdict(
        list
    )  # store declared api as dictionary {key: value} => {api: list of apks}
    d_permission_all = defaultdict(
        list
    )  # store permission as dictionary {key: value} => {permission: list of apks}
    d_xml = {"config.xml": [], "plugins.xml": []}
    # scan all apks and update dictionary of api and permission
    total_apks = len(l_apk_name)
    for i, apk_name in enumerate(l_apk_name):
        print_title()
        print_title(f"{i+1}/{total_apks} APK - {apk_name}")
        scan_apk = ScanAPK(
            apk_name, dir_src, main_folders, main_extentions, main_targets
        )
        d_apk_data = scan_apk.d_apk_data
        if not d_apk_data["main_folders_exist"]:  # print apks without target folder
            l_main_folder_exist.append(apk_name)
        else:
            # d_api_files = d_apk_data["d_api_files"]
            # store undeclared_plugin with api call detected file and its apk name
            undeclared_plugin = scan_apk.undeclared_plugin()
            if undeclared_plugin:
                d_cdv_apk_undeclared_plugin[apk_name] = {
                    # "plugin_usage": {plugin: d_apk_data["d_api"][plugin] for plugin in undeclared_plugin},
                    # "plugin_declaration": {plugin: d_apk_data["d_plugin_declare"][plugin] for plugin in undeclared_plugin},
                    "config.xml": d_apk_data["config_xml"],
                    "plugins.xml": d_apk_data["plugins_xml"],
                    "d_api_files": {plugin: d_apk_data["d_api_files"][plugin] for plugin in undeclared_plugin},
                } 


            l_cdv_apk.append(apk_name)
            d_api_all = update_api(
                apk_name, d_api_all, d_apk_data["d_api"]
            )  # concate all dict for api
            d_permission_all = update_permission(
                apk_name, d_permission_all, d_apk_data["l_permission"]
            )  # concate all dict for permission
            d_plugin_declare_all = update_api(
                apk_name, d_plugin_declare_all, d_apk_data["d_plugin_declare"]
            )  # concate all dict for api
            d_plugin_permission_declare_all = update_api(
                apk_name,
                d_plugin_permission_declare_all,
                d_apk_data["d_plugin_permission_declare"],
            )  # concate all dict for api
            d_xml["config.xml"].append(d_apk_data["config_xml"])
            d_xml["plugins.xml"].append(d_apk_data["plugins_xml"])
            # the list of cordava apks contain neither config.xml not plugins.xml
            if not d_apk_data["config_xml"] and not d_apk_data["plugins_xml"]:
                l_cdv_apk_xml.append(apk_name)
            print("\n")

    d_plugin_declare_xml_all = {**d_plugin_declare_all, **d_xml}
    d_int_permission_all = convert_dict_bool(l_cdv_apk, d_permission_all)
    d_apk_name = {"apk_name": l_cdv_apk}
    # Output as csv files
    # output_csv(
    #     d_apk_name,
    #     d_api_all,
    #     d_int_permission_all,
    #     d_plugin_declare_xml_all,
    #     d_plugin_permission_declare_all,
    #     dir_output,
    # )

    # print(
    #     f"{len(l_main_folder_exist)} APKs are not Cordava APPs: \n{sorted(l_main_folder_exist)}\n"
    # )
    # print(
    #     f"{len(l_cdv_apk_xml)} Cordava APKs have neither config.xml nor plugins.xml: \n{sorted(l_cdv_apk_xml)}\n"
    # )
    output_json_undeclared_plugin(d_cdv_apk_undeclared_plugin, l_cdv_apk)

def output_json_undeclared_plugin(d_cdv_apk_undeclared_plugin, l_cdv_apk):
    data = d_cdv_apk_undeclared_plugin
    # file_path = "../db/cdv/apk_undeclared_plugin.json"
    file_path = "../db/cdv/apk_plugin_usage.json"
    print(f"output path for apks with undeclared plugin: {file_path}")
    print(f"{len(file_path)}/{len(l_cdv_apk)} apks with undeclared plugin")
    with open(file_path, "w", encoding ='utf8') as json_file:
        json.dump(data, json_file)


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
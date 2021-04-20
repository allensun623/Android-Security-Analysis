"""
    Scan single APK
"""

from .print_title import print_title
from .cdv_scan_codes import ScanCodes
from .cdv_scan_permission import ScanPermission
from .cdv_scan_plugin_declaration import ScanPluginDeclaration

from .cdv_plugins import get_plugin_object_d
from .cdv_plugins import get_plugin
from .cdv_plugins import get_name_plugin_d
from .cdv_plugins import get_plugin_permission_d


class ScanAPK:
    def __init__(self, apk_name, dir_src, main_folders, main_extentions, main_targets):
        self.apk_name = apk_name
        self.dir_src = dir_src
        self.main_folders = main_folders
        self.main_extentions = main_extentions
        self.main_targets = main_targets
        self.d_apk_data = self.scan_single_apk(
            self.apk_name,
            self.dir_src,
            self.main_folders,
            self.main_extentions,
            self.main_targets,
        )

    def scan_single_apk(
        self, apk_name, dir_src, main_folders, main_extentions, main_targets
    ):
        # return a dict of api, list of permission, a dict of plugin declaration
        print_title()
        l_plugin = get_plugin()
        d_name_plugin = get_name_plugin_d()
        d_plugin_object = get_plugin_object_d()
        apk_src = dir_src + apk_name
        d_res = {
            "main_folders_exist": False,  # if the targe folder not exists:
            "d_api": False,
            "d_api_files": False,
            "l_permission": False,
            "d_plugin_declare": False,
            "d_plugin_permission_declare": False,
            "config_xml": False,
            "plugins_xml": False,
        }
        cvd_scan_codes = ScanCodes(apk_src, main_folders, main_extentions, main_targets)
        if cvd_scan_codes.main_folders_exist:
            cdv_scan_permission = ScanPermission(apk_src)
            cdv_scan_plugin_declaration = ScanPluginDeclaration(
                apk_src, l_plugin, d_name_plugin
            )
            d_api, d_api_files = cvd_scan_codes.get_all_targets_d()
            # d_api = convert_event_obj(d_api)  # sum up events and obj
            # map object to plugin
            d_api = {d_plugin_object[k]: v for k, v in d_api.items()}
            d_api_files = {d_plugin_object[k]: v for k, v in d_api_files.items()}
            l_permission = cdv_scan_permission.get_permission_l()
            d_plugin_declare = cdv_scan_plugin_declaration.get_all_plugins_d()
            d_plugin_permission_declare = self.__plugin_permission_map(
                l_permission, l_plugin
            )
            d_res = {
                "main_folders_exist": cvd_scan_codes.main_folders_exist,  # if the targe folder not exists:
                "d_api": d_api,
                "d_api_files": d_api_files,
                "l_permission": l_permission,
                "d_plugin_declare": d_plugin_declare,
                "d_plugin_permission_declare": d_plugin_permission_declare,
                "config_xml": cdv_scan_plugin_declaration.config_xml,
                "plugins_xml": cdv_scan_plugin_declaration.plugins_xml,
            }

        return d_res

    def undeclared_plugin(self):
        # d_api: plugin: (0, 1, 2, ...)
        # d_plugin_declare: plugin: (0, 1)
        # store the plugin used (value>1) but not declared(value=0)
        d_p_use = self.d_apk_data["d_api"]
        d_p_dec = self.d_apk_data["d_plugin_declare"]
        l_res = [p for p, v in d_p_use.items() if int(v) > 0 and int(d_p_dec[p]) == 0]
        return l_res

    def __plugin_permission_map(self, l_permission, l_plugin):
        # output {plugin1: 0/1, plugin2: 0/1 } AndroidManifest declares required permission for corresponsing plug
        print_title()
        d_plugin_permission = get_plugin_permission_d()
        d_plugin = {plugin: 0 for plugin in l_plugin}
        for plugin in l_plugin:
            # if all required permission declared in the obtained list
            if all(perm in l_permission for perm in d_plugin_permission[plugin]):
                d_plugin[plugin] = 1
        return d_plugin

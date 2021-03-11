"""
Scan declarad plugins
"""
from os import walk
from os import path
import re
from collections import defaultdict
class ScanPluginDeclaration():
    """
        Scan .xml files (especially for config.xml and plugin.xml)
        under the apk decompiled source code folder `/apktools/res/xml/`.
        Extract all permission and store as a list.
        dict: {plugin1: int, plugin2: int, ...}
        ...
    """
    def __init__(self, apk_src, l_plugin, d_name_plugin):
        self.apk_src = apk_src
        self.main_folder = "apktools/res/xml"
        self.main_extentions = ".xml"
        self.l_plugin = l_plugin  # a list {plugin1, plugin2, ...} 
        self.d_name_plugin = d_name_plugin # a dictionary {name1:plugin1, name2:plugin2} 
        self.target_files = self.__scan_subfolder()
        # self.d_methods = self.__get_all_methods()

    def __scan_subfolder(self):
        # scan all target files (.xml)
        target_files = []
        dir_path = self.apk_src + "/" + self.main_folder
        for dirpath, _, filenames in walk(dir_path):
            for filename in [f for f in filenames if f.endswith(tuple(self.main_extentions))]:
                target_files.append(path.join(dirpath, filename))

        # print(target_files)
        if len(target_files):
            print(f"Total \"{self.main_extentions}\" files scanned: {len(target_files)}")
        else:
            print(f"Wrong source path or there is no {self.main_extentions} file in the path: \"{self.apk_src}\n")
        return target_files

    def get_all_plugins_d(self):
        # extract all plugin declared from a list of files, and store as a dict
        self.print_title("Start Extracting Targets")
        d_plugins = {plugin:0 for plugin in self.l_plugin}
        # find all targets match " target1|target2|..."
        for target_path in self.target_files:
            d_plugins = self.__get_plugin_single_file(target_path, d_plugins)
        print(f"Total unique plugin declared: {len(d_plugins)}")

        return d_plugins

    def __get_plugin_single_file(self, target_path, d_plugins):
        # extract all targets from a extention file, and store as a dict
        try: 
            with open (target_path, 'r') as source_file:
                source_code = source_file.read() 
                # <feature name="plugin" ...>
                # TODO - Consider single quote
                match = re.findall(
                    "(<feature|<plugin) name=\"(.*?)\"", source_code
                )
                # match: list of [("<feature", name), ("<plugin", name), ...]
                for _, name in match:
                    if name in self.d_name_plugin:
                        d_plugins[self.d_name_plugin[name]] = 1    # function + 1
                # print(d_plugins)

        except Exception as e:
            print(e)

        return d_plugins



    def print_title(self, title):
        # print break line with title
        # ============== title =============
        total_len = 100
        decoration = "=" * ((total_len - len(title) - 1) // 2)
        print(decoration + " " + title + " " + decoration)


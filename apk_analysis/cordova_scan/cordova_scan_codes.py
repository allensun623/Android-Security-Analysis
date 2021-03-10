from os import walk
from os import path
import re
from collections import defaultdict
from tqdm import tqdm
from scan_codes.scan_codes import ScanCodes
from cordova_scan.cordova_plugins import get_func
from cordova_scan.cordova_plugins import get_plugin_func
from cordova_scan.cordova_plugins import get_func_plugin_dict


class CordovaScanCodes(ScanCodes):
    def __init__(self, apk_src):
        self.l_func = get_func()    # [plugin1_function1, plugin1_function2, ..., ]
        self.l_plugin_func = get_plugin_func()    # [plugin1_function1, plugin1_function2, ..., plugin1, ... plugin]
        self.d_func_plugin = get_func_plugin_dict()    # {func: plugin}
        # initialize the list of plugins and funcs as key-value pair of {feature: 0}
        self.d_methods = {pf: 0 for pf in self.l_plugin_func}
        super().__init__(apk_src)

    def get_all_methods_d(self):
        # extract all methods from a list of java files, and store as a dict
        self.print_title("Start Extracting Java Methods")

        # for target_path in tqdm(self.java_files):  # this is for process bar
        for target_path in self.java_files:
            self.__get_methods_single_java_file(target_path)
        
        # print(f"Total unique methods extracted: {len(self.d_methods)}")
        # print(self.d_methods)
        return self.d_methods

    def __get_methods_single_java_file(self, target_path):
        # extract all methods matching functions in corresponding cordova plugin
        # from a java file, and store as a dict
        try:
            with open(target_path, "r") as source_file:
                source_code = source_file.read()
                # cordova: find all methods match "function|public|protected|private|static ... ("
                match = re.findall(
                    "(function|public|protected|private|static) (.*?)\(", source_code
                )
                for m in match:
                    # m is a set of ('function|public|protected|private|static', 'void string')
                    method = m[1].split(" ")[-1]
                    if method and method in self.l_func:
                        self.d_methods[method] += 1    # function + 1
                        self.d_methods[self.d_func_plugin[method]] += 1    # plugin + 1
                # print(d_methods)

        except Exception as e:
            print(e)

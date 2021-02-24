from os import walk
from os import path
import re
from collections import defaultdict
from tqdm import tqdm

class ScanCodes:
    """
        Scan all .java files under the apk decompiled source code folder `src`.
        Extract all methods from obtained java files and store as a dict.
    """
    def __init__(self, apk_src):
        self.apk_src = apk_src
        # ToDo: needs to check which folder stores the main source code
        # self.main_folders =  ["src/androidx/", "src/com/"]
        self.main_folders =  ["src/"]
        self.java_files = self.__scan_subfolder()
        # self.l_permission = None
        self.android_manifest = self.__get_android_manifest()
        # self.d_methods = self.__get_all_methods()

    def __scan_subfolder(self):
        # scan all .java files
        java_files = []
        for folder in self.main_folders:
            dir_path = self.apk_src + "/" + folder
            for dirpath, _, filenames in walk(dir_path):
                for filename in [f for f in filenames if f.endswith(".java")]:
                    java_files.append(path.join(dirpath, filename))

        # print(java_files)
        if len(java_files):
            print(f"Total \".Java\" files scanned: {len(java_files)}")
        else:
            print(f"Wrong source path or there is no .java file in the path: \"{self.apk_src}\n")
        return java_files

    def __get_android_manifest(self):
        # If AndroidManifest.xml exists, return its path and extract all permission
        # Else, return false.
        file_path = self.apk_src + "/apktools/AndroidManifest.xml"
        if self.__file_dir_exist(file_path):
            print("Obtained \"AndroidMaifest.xml\".")
            # self.l_permission = self.__get_permission(file_path)
            return file_path
        else:
            print("Didn't find \"AndroidMaifest.xml\"")
            return False

    def get_permission_l(self):
        # extract all permission from AndroidMaifest.xml, and store as a list
        if self.android_manifest:
            try:
                with open (self.android_manifest, 'r') as source_file:
                    source_code = source_file.read() 
                    # e.g. <uses-permission android:name="android.permission.INTERNET"/>
                    match = re.findall("<uses-permission android:name=(.*?)\/\>", source_code)
                    # remove quotes and store as a list
                    l_permission = [m[1:-1] for m in match]
                    # print(l_permission)
                
                print(f"Total \"permission\" extracted: {len(l_permission)}")
                return l_permission

            except Exception as err:
                print(err)
                return 
        else:
            print("Didn't find \"AndroidMaifest.xml\"")


    def __file_dir_exist(self, target_path):
        exists = path.exists(target_path)
        if not exists:
            print("\"" + target_path + "\"" + " NOT EXISTS!")
        return exists

    def get_all_methods_d(self):
        # extract all methods from a list of java files, and store as a dict
        self.print_title("Start Extracting Java Methods")
        d_methods = defaultdict(int)
        for target_path in tqdm(self.java_files):
            d_methods_file = self.get_methods_single_java_file(target_path)
            # update to d_method
            if d_methods_file:
                d_methods.update(d_methods_file)
        print(f"Total unique methods extracted: {len(d_methods)}")

        return d_methods

    def get_methods_single_java_file(self, target_path):
        # extract all methods from a java file, and store as a dict
        try: 
            with open (target_path, 'r') as source_file:
                source_code = source_file.read() 
                # find all methods match " public|protected|private|static ... ("
                match = re.findall(" (public|protected|private|static) (.*?)\(", source_code)
                # print(match)
                # get all methods as a list
                # methods = [m[1].split(" ")[-1] for m in match]
                # print(methods)
                d_methods = defaultdict(int)
                for m in match:
                    # m is a set of (public|protected|private|static, string)
                    method = m[1].split(" ")[-1]
                    d_methods[method] += 1 
                # print(d_methods)
            return d_methods

        except Exception as e:
            print(e)
            return 

    def print_title(self, title):
        # print break line with title
        # ============== title =============
        total_len = 100
        decoration = "=" * ((total_len - len(title) - 1) // 2)
        print(decoration + " " + title + " " + decoration)


from os import path
import re

class ScanPermission:
    """
        Scan all AndroidManifest.xml files under the apk decompiled source code folder `/apktools/`.
        Extract all permission and store as a list.
        list:
        [permission1, permission2, ...]
        ...
    """
    def __init__(self, apk_src):
        self.apk_src = apk_src
        self.android_manifest = self.__get_android_manifest()
        # self.d_methods = self.__get_all_methods()


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


    def print_title(self, title):
        # print break line with title
        # ============== title =============
        total_len = 100
        decoration = "=" * ((total_len - len(title) - 1) // 2)
        print(decoration + " " + title + " " + decoration)


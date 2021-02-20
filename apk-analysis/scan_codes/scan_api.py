from os import walk
from os import path

class ScanAPI:
    def __init__(self, apk_src):
        self.apk_src = apk_src
        # ToDo: needs to check which folder stores the main source code
        # self.main_folders =  ["src/androidx/", "src/com/"]
        self.main_folders =  ["src/"]
        self.java_files = self.scan_subfolder()
        self.android_manifest = self.get_android_manifest()

    def scan_subfolder(self):
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

    def get_android_manifest(self):
        # If AndroidManifest.xml exists, return its path
        # Else, return false.
        file_path = self.apk_src + "/apktools/AndroidManifest.xml"
        if self.file_dir_exist(file_path):
            print("\"AndroidMaifest.xml\" scanned.")
            return file_path
        else:
            return False

    def file_dir_exist(self, target_path):
        exists = path.exists(target_path)
        if not exists:
            print("\"" + target_path + "\"" + " NOT EXISTS!")
        return exists
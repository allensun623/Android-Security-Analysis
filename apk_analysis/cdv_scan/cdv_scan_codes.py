from os import walk
from os import path
import re
from collections import defaultdict
from tqdm import tqdm

class ScanCodes:
    """
        Scan all files(e.g. .js, .html) under the apk decompiled source code folder `src`.
        Extract all targets from obtained extention files and store as a dict.
        dict: {main_target1: int, main_target2: int, ...}
    """
    def __init__(self, apk_src, main_folders, main_extentions, main_targets):
        self.apk_src = apk_src
        # ToDo: needs to check which folder stores the main source code
        # self.main_folders =  ["src/androidx/", "src/com/"]
        self.main_folders =  main_folders    # main source folder
        self.main_extentions = main_extentions    # main suffix file e.g. .js, .html
        self.main_targets = main_targets    # a list of targets e.g. battery, camera
        self.target_files = self.__scan_subfolder()

    def __scan_subfolder(self):
        # scan all target files (.js, .html, .mustache)
        target_files = []
        for folder in self.main_folders:
            dir_path = self.apk_src + "/" + folder
            for dirpath, _, filenames in walk(dir_path):
                for filename in [f for f in filenames if f.endswith(tuple(self.main_extentions))]:
                    target_files.append(path.join(dirpath, filename))

        # print(target_files)
        if len(target_files):
            print(f"Total \"{self.main_extentions}\" files scanned: {len(target_files)}")
        else:
            print(f"Wrong source path or there is no {self.main_extentions} file in the path: \"{self.apk_src}\n")
        return target_files

    def __file_dir_exist(self, target_path):
        exists = path.exists(target_path)
        if not exists:
            print("\"" + target_path + "\"" + " NOT EXISTS!")
        return exists

    def get_all_targets_d(self):
        # extract all targets from a list of files, and store as a dict
        self.print_title("Start Extracting Targets")
        d_targets = {target:0 for target in self.main_targets}
        # find all targets match " target1|target2|..."
        find_string = "|".join(self.main_targets)
        for target_path in tqdm(self.target_files):
            d_targets_single = self.__get_target_single_file(target_path, find_string)
            # update to d_targets
            if d_targets_single:
                d_targets.update(d_targets_single)
        print(f"Total unique targets extracted: {len(d_targets)}")

        return d_targets

    def __get_target_single_file(self, target_path, find_string):
        # extract all targets from a extention file, and store as a dict
        d_targets = defaultdict(int)
        try: 
            with open (target_path, 'r') as source_file:
                source_code = source_file.read() 
                # print(find_string)
                match = re.findall(f"({find_string})", source_code)
                for m in match:
                    # make sure got the match in the targets
                    if m in self.main_targets:
                        d_targets[m] += 1 
                # print(d_targets)

        except Exception as e:
            print(e)

        return d_targets



    def print_title(self, title):
        # print break line with title
        # ============== title =============
        total_len = 100
        decoration = "=" * ((total_len - len(title) - 1) // 2)
        print(decoration + " " + title + " " + decoration)


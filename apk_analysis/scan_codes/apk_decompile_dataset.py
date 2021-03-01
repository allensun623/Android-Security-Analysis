from scan_codes import ScanCodes
# Todo import from parent directory
from apk_process import decompile_apk
from os import walk
from os import path

def run_scan(apk_src):
    print_title("Start Scanning...")
    scan_api = ScanCodes(apk_src)

def file_dir_exist(target_path):
    exists = False
    try:
        exists = path.exists(target_path)
    except Exception as e:
        print(e)
    if not exists:
        print("\"" + str(target_path) + "\"" + " NOT EXISTS!")
    return exists

def check_apk(target_path):
    # check if the target file is an apk
    apk = target_path[-3:] == "apk"
    print(target_path[-3:])
    if not apk:
        print("It is not an apk, please use an apk file!")
    return apk

def print_title(title):
    # print break line with title
    # ############# title #############
    total_len = 100
    decoration = "#" * ((total_len - len(title) - 1) // 2)
    print(decoration + " " + title + " " + decoration)

def get_apks(dir_path):
    # scan all .apk files
    apk_files = []
    apk_names = []
    try: 
        for dirpath, _, filenames in walk(dir_path):
            for filename in [f for f in filenames if f.endswith(".apk")]:
                apk_files.append(path.join(dirpath, filename))
                apk_names.append(filename[:-4])
    except Exception as e:
        print(e)
    # print(apk_files)
    # print(apk_names)
    if len(apk_files):
        print(f"Total \".apk\" files scanned: {len(apk_files)}")
    else:
        print(f"Wrong source path or there is no .apk file in the path: \"{dir_path}\n")
    return apk_files, apk_names

def apk_decompile(apk_codes_path, apk_files, apk_names):
    print_title("Start Decompile")
    for i, apk_src, apk_name in enumerate(zip(apk_files, apk_names)):
        print_title(f"At {i}/{len(apk_files)} decompiling...")
        apk_dst = f"{apk_codes_path}/{apk_name}"
        decompile_apk(apk_src, apk_dst)

def main():
    # zip_src = "../../apps/apks_upzip/0a37f086841ff927ec8bee9f3bdb1048ecfba54b09aea400e980bd3ef301519d.77f09f214993016fbc747b5bafa5f94f.zip"
    dir_path = "../../apps/apks/chirag"
    apk_codes_path = "../../apps/apks_codes/chirag"
    apk_files, apk_names = get_apks(dir_path)
    # decompile a list of apks
    apk_decompile(apk_codes_path, apk_files, apk_names)

    # input source apk
    # apk_name = "iBooks for Android Advice_v4.7_apkpure.com"
    # apk_src = f"../../apps/apks/{apk_name}.apk" 
    # output source code
    # for apk_src, apk_name in zip(apk_files, apk_names):
    #     apk_dst = f"{apk_codes_path}/{apk_name}"
    #     decompile_apk(apk_src, apk_dst)
    # check dir and apk file
    # if file_dir_exist(apk_dst) and check_apk(apk_src):
    #     run_scan(apk_dst)

if __name__ == "__main__":
    main()
    
from scan_codes import ScanCodes
from os import path
# Todo import from parent directory
from apk_process import decompile_apk

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
    # ============== title =============
    total_len = 100
    decoration = "=" * ((total_len - len(title) - 1) // 2)
    print(decoration + " " + title + " " + decoration)

def main():
    # zip_src = "../apps/apks_upzip/0a37f086841ff927ec8bee9f3bdb1048ecfba54b09aea400e980bd3ef301519d.77f09f214993016fbc747b5bafa5f94f.zip"
    # input source apk
    apk_src = "../../apps/apks/0ac4aa9b5413666a2bd66b96faa0cc8e656144ffcd351101071f8d028970befa.2fd32776a17d88eaa6fb2bcd792695f0.apk" 
    # output source code
    apk_dst = "../../apps/apks_codes/0ac4aa9b5413666a2bd66b96faa0cc8e656144ffcd351101071f8d028970befa.2fd32776a17d88eaa6fb2bcd792695f0"
    decompile_apk(apk_src, apk_dst)
    # check dir and apk file
    if file_dir_exist(apk_dst) and check_apk(apk_src):
        run_scan(apk_dst)

if __name__ == "__main__":
    main()
    
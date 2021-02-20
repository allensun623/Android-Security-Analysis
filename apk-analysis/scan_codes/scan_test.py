from scan_api import ScanAPI
from os import path

def run_scan(apk_src):
    print_title("Start Scanning...")
    scan_api = ScanAPI(apk_src)


def main():
    apk_src = "../apks_unzip/Instagram_v173.0.0.39.120_apkpure.com"
    if file_dir_exist(apk_src):
        run_scan(apk_src)


def file_dir_exist(target_path):
    exists = path.exists(target_path)
    if not exists:
        print("\"" + target_path + "\"" + " NOT EXISTS!")
    return exists

def print_title(title):
    # print break line with title
    # ============== title =============
    total_len = 100
    decoration = "=" * ((total_len - len(title) - 1) // 2)
    print(decoration + " " + title + " " + decoration)

if __name__ == "__main__":
    main()
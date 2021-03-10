from cordova_scan.cordova_analysis_codes import run_scan
from cordova_scan.cordova_analysis_codes import scan_folder

def print_title(title=""):
    # print break line with title
    # ============== title =============
    total_len = 100
    if title:
        decoration = "#" * ((total_len - len(title) - 1) // 2)
        print(decoration + " " + title + " " + decoration)
    else:
        print("#" * 101)

def main():
    print_title("Start Scanning...")
    # directory for apk source codes
    dir_src = "../apps/apks_codes/chirag/"
    # directory for output csv
    dir_output = "db/cordova/"
    l_apk_name = scan_folder(dir_src)
    run_scan(l_apk_name, dir_src, dir_output)

if __name__ == '__main__':
    main()
from cdv_scan.cdv_analysis_codes import run_scan
from cdv_scan.cdv_plugins import get_event_object
from cdv_scan.cdv_plugins import get_object_l


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
    dir_src = "../apps/apks_codes/cdv_apk/"
    # directory for output csv
    dir_output = "db/cdv/"
    # main source folder
    main_folders = ["apktools/assets/www/"]
    # main files for scanning
    main_extentions = [".js", ".html", ".mustache"]
    # main targets for scanning
    main_targets = get_object_l()
    # Hybrid apks
    run_scan(dir_src, dir_output, main_folders, main_extentions, main_targets)


if __name__ == '__main__':
    main()
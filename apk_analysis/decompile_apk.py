from os import listdir
from shutil import copy2
from analysis_apk import DecompileAPK


def scan_apk(apk_dir_path, apk_unzip_dir_path):
    # Scan all android files under specific directory
    print_title("SCAN APKS")
    print("Start scanning...")
    print(f"Targer folder: {apk_dir_path}")
    apks = None
    try:
        apks = listdir(apk_dir_path)
    except Exception as err:
        print(err)

    if apks:
        print(f"Total APKs Scanned: {len(apks)}")
        # read_apk(apks[0], apk_dir_path, apk_unzip_dir_path)
        apks_zip = copy_apks(apks, apk_dir_path, apk_unzip_dir_path)
        if apks_zip:
            analysis(apks, apk_dir_path, apks_zip, apk_unzip_dir_path)
    # return apks


def copy_apks(apks, apk_dir_path, apk_unzip_dir_path):
    # copy apks as zip files to a new folder
    print_title("COPY APK TO ZIP")
    print(f"Start Copying...")
    print(f"Direction folder: {apk_dir_path}")
    try:
        # remove suffix "apk"
        apks_zip = [apk[:-3] + "zip" for apk in apks]
        for apk, apk_zip in zip(apks, apks_zip):
            src = apk_dir_path + "/" + apk
            dst = apk_unzip_dir_path + "/" + apk_zip
            copy2(src, dst)
        print("Finish copy.")
        print(f"Total APKs: {len(apks)}")
        print(f"Successful ZIPs: {len(apks_zip)}")
        return apks_zip

    except Exception as err:
        print(err)
        return False


def analysis(apks, apk_dir_path, apks_zip, apk_unzip_dir_path):
    print_title("ANALYZING APK")
    for apk, apk_zip in zip(apks, apks_zip):
        apk_src = apk_dir_path + "/" + apk
        zip_src = apk_unzip_dir_path + "/" + apk_zip
        # destinate folder for unzip file
        apk_dst = apk_unzip_dir_path + "/" + apk_zip[:-4]
        apk_analysis = DecompileAPK(apk_src, zip_src, apk_dst)
        # apk_analysis.unzip_apk()
        apk_analysis.decompile_apk()
        # break

def print_title(title):
    # print break line with title
    # ============== title =============
    total_len = 100
    decoration = "=" * ((total_len - len(title) - 1) // 2)
    print(decoration + " " + title + " " + decoration)


def main():
    apk_dir_path = "./apks"
    apk_unzip_dir_path = "./apks_unzip"
    scan_apk(apk_dir_path, apk_unzip_dir_path)


if __name__ == "__main__":
    main()

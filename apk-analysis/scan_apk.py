from os import listdir
from shutil import copy2
import analysis_apk

def scan_apk(apk_dir_path, apk_unzip_dir_path):
    # Scan all android files under specific directory
    print("=" * 30 + " SCAN APKS " + "=" * 30)
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
            analysis(apks_zip)
    # return apks

def copy_apks(apks, apk_dir_path, apk_unzip_dir_path):
    print("=" * 30 + " COPY APK TO ZIP " + "=" * 30)
    print(f"Start Copying...")
    print(f"Direction folder: {apk_dir_path}")
    # remove suffix "apk"
    try: 
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

def analysis(apks_zip):
    for apk in apks_zip:
        analysis = analysis_apk.Analysis_apk(apk)


# def upzip(apk_name, apk_dir_path, apk_unzip_dir_path):
#     print(f"Analizing {apk_name}")

def main():
    apk_dir_path = "./apks"
    apk_unzip_dir_path = "./apks_unzip"
    scan_apk(apk_dir_path, apk_unzip_dir_path)

if __name__ == "__main__":
    main()

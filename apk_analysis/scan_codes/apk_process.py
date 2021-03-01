import zipfile
import apk2java

def unzip_apk(apk_src, apk_dst):
    # unzip apk
    try:
        with zipfile.ZipFile(apk_src, 'r') as zip_ref:
            zip_ref.extractall(apk_dst)
    except Exception as err:
        print(err)

def apk_decompile(apk_codes_path, apk_files, apk_names):
    # Decompile a list of APKs
    print_title("Start Decompile")
    for i, apk_src, apk_name in enumerate(zip(apk_files, apk_names)):
        print_title(f"At {i}/{len(apk_files)} decompiling...")
        apk_dst = f"{apk_codes_path}/{apk_name}"
        decompile_apk(apk_src, apk_dst)

def decompile_apk(apk_src, apk_dst):
    # Decompile a single APK
    print(apk_src, apk_dst)
    try:
        apk2java.decompile(apk_src, apk_dst)
    except Exception as err:
        print(err)

def print_title(title):
    # print break line with title
    # ############# title #############
    total_len = 100
    decoration = "#" * ((total_len - len(title) - 1) // 2)
    print(decoration + " " + title + " " + decoration)
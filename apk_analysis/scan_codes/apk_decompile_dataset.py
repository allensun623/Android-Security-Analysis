# from scan_codes import ScanCodes
# Todo import from parent directory
from os import walk
from os import path
import apk2java
from os import system
from os import listdir
import threading
import multiprocessing
import time

# def run_scan(apk_src):
#     print_title("Start Scanning...")
#     scan_api = ScanCodes(apk_src)


def file_dir_exist(target_path):
    exists = False
    try:
        exists = path.exists(target_path)
    except Exception as e:
        print(e)
    if not exists:
        print('"' + str(target_path) + '"' + " NOT EXISTS!")
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
        print(f'Total ".apk" files scanned: {len(apk_files)}')
    else:
        print(f'Wrong source path or there is no .apk file in the path: "{dir_path}\n')
    return sorted(apk_files), sorted(apk_names)


def get_decompiled_apk(dir_path):
    try:
        decompiled_apks = sorted(listdir(dir_path))
        return decompiled_apks
    except Exception as e:
        return


def apk_decompile(apk_codes_path, apk_files, apk_names):
    # Threading
    print_title("Start Decompile")
    decompiled_apks = get_decompiled_apk(apk_codes_path)
    new_apks = []

    max_threads = 20
    threads = list()

    for i, (apk_src, apk_name) in enumerate(zip(apk_files, apk_names)):
        if apk_name not in decompiled_apks:
            new_apks.append(apk_name)
            print_title(f"At {i+1}/{len(apk_files)} decompiling...")
            apk_dst = f"{apk_codes_path}/{apk_name}"

            if len(threads) >= max_threads or (i + 1 == len(apk_files)):
                for t in threads:
                    t.start()

                for one_thread in threads:
                    one_thread.join()
                threads = list()

            # multiprocessing
            # p = multiprocessing.Process(target=decompile_apk, args=(apk_src, apk_dst,))
            # threads.append(p)
            # p.start()

            # threading
            t = threading.Thread(
                target=decompile_apk,
                args=(
                    apk_src,
                    apk_dst,
                ),
            )
            threads.append(t)
            # t.start()

    # print(len(new_apks), len(apk_names))
    # decompile_apk_command(apk_src, apk_dst)


def decompile_apk(apk_src, apk_dst):
    # Decompile a single APK
    print(apk_src, apk_dst)
    try:
        apk2java.decompile(apk_src, apk_dst)
    except Exception as err:
        print(err)


def decompile_apk_command(apk_src, apk_dst):
    # Decompile a single APK with command
    print(apk_src, apk_dst)
    command = f"apktool d -f -r {apk_src}"
    try:
        system(command)
    except Exception as err:
        print(err)


def main():
    # zip_src = "../../apps/apks_upzip/0a37f086841ff927ec8bee9f3bdb1048ecfba54b09aea400e980bd3ef301519d.77f09f214993016fbc747b5bafa5f94f.zip"
    dir_path = "../../apps/apks/cdv_apk"
    apk_codes_path = "../../apps/apks_codes/cdv_apk"
    # dir_path = "../../apps/apks/threading_test"
    # apk_codes_path = "../../apps/apks_codes/threading_test"
    apk_files, apk_names = get_apks(dir_path)
    # decompile a list of apks
    apk_decompile(apk_codes_path, apk_files, apk_names)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

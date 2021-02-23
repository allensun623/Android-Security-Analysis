import zipfile
import apk2java

def unzip_apk(apk_src, apk_dst):
    # unzip apk
    try:
        with zipfile.ZipFile(apk_src, 'r') as zip_ref:
            zip_ref.extractall(apk_dst)
    except Exception as err:
        print(err)

def decompile_apk(apk_src, apk_dst):
    print(apk_src, apk_dst)
    try:
        apk2java.decompile(apk_src, apk_dst)
    except Exception as err:
        print(err)


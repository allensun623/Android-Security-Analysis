import zipfile


class Analysis_APK():
    def __init__(apk):
        self.apk = apk
        self.unzip_apk(apk)
    
    def unzip_apk(apk):
        # unzip apk
        try:
            with zipfile.ZipFile(apk, 'r') as zip_ref:
                zip_ref.extractall(".")
        except Exception as err:
            print(err)

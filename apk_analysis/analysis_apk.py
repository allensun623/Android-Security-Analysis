import zipfile
import apk2java

class DecompileAPK():
    def __init__(self, apk_src, zip_src, apk_dst):
        self.apk_src = apk_src
        self.zip_src = zip_src
        self.apk_dst = apk_dst
    
    def unzip_apk(self):
        # unzip apk
        try:
            with zipfile.ZipFile(self.apk_src, 'r') as zip_ref:
                zip_ref.extractall(self.apk_dst)
        except Exception as err:
            print(err)

    def decompile_apk(self):
        print(self.apk_src, self.apk_dst)
        try:
            apk2java.decompile(self.apk_src, self.apk_dst)
        except Exception as err:
            print(err)


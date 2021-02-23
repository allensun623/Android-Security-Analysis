import re
from collections import defaultdict
def get_api(target_file):
    with open (target_file, 'r') as source_file:
        source_code = source_file.read() 
        # find all apis match " public|protected|private|static ... ("
        match = re.findall(" (public|protected|private|static) (.*?)\(", source_code)
        # print(match)
        # get all methods as a list
        # methods = [m[1].split(" ")[-1] for m in match]
        # print(methods)
        d_methods = defaultdict(int)
        for m in match:
            # m is a set of (public|protected|private|static, string)
            method = m[1].split(" ")[-1]
            d_methods[method] += 1 
        print(d_methods)

def get_permission(target_file):
    try:
        with open (target_file, 'r') as source_file:
            source_code = source_file.read() 
            # e.g. <uses-permission android:name="android.permission.INTERNET"/>
            match = re.findall("<uses-permission android:name=(.*?)\/\>", source_code)
            # remove quotes and store as a list
            permissions = [m[1:-1] for m in match]
            # print(permissions)
        return permissions
    except Exception as err:
        print(err)
        return 

def main():
    apt_src = "../../apps/apks_codes/0a37f086841ff927ec8bee9f3bdb1048ecfba54b09aea400e980bd3ef301519d.77f09f214993016fbc747b5bafa5f94f"
    target_file = "/apktools/AndroidManifest.xml"
    permissions = get_permission(apt_src + target_file)
    print(permissions)

if __name__ == '__main__':
    main()
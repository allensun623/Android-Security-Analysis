import re
from cdv_plugins import get_object

def find_all():
    target_path = "cordova.js"
    with open (target_path, 'r') as source_file:
        source_code = source_file.read() 
        find_string = "|".join(get_object())
        match = re.findall(f"({find_string})", source_code)
        print(match)


def main():
    find_all()

if __name__ == '__main__': 
    main()
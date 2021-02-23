from scan_codes import ScanCodes


def analysis_api(d_methods):
    print(d_methods)

def analysis_permissions(l_permission):
    print(l_permission)

def print_title(title):
    # print break line with title
    # ============== title =============
    total_len = 100
    decoration = "=" * ((total_len - len(title) - 1) // 2)
    print(decoration + " " + title + " " + decoration)

def main():
    print_title("Start Scanning...")
    apk_src = "../../apps/apks_codes/0a37f086841ff927ec8bee9f3bdb1048ecfba54b09aea400e980bd3ef301519d.77f09f214993016fbc747b5bafa5f94f"
    scan_codes = ScanCodes(apk_src)
    # analysis_api(scan_codes.d_methods)
    analysis_permissions(scan_codes.l_permission)


if __name__ == '__main__':
    main()
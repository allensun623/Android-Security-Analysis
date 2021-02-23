# Android-Security-Analysis

## Decompile
- install apktool
[installation of apktool](https://stackoverflow.com/questions/34336338/apktool-command-not-found-error)

Mac: 
```

```


## Scan
* `extract_apk.py`
    * input source apk: apk_src
    * output decompiled source code: apk_dst
        * `from apk_process import decompile_apk`
        * `decompile_apk(apk_src, apk_dst)`
    * scan all methods of .java files
        * `from scan_codes import ScanCodes`
        * `scan_codes = ScanCodes(apk_src)`

* `scan_codes.py` 
    * scan all .java files under the folder `src`.
    * Extract all methods from obtained java files and store as a dict.

* `apk_process.py`
    * decompile an apk
    * unzip an apk

* `analysis_codes.py`
    * analyze a single apk and its source codes for testing
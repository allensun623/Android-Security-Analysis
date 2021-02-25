# Android-Security-Analysis

## Decompile
* install apktool
[installation of apktool](https://stackoverflow.com/questions/34336338/apktool-command-not-found-error)

Mac: 
```

```


## Scan


* `analysis_codes.py`
    * analyze a list of apks and its source codes for testing
    * output features of apis and permissions as a csv file
        * columns: features
        * rows: samples

* `extract_apk.py`
    * input source apk: apk_src
    * output decompiled source code: apk_dst
        * `from apk_process import decompile_apk`
        * `decompile_apk(apk_src, apk_dst)`
    * scan all methods of .java files
        * `from scan_codes import ScanCodes`
        * `scan_codes = ScanCodes(apk_src)`

* `scan_codes.py` 
    * scan all .java files under the directory `src`.
    * Extract all methods from obtained java files and store as a dict.
    * Extract all permission from AndroidManifest.xml and store as a list.

* `apk_process.py`
    * decompile an apk
    * unzip an apk




# DATASET
[CICMalDroid 2020](https://www.unb.ca/cic/datasets/maldroid-2020.html)
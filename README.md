# Android-Security-Analysis

## Decompile
* install apktool
[installation of apktool](https://stackoverflow.com/questions/34336338/apktool-command-not-found-error)

Mac: 
```

```


## Scan

### cdv_scan
* `output_csv.py`
    * Input: 
        * dictionaries: apk_names, apis,  permissions
        * the output directory path
    * Output: csv files
        * cordova_APIs.csv
        * cordova_PERMISSIONs.csv
        * cordova_FEATUREs.csv


* `analysis_codes.py`
    * data
        * input: source codes of a list of apks
        * output: csv files for extracted permission, API, and combined features respectively
    * analyze a list of apks and its source codes for testing
    * output features of apis and permissions as a csv file
        * columns: features
        * rows: samples 

* `apk_decompile_dataset.py`
    * decompile all apks under a directory
    * use command "apktool d -f -r {apk_src}" to decompile apk
        * need to install apktool to system
        * output folder would be the current folder



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

## Feature Set
- core plugins:
    ```
    ['battery-status', 'camera', 'contacts', 'device', 'dialogs', 'file','geolocation', 'globalization', 'inappbrowser', 'media', 'media-capture','network-information', 'splashscreen', 'statusbar', 'vibration']
    ```
- prefix
    - u -> plugin usage: the plugin is used in apk 
        - e.g. `u_battery-status`, `u_camera`
    - d -> plugin declaration: the plugin is declared in `config.xml` or `plugins.xml`
        - e.g. `d_battery-status`, `d_camera`
    - p -> plugin permission: the plugin is detected with full permissions in `AndroidManifest.xml`
        - e.g. `p_battery-status`, `p_camera`

- table shape: 2659 rows × 905 columns
    - 2659 APKs
    - 905 features

- Feature values: all feature values are binary
    - 1 -> detected (contains, exists)
    - 0 -> not detected (not contains, not exists)

|  Feature |  Description | 
|  --- | --- |
| apk_name | The name of cordova apk | 
| u_battery-status | The plugin battery-status is used in apk | 
| ... | ... | 
| u_vibration | The plugin vibration is used in apk | 
| d_battery-status | The plugin battery-status is declared in `config.xml` or `plugins.xml` | 
| ... | ... | 
| d_vibration | The plugin vibration is declared in `config.xml` or `plugins.xml` |
| config.xml | Whether the file `config.xml` exists in the apk | 
| plugins.xml | Whether the file `plugins.xml` exists in the apk |
| p_battery-status | The plugin battery-status is detected with full permissions in `AndroidManifest.xml`|
| ... | ... | 
| p_vibration | The plugin vibration is detected with full permissions in `AndroidManifest.xml` | 
| android.permission.ACCESS_NETWORK_STATE | Whether the permission is detected in `AndroidManifest.xml` | 
| android.permission.READ_PHONE_STATE | Whether the permission is detected in `AndroidManifest.xml` | 
| ... | ... | 
| wtdt.resgrid.andriod.permission.C2D_MESSAGE | Whether the permission is detected in `AndroidManifest.xml` | 
| yonatan.benmoshe.permission.C2D_MESSAGE | Whether the permission is detected in `AndroidManifest.xml` | 
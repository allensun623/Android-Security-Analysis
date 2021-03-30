"""
copy from cdv_scan/cdv_plugins
d_plugins
    use example
    plugin: {
        "name": "",  # plugin name defined in plugin.xml and config.xml
        "object": "",  # API call
        "method": [],
        "property": [],
        "event": [],  
        "permission: []
        # "java_class": [],
    }

"""

d_plugins = {
    # // We get the initial value when the promise resolves ...
    # navigator.getBattery().then(function(battery) {
    # console.log(battery.level);
    # // ... and any subsequent updates.
    # battery.onlevelchange = function() {
    #     console.log(this.level);
    # };
    # });
    "battery-status": {
        "name": "Battery",
        # "object": "navigator.getBattery",
        "object": "batterystatus",  # use event to call battery
        "method": [],
        "property": [],
        "event": ["batterystatus", "batterycritical", "batterylow"],
        "permission": [],
        # "java_class": ["BatteryListener.java"],
    },
    # navigator.camera.getPicture(cameraSuccess, cameraError, cameraOptions);
    "camera": {
        "name": "Camera",
        "object": "navigator.camera",
        "method": ["getPicture", "cleanup", "onError", "onSuccess", "CameraOptions"],
        "property": [],
        "event": ["Camera."],
        "java_class": [],
        "permission": ["android.permission.WRITE_EXTERNAL_STORAGE"],
    },
    # var myContact = navigator.contacts.create({"displayName": "Test User"});
    "contacts": {
        "name": "Contacts",
        "object": "navigator.contacts",
        "method": ["create", "find", "pickContact"],
        "property": [],
        "event": [
            "ContactName",
            "ContactField",
            "ContactAddress",
            "ContactOrganization",
            "ContactFindOptions",
            "ContactError",
            "ContactFieldType",
        ],  # they are objects, store as event for extraction
        "java_class": [],
        "permission": [
            "android.permission.READ_CONTACTS",
            "android.permission.WRITE_CONTACTS",
            "android.permission.GET_ACCOUNTS",
        ],
    },
    # var string = device.platform;
    "device": {
        "name": "Device",
        "object": "device",
        "method": [],
        "property": [
            "cordova",
            "model",
            "platform",
            "uuid",
            "version",
            "manufacturer",
            "isVirtual",
            "serial",
        ],
        "event": [],
        "permission": [],
    },
    "dialogs": {
        "name": "Notification",
        "object": "navigator.notification",
        "method": [
            "alert",
            "confirm",
            "prompt",
            "beep",
            "dismissPrevious",
            "dismissAll",
        ],
        "property": [],
        "event": [],
        "permission": [],
    },
    # document.addEventListener("deviceready", onDeviceReady, false);
    # function onDeviceReady() {
    #     console.log(cordova.file);
    # }
    # TODO - Android file
    "file": {
        "name": "File",
        "object": "file",
        "method": [
            "resolveLocalFileSystemURL",
            "applicationDirectory",
            "applicationStorageDirectory",
            "dataDirectory",
            "cacheDirectory",
            "externalApplicationStorageDirectory",
            "externalDataDirectory",
            "externalCacheDirectory",
            "externalRootDirectory",
            "tempDirectory",
            "syncedDataDirectory",
            "documentsDirectory",
            "sharedDirectory",
        ],
        "property": [],
        "event": ["requestFileSystem", "resolveLocalFileSystemURL"],
        "permission": ["android.permission.WRITE_EXTERNAL_STORAGE"],
    },
    # navigator.geolocation.getCurrentPosition(geolocationSuccess, [geolocationError], [geolocationOptions]);
    "geolocation": {
        "name": "Geolocation",
        "object": "navigator.geolocation",
        "method": ["getCurrentPosition", "watchPosition", "clearWatch"],
        "property": [],
        "event": [],
        "permission": [
            "android.permission.ACCESS_COARSE_LOCATION",
            "android.permission.ACCESS_FINE_LOCATION",
        ],
    },
    # console.log(navigator.globalization);
    "globalization": {
        "name": "Globalization",
        "object": "navigator.globalization",
        "method": [
            "getPreferredLanguage",
            "getLocaleName",
            "dateToString",
            "stringToDate",
            "getDatePattern",
            "getDateNames",
            "isDayLightSavingsTime",
            "getFirstDayOfWeek",
            "numberToString",
            "stringToNumber",
            "getNumberPattern",
            "getCurrencyPattern",
        ],
        "property": [],
        "event": [],
        "permission": [],
    },
    # var ref = cordova.InAppBrowser.open('http://apache.org', '_blank', 'location=yes');
    # var iab = cordova.InAppBrowser;
    # iab.open('local-url.html'); // loads in the Cordova WebView
    "inappbrowser": {
        "name": "InAppBrowser",
        "object": "cordova.InAppBrowser",
        "method": ["open"],
        "property": [],
        "event": [],
        "permission": [],
    },
    # var my_media = new Media(src, onSuccess, onError);
    # my_media.startRecord();
    "media": {
        "name": "Media",
        "object": "new Media",
        "method": [
            "getCurrentAmplitude",
            "getCurrentPosition",
            "getDuration",
            "play",
            "pause",
            "pauseRecord",
            "release",
            "resumeRecord",
            "seekTo",
            "setVolume",
            "startRecord",
            "stopRecord",
            "stop",
            "setRate",
        ],
        "property": [],
        "event": [],
        "permission": [
            "android.permission.RECORD_AUDIO",
            "android.permission.MODIFY_AUDIO_SETTINGS",
            "android.permission.WRITE_EXTERNAL_STORAGE",
            "android.permission.READ_PHONE_STATE",
        ],
    },
    # navigator.device.capture.captureVideo(captureSuccess, captureError, {limit:2});
    "media-capture": {
        "name": "Capture",
        "object": "navigator.device.capture",
        "method": ["captureAudio", "captureImage", "captureVideo"],
        "property": [],
        "event": [],
        "permission": [
            "android.permission.RECORD_AUDIO",
            "android.permission.RECORD_VIDEO",
            "android.permission.READ_EXTERNAL_STORAGE",
            "android.permission.WRITE_EXTERNAL_STORAGE",
        ],
    },
    # var networkState = navigator.connection.type;
    "network-information": {
        "name": "NetworkStatus",
        "object": "navigator.connection",
        "method": [],
        "property": ["type"],
        "event": ["offline"],
        "permission": ["android.permission.ACCESS_NETWORK_STATE"],
    },
    # // set to either landscape
    # screen.orientation.lock('landscape');
    # // allow user rotate
    # screen.orientation.unlock();
    # // access current orientation
    # console.log('Orientation is ' + screen.orientation.type);
    # "screen-orientation": {
    #     "name": "CDVOrientation",
    #     "object": "screen.orientation",
    #     "method": ["lock", "unlock"],
    #     "property": ["type"],
    #     "event": ["orientationchange"],
    # },
    # setTimeout(function() {
    #   navigator.splashscreen.hide();
    # }, 2000);
    "splashscreen": {
        "name": "SplashScreen",
        "object": "navigator.splashscreen",
        "method": ["show", "hide"],
        "property": [],
        "event": [],
        "permission": [],
    },
    # StatusBar.overlaysWebView(true);
    # if (StatusBar.isVisible) {
    # // do something
    # }
    "statusbar": {
        "name": "StatusBar",
        "object": "StatusBar",
        "method": [
            "overlaysWebView",
            "styleDefault",
            "styleLightContent",
            "styleBlackTranslucent",
            "styleBlackOpaque",
            "backgroundColorByName",
            "backgroundColorByHexString",
            "hide",
            "show",
        ],
        "property": ["isVisible"],
        "event": ["statusTap"],
        "permission": [],
    },
    # document.addEventListener("deviceready", onDeviceReady, false);
    # function onDeviceReady() {
    #     console.log(navigator.vibrate);
    # }
    "vibration": {
        "name": "Vibration",
        "object": "navigator.vibrate",
        "method": [],
        "property": [],
        "event": [],
        "permission": ["android.permission.VIBRATE"],
    },
}

# TODO - Redesign get event, method, object
# TODO - Third party library:
# TODO -    Google Map JavaScript Library


def get_func():
    # return all functions(["method", "property", "event"]) of all plugins as one list
    # [plugin1.function1, plugin1.function2, ..., ]
    l_func = []
    values = ["method", "property"]
    for funcs in d_plugins.values():
        plugin_obj = funcs["object"]
        for v in values:
            for func in funcs[v]:
                l_func.append[f"{plugin_obj}.{func}"]
    return l_func


def get_plugin():
    # return all plugins as a list
    # [plugin1, plugin2, ]
    return d_plugins.keys()

def get_plugin_d():
    # return all plugins as a dictionary {plugin1:0, plugin1:0, ...}
    # [plugin1, plugin2, ]
    return {p:0 for p in d_plugins.keys()}

def get_plugin_object_d():
    # return plugin and object of API call as a dictionary:
    # [object1: plugin1, object2: plugin2...]
    return {v["object"]: plugin for plugin, v in d_plugins.items()}


def get_name_plugin_d():
    # return plugin and name of API call as a dictionary:
    # [name1: plugin1, name2: plugin2...]
    return {v["name"]: plugin for plugin, v in d_plugins.items()}


def get_plugin_name_d():
    # return plugin and name of API call as a dictionary:
    # [name1: plugin1, name2: plugin2...]
    return {plugin: v["name"] for plugin, v in d_plugins.items()}


def get_event_object():
    # return event and object of API call as a {key, value} pair:
    # [event1_object1, event2_object1, object1, event1_object2, ...]
    l_temp = []
    for v in d_plugins.values():
        event = v["event"]
        if event:
            l_temp.extend(event)
        l_temp.append(v["object"])
    return l_temp


def get_event_object_d():
    # return event and object of API call as a list:
    # [event1_object1: object1, event2_object1: object1, object1: object1, event1_object2: object2 , ...]
    d_temp = {}
    for v in d_plugins.values():
        event = v["event"]
        for e in event:
            d_temp[e] = v["object"]
        d_temp[v["object"]] = v["object"]
    return d_temp


def get_object_l():
    # return object of API call as a list:
    return [v["object"] for v in d_plugins.values()]


def get_object_d():
    # return object of API call as a dictionary {object:0}:
    return {obj: 0 for obj in get_object_l()}


def get_plugin_permission_d():
    # return permissions of plugin as a dictionary {plugin:[permissions]}:
    return {plugin: v["permission"] for plugin, v in d_plugins.items()}

def get_plugin_permission_require_l():
        # return plugins that require permissions as a dictionary plugin}:
    return [plugin for plugin, v in d_plugins.items() if v["permission"]]

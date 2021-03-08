d_plugins = {
    "battery": {
        "object": "window",
        "event": ["batterystatus", "batterycritical", "batterylow"],
    },
    "camera": {
        "object": "navigator.camera",
        "method": ["getPicture", "cleanup", "onError", "onSuccess", "CameraOptions"],
    },
    "device": {
        "object": "device",
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
    },
    "dialogs": {
        "object": "navigator.notification",
        "method": [
            "alert",
            "confirm",
            "prompt",
            "beep",
            "dismissPrevious",
            "dismissAll",
        ],
    },
    # TODO - define for android
    # ? Still NOT Get This?
    "file": [
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
    "geolocation": {
        "object": "navigator.geolocation",
        "method": ["getCurrentPosition", "watchPosition", "clearWatch"],
    },
    # var ref = cordova.InAppBrowser.open('http://apache.org', '_blank', 'location=yes');
    # var iab = cordova.InAppBrowser;
    # iab.open('local-url.html'); // loads in the Cordova WebView
    "InAppBrowser": {
        "object": "cordova.InAppBrowser",
        "method": ["open"],
    },

    # var my_media = new Media(src, onSuccess, onError);
    # my_media.startRecord();
    "media": {
        "object": "Media",
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
    },

    # navigator.device.capture.captureVideo(captureSuccess, captureError, {limit:2});
    "media-capture": {
        "object": "navigator.device.capture",
        "method": ["captureAudio", "captureImage", "captureVideo"]
    },

    "network-information": 
    ["connection", "checkConnection", "onOnline", "onOffline"],
    "screen-orientation": [
        "orientation",
        "screenLock",
        "screenUnlock",
        "orientationOnchange",
        "orientationType",
    ],
    "splashscreen": ["splashscreen", "splashscreenShow", "splashscreenHide"],
    "statusbar": [
        "statusbar",
        "backgroundColorByHexString",
        "overlaysWebView",
        "backgroundColorByHexString",
        "styleDefault",
        "styleLightContent",
        "styleBlackTranslucent",
        "styleBlackOpaque",
        "backgroundColorByName",
        "backgroundColorByHexString",
    ],
    "vibration": ["vibrate"],
}

# TODO - Redesign get event, method, object


def get_func():
    # return all functions of all plugins as one list
    # [plugin1_function1, plugin1_function2, ..., ]
    l_func = [func for funcs in d_plugins.values() for func in funcs]
    return l_func


def get_plugin():
    # return all plugins as a list
    # [plugin1, plugin2, ]
    return d_plugins.keys()


def get_plugin_func():
    # return all functions and plugins as one list
    # [plugin1_function1, plugin1_function2, ..., plugin1, ... plugin]
    l_plugins_func = []
    for plugin, funcs in d_plugins.items():
        l_plugins_func.extend(funcs)
        l_plugins_func.append(plugin)
    return l_plugins_func


def get_func_plugin_dict():
    # Todo - some plugin might have the same function name
    # return a dict of func and plugin pair
    # {function: plugin}
    d_func_plugin = {
        func: plugin for plugin, funcs in d_plugins.items() for func in funcs
    }
    return d_func_plugin
d_plugins = {
    "battery": [
        "getBattery",
        "onlevelchange",
        "updateBatteryStatus",
        "onchargingchange",
        "ondischargingtimechange",
    ],
    "camera": [
        "getPicture",
        "CameraOptions",
        "PictureSourceType",
        "PopoverArrowDirection",
        "CameraPopoverHandle",
        "CameraPopoverOptions",
    ],
    "device": ["device", "deviceready"],
    "dialogs": [
        "notification",
        "notification.alert",
        "notification.confirm",
        "notification.prompt",
        "notification.dismissAll",
        "notification.dismissPrevious",
        "notification.beep",
    ],
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
    "geolocation": ["geolocation", "getCurrentPosition", "watchPosition", "clearWatch"],
    "InAppBrowser": ["InAppBrowser"],
    "media": [
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
    "network-information": ["connection", "checkConnection", "onOnline", "onOffline"],
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


def get_func():
    # return all functions of all plugins as one list
    # [plugin1_function1, plugin1_function2, ..., ]
    l_func = [func for funcs in d_plugins.values() for func in funcs]
    return l_func


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
        func: plugin
        for plugin, funcs in d_plugins.items()
        for func in funcs
    }
    return d_func_plugin
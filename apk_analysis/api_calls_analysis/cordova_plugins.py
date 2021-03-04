d_plugins = {
    "battery": ["getBattery", "onlevelchange", "updateBatteryStatus", "onchargingchange", "ondischargingtimechange",],
    "camera": ["getPicture", "CameraOptions", "PictureSourceType", "PopoverArrowDirection", "CameraPopoverHandle", "CameraPopoverOptions",],
    "device": ["device", "deviceready"],
    "dialogs": ["notification", "notification.alert", "notification.confirm", "notification.prompt", "notification.dismissAll", "notification.dismissPrevious", "notification.beep"],
    "file": ["resolveLocalFileSystemURL", "applicationDirectory", "applicationStorageDirectory", "dataDirectory", "cacheDirectory", "externalApplicationStorageDirectory", "externalDataDirectory", "externalCacheDirectory", "externalRootDirectory", "tempDirectory", "syncedDataDirectory", "documentsDirectory", "sharedDirectory"],
    "geolocation": ["geolocation", "getCurrentPosition", "watchPosition", "clearWatch", ""],
    "InAppBrowser": ["InAppBrowser"],
    "media": ["getCurrentAmplitude", "getCurrentPosition", "getDuration", "play", "pause", "pauseRecord", "release", "resumeRecord", "seekTo", "setVolume", "startRecord", "stopRecord", "stop", "setRate"],
    "network-information": ["connection", "checkConnection", "onOnline", "onOffline", ""],
    "screen-orientation": ["orientation", "screenLock", "screenUnlock", "orientationOnchange", "orientationType"],
    "splashscreen": ["splashscreen", "splashscreenShow", "splashscreenHide"],
    "statusbar": ["statusbar", "backgroundColorByHexString", "overlaysWebView", "backgroundColorByHexString", "styleDefault", "styleLightContent", "styleBlackTranslucent", "styleBlackOpaque", "backgroundColorByName", "backgroundColorByHexString"],
    "vibration": ["vibrate"],
}

def get_plugins_func(self):
    # [plugin1_function1, plugin1_function2, ..., plugin1, ... plugin}
    # Todo - Use reduce function
    d_plugins_func = []
    for plugin, funcs in d_plugins.items():
        d_plugins_func.extend(funcs)
        d_plugins_func.append(plugin)
    
    return d_plugins_func
    
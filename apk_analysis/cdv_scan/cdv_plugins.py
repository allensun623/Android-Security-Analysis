"""
d_plugins
    use example
    plugin: {
        "object": "", 
        "method": [],
        "property": [],
        "event": [],  
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
    "battery": {
        "object": "navigator.getBattery",
        "method": [],
        "property": [],
        "event": ["batterystatus", "batterycritical", "batterylow"],
    },
    # navigator.camera.getPicture(cameraSuccess, cameraError, cameraOptions);
    "camera": {
        "object": "navigator.camera",
        "method": ["getPicture", "cleanup", "onError", "onSuccess", "CameraOptions"],
        "property": [],
        "event": ["Camera."],
    },
    # var string = device.platform;
    "device": {
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
        "property": [],
        "event": [],
    },
    # document.addEventListener("deviceready", onDeviceReady, false);
    # function onDeviceReady() {
    #     console.log(cordova.file);
    # }
    # TODO - Android file
    "file": {
        "object": "cordova.file",
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
    },
    # navigator.geolocation.getCurrentPosition(geolocationSuccess, [geolocationError], [geolocationOptions]);
    "geolocation": {
        "object": "navigator.geolocation",
        "method": ["getCurrentPosition", "watchPosition", "clearWatch"],
        "property": [],
        "event": [],
    },
    # var ref = cordova.InAppBrowser.open('http://apache.org', '_blank', 'location=yes');
    # var iab = cordova.InAppBrowser;
    # iab.open('local-url.html'); // loads in the Cordova WebView
    "InAppBrowser": {
        "object": "cordova.InAppBrowser",
        "method": ["open"],
        "property": [],
        "event": [],
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
        "property": [],
        "event": [],
    },
    # navigator.device.capture.captureVideo(captureSuccess, captureError, {limit:2});
    "media-capture": {
        "object": "navigator.device.capture",
        "method": ["captureAudio", "captureImage", "captureVideo"],
        "property": [],
        "event": [],
    },
    # var networkState = navigator.connection.type;
    "network-information": {
        "object": "navigator.connection",
        "method": [],
        "property": ["type"],
        "event": ["offline"],
    },
    # // set to either landscape
    # screen.orientation.lock('landscape');
    # // allow user rotate
    # screen.orientation.unlock();
    # // access current orientation
    # console.log('Orientation is ' + screen.orientation.type);
    "screen-orientation": {
        "object": "screen.orientation",
        "method": ["lock", "unlock"],
        "property": ["type"],
        "event": ["orientationchange"],
    },
    # setTimeout(function() {
    #   navigator.splashscreen.hide();
    # }, 2000);
    "splashscreen": {
        "object": "navigator.splashscreen",
        "method": ["show", "hide"],
        "property": [],
        "event": [],
    },
    # StatusBar.overlaysWebView(true);
    # if (StatusBar.isVisible) {
    # // do something
    # }
    "statusbar": {
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
    },
    # document.addEventListener("deviceready", onDeviceReady, false);
    # function onDeviceReady() {
    #     console.log(navigator.vibrate);
    # }
    "vibration": {
        "object": "navigator.vibrate",
        "method": [],
        "property": [],
        "event": [],
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


def get_plugin_object_d():
    # return plugin and object of API call as a dictionary:
    # [object1: plugin1, object2: plugin2...]
    return {v["object"]: plugin for plugin, v in d_plugins.items()}


def get_event_object():
    # return event and object of API call as a {key, value} pair:
    # [event1_object1, event2_object1, object1: object1, event1_object2, ...]
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


def get_object():
    # return object of API call as a list:
    return [v["object"] for v in d_plugins.values()]


def get_object_d():
    # return object of API call as a dictionary {object:0}:
    return {obj: 0 for obj in get_object()}

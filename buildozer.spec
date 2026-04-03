[app]
title = Paradise
package.name = paradise
package.domain = org.paradise

source.dir = .

source.include_exts = py,png,jpg,kv,atlas,json
source.include_patterns = *

version = 1.0.0

orientation = portrait
fullscreen = 0

requirements = python3, kivy==2.3.1, pillow, requests, urllib3, certifi, idna, charset-normalizer

android.permissions = INTERNET,ACCESS_NETWORK_STATE

android.api = 33
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a

android.accept_sdk_license = True
android.enable_androidx = True

p4a.bootstrap = sdl2

[buildozer]
log_level = 1
warn_on_root = 1

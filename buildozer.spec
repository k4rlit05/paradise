[app]
# (str) Title of your application
title = Paradise Trading App

# (str) Package name
package.name = paradisetrading

# (str) Package domain (needed for android packaging)
package.domain = org.paradise

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let's add atlas and txt just in case)
source.include_exts = py,kv,png,jpg,json,atlas,txt

# (str) Application version
version = 1.0.0

# (list) Application requirements
# Added 'requests' and 'urllib3' as they are common for trading apps
requirements = python3,kivy==2.3.0,pillow,openssl,requests,urllib3

# (str) Supported orientation
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API your app will support.
android.ndk_api = 21

# (bool) Use this to skip the license prompts that cause the "File Too Large" error
android.accept_sdk_license = True

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) indicates if the application should be signed for distribution
android.release = False

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = no, 1 = yes)
warn_on_root = 1

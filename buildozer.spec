[app]
# (str) Title of your application
title = Paradise Trading App

# (str) Package name
package.name = paradisetrading

# (str) Package domain
package.domain = org.paradise

# (str) Source code directory
source.dir = .

# (list) Source files to include
source.include_exts = py,kv,png,jpg,json,atlas,txt

# (str) Application version
version = 1.0.0

# (list) Application requirements
# Added hostpython3 and openssl for SSL/Trading connection support
requirements = python3,kivy==2.3.0,pillow,openssl,requests,urllib3,hostpython3

# (str) Supported orientation
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) python-for-android branch to use
# THIS IS THE FIX for the sdkmanager error
p4a.branch = develop

# (bool) Automatically accept SDK license agreements
android.accept_sdk_license = True

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) indicates if the application should be signed for distribution
android.release = False

[buildozer]
# (int) Log level (2 = debug to see exactly what's happening)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

[app]
# (str) Title of your application
title = Paradise Trading App

# (str) Package name
package.name = paradisetrading

# (str) Package domain
package.domain = org.paradise

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (ONLY ONE LINE ALLOWED HERE)
source.include_exts = py,kv,png,jpg,json,atlas,txt

# (str) Application version
version = 1.0.0

# (list) Application requirements (ONLY ONE LINE ALLOWED HERE)
requirements = python3,kivy==2.3.0,pillow,openssl,requests,urllib3,hostpython3

# (str) Supported orientation
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API (Use 34 for modern Play Store requirements)
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version (Updated to 28c for the develop branch)
android.ndk = 28c

# (int) Android NDK API
android.ndk_api = 21

# (bool) Use this to skip the license prompts
android.accept_sdk_license = True

# (str) python-for-android branch to use (Crucial for the sdkmanager fix)
p4a.branch = develop

# (list) The Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) indicates if the application should be signed for distribution
android.release = False

[buildozer]
# (int) Log level (2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

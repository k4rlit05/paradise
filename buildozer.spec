[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise
source.dir = .
source.include_exts = py,kv,png,jpg,json
version = 1.0.0

# Added libffi and openssl for trading API stability
requirements = python3,kivy==2.3.1,pillow,libffi,openssl,requests,urllib3,hostpython3

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# --- FIXED ANDROID CONFIG ---
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.sdk_api = 33
android.ndk = 25b

# Force this version to solve the "Aidl not found" error
android.build_tools_version = 33.0.2

android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.2'
android.use_androidx = True
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1

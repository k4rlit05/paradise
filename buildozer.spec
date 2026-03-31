[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise
source.dir = .
source.include_exts = py,kv,png,jpg,json,atlas,txt
version = 1.0.0

requirements = python3,kivy==2.3.0,pillow,openssl,requests,urllib3,hostpython3

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# --- STABLE SETTINGS ---
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.2'
android.accept_sdk_license = True
# -----------------------

[buildozer]
log_level = 2
warn_on_root = 1

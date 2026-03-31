[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise
source.dir = .
source.include_exts = py,kv,png,jpg,json,atlas,txt
version = 1.0.0

# Added 'openssl' and 'requests' for trading API stability
requirements = python3,kivy==2.3.0,pillow,openssl,requests,urllib3,hostpython3

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# Match NDK 25b and API 31 for stability
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a

# CRITICAL FIXES
android.accept_sdk_license = True
android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.2'

[buildozer]
log_level = 2

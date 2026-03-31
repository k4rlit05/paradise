[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise

source.dir = .
source.include_exts = py,kv,png,jpg,json

version = 1.0.0

# Fixed for modern compatibility
requirements = python3,kivy==2.3.1,pillow,hostpython3

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# 2026 Android Standards (API 35 is Android 15)
android.api = 35
android.minapi = 21
android.sdk_api = 35
android.build_tools_version = 35.0.0
android.ndk_api = 21

# Modern phone support (Required for Play Store)
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1

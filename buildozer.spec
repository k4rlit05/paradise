[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise

source.dir = .
source.include_exts = py,kv,png,jpg,json

version = 1.0.0

requirements = python3,kivy==2.3.1,pillow

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# --- FIXED PATHS (NO $HOME) ---
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
android.sdk_api = 33
android.build_tools_version = 34.0.0

android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1

android.accept_sdk_license = True

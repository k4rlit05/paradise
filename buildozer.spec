[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise

source.dir = .
source.include_exts = py,kv,png,jpg,json

version = 1.0.0

requirements = python3,kivy==2.3.1,pillow,requests,urllib3,cython<3

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# --- ANDROID CONFIG ---
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.sdk_api = 33

android.build_tools_version = 33.0.2

android.sdk_path =
android.ndk_path =

android.gradle_dependencies = com.android.tools.build:gradle:7.4.2
android.use_androidx = True
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1

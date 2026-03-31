[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise

source.dir = .
source.include_exts = py,kv,png,jpg,json,atlas,txt
version = 1.0.0

# Requirements: Added 'openssl' and 'hostpython3' for compilation stability
requirements = python3,kivy==2.3.0,pillow,openssl,requests,urllib3,hostpython3

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# --- STABLE ANDROID SETTINGS (From your successful 20min run) ---
android.api = 34
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# Modern phone support
android.archs = arm64-v8a, armeabi-v7a

# Fixes the Gradle download crash
android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.2'
android.accept_sdk_license = True
# -------------------------------

[buildozer]
log_level = 2
warn_on_root = 1

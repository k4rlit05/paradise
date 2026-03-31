[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise

source.dir = .
source.include_exts = py,kv,png,jpg,json
version = 1.0.0

# Stable requirements
requirements = python3,kivy==2.3.0,pillow

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# --- STABLE ANDROID SETTINGS ---
android.api = 34
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# Modern phone support
android.archs = arm64-v8a, armeabi-v7a

# This specific line fixes the "Gradle Download Error"
android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.2'
# -------------------------------

[buildozer]
log_level = 2
warn_on_root = 1

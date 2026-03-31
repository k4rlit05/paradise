[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise

source.dir = .
source.include_exts = py,kv,png,jpg,json
version = 1.0.0

# ADDED 'openssl' here to fix the -lssl error
requirements = python3,kivy==2.3.0,pillow,openssl

orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# --- STABLE ANDROID SETTINGS ---
android.api = 34
android.minapi = 21
# Critical: NDK 25b is the most stable for OpenSSL builds
android.ndk = 25b
android.ndk_api = 21

# Modern phone support
android.archs = arm64-v8a, armeabi-v7a

# Fixes the Gradle download crash
android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.2'
# -------------------------------

[buildozer]
log_level = 2
warn_on_root = 1

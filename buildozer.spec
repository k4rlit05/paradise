[app]
# (str) Title of your application
title = Paradise Trading App

# (str) Package name
package.name = paradisetrading

# (str) Package domain (needed for android packaging)
package.domain = org.paradise

# (list) Source files to include
source.include_exts = py,kv,png,jpg,json,atlas,txt

# (list) Application requirements
# Added 'requests' and 'openssl' as trading apps usually need API access
requirements = python3,kivy==2.3.0,pillow,openssl,requests,urllib3,hostpython3

# (list) Permissions
# Critical for trading/data apps
android.permissions = INTERNET

# --- ANDROID SPECIFIC SETTINGS ---
# API 31 is the standard for most modern Play Store requirements
android.api = 31
android.minapi = 21

# NDK 25b is highly stable for Kivy 2.3.0
android.ndk = 25b
android.ndk_api = 21

# Modern phone architectures (includes 64-bit support)
android.archs = arm64-v8a, armeabi-v7a

# This line is CRITICAL for the GitHub Action to work
android.accept_sdk_license = True

# Fixes a common Gradle download error in CI environments
android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.2'

[buildozer]
# (int) Log level (2 will give us more detail if it fails)
log_level = 2

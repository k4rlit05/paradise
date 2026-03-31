[app]
# (str) Title of your application
title = Paradise Trading App

# (str) Package name
package.name = paradisetrading

# (str) Package domain (needed for android packaging)
package.domain = org.paradise

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let's include everything needed)
source.include_exts = py,kv,png,jpg,json,atlas,txt

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
# hostpython3 is added to ensure the build environment is stable
requirements = python3,kivy==2.3.0,pillow,openssl,requests,urllib3,hostpython3

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# --- ANDROID SPECIFIC SETTINGS ---
# Using API 31/33 for maximum compatibility with NDK 25b
android.api = 31
android.minapi = 21

# This MUST match what the YAML is preparing
android.ndk = 25b
android.ndk_api = 21

# Modern phone architectures
android.archs = arm64-v8a, armeabi-v7a

# Fixes the Gradle download crash
android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.2'

# Allow Buildozer to accept the licenses automatically
android.accept_sdk_license = True

# (int) Log level (2 = Error/Info, 1 = Error only)
log_level = 2

# (int) Display warning if buildozer is run as root (1 = yes)
warn_on_root = 1

[buildozer]
# (int) Log level
log_level = 2

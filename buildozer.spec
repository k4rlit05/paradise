[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise
source.dir = .
source.include_exts = py,kv,png,jpg,json,atlas,txt
version = 1.0.0

# Requirements (Added hostpython3 to ensure smooth compilation)
requirements = python3,kivy==2.3.0,pillow,openssl,requests,urllib3,hostpython3

orientation = portrait
android.permissions = INTERNET
android.api = 34
android.minapi = 21

# IMPORTANT: Using NDK 28c with the develop branch 
# fixes the modern Android SDK pathing issues.
android.ndk = 28c
p4a.branch = develop

android.ndk_api = 21
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a
android.release = False

[buildozer]
log_level = 2
warn_on_root = 1

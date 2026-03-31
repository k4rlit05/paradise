[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise
source.dir = .
source.include_exts = py,kv,png,jpg,json
version = 1.0.0

# This line is the most important part for the Buildozer fix
requirements = python3,kivy==2.3.0,pillow,openssl

orientation = portrait
android.permissions = INTERNET
android.api = 34
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1

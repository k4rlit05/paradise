[app]
title = Paradise
package.name = paradise
package.domain = org.paradise
source.dir = paradise
version = 1.0.0
orientation = portrait
fullscreen = 0

requirements = python3,kivy==2.3.0,pillow,openssl,requests,urllib3,libffi,hostpython3

android.permissions = INTERNET

android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.2'
android.use_setup_py = False

[buildozer]
log_level = 2
warn_on_root = 1

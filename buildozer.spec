[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise

source.dir = .
source.include_exts = py,kv,png,jpg,json

version = 1.0.0

# Critical: Use Kivy 2.3.1 for modern Android compatibility
requirements = python3,kivy==2.3.1,pillow,hostpython3

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# 2026 Play Store Requirements
android.api = 35
android.minapi = 21
android.sdk_api = 35
android.build_tools_version = 35.0.0
android.ndk_api = 21

# Architecture for all modern devices
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1

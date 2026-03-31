[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise

source.dir = .
source.include_exts = py,kv,png,jpg,json

version = 1.0.0

# ADDED: hostpython3 is required for the compilation process
requirements = python3,kivy==2.3.1,pillow,hostpython3

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# --- ANDROID CONFIG ---
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.sdk_api = 33
android.build_tools_version = 33.0.2

# FIXED: Commented these out. GitHub Actions will provide these automatically.
# android.sdk_path = /home/runner/android-sdk
# android.ndk_path = /home/runner/android-sdk/ndk/25.1.8937393

# RECOMMENDED: Build for both modern and older 64-bit/32-bit devices
android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1

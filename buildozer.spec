[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise

source.dir = .
source.include_exts = py,kv,png,jpg,json

version = 1.0.0

requirements = python3,kivy==2.3.1,pillow

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# --- ANDROID CONFIG ---
android.api = 33
android.minapi = 21
android.sdk_api = 33
android.build_tools_version = 33.0.2

# Force Buildozer to use the SDK/NDK installed in GitHub Actions
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.1.8937393

# REMOVE THIS (it breaks the build)
# android.ndk = 25b

android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1

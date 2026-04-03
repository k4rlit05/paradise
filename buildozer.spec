[app]
title = Paradise
package.name = paradise
package.domain = org.paradise

# IMPORTANT: your app is inside /paradise folder
source.dir = paradise

# Include all needed files
source.include_exts = py,png,jpg,kv,atlas,json
source.include_patterns = paradise/*

version = 1.0.0

orientation = portrait
fullscreen = 0

# CLEAN requirements (very important)
requirements = python3,kivy==2.3.1,pillow,requests,urllib3

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# Android config
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a

# Use default SDK/NDK from buildozer (do NOT set paths)
android.accept_sdk_license = True
android.enable_androidx = True

# Bootstrap (default but we make it explicit)
p4a.bootstrap = sdl2

[buildozer]
log_level = 1
warn_on_root = 1

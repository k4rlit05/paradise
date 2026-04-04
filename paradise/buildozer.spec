[app]
title = Paradise
package.name = paradise
package.domain = org.paradise

# Your real code lives inside the inner paradise folder
source.dir = .

# Include Python and asset files
source.include_exts = py,png,jpg,kv,atlas,json

# Include all modules inside the inner paradise folder
source.include_patterns = paradise/*.py, paradise/ui/*.py, paradise/engine/*.py, paradise/backend/*.py

# App icon
icon.filename = assets/icon.png

version = 1.0.0
orientation = portrait
fullscreen = 0

# Python dependencies
requirements = python3, kivy==2.3.1, pillow, requests, urllib3, certifi, idna, charset-normalizer, openssl

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# ---------------------------------------------------------
# ANDROID BUILD SETTINGS (CLEAN + CORRECT)
# ---------------------------------------------------------
android.api = 34
android.compile_sdk = 34
android.sdk = 34
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.enable_androidx = True

# Required for Kivy 2.3.x
android.gradle_dependencies = androidx.appcompat:appcompat:1.6.1, androidx.core:core-ktx:1.12.0

# Kivy bootstrap
p4a.bootstrap = sdl2

# ---------------------------------------------------------
# IMPORTANT: FORCE BUILD TO IGNORE SYSTEM SDK/NDK
# These MUST stay commented exactly like this
# ---------------------------------------------------------
#android.sdk_path =
#android.ndk_path =
#android.ndk_api =

[buildozer]
log_level = 1
warn_on_root = 1
use_cache = False

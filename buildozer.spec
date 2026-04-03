[app]
title = Paradise
package.name = paradise
package.domain = org.paradise

# Omdat je code in de map 'paradise' staat:
source.dir = paradise
source.include_exts = py,png,jpg,kv,atlas,toml
source.include_patterns = backend/*, engine/*, ui/*

version = 1.0.0
orientation = portrait
fullscreen = 0

# Essentiële bibliotheken voor Kivy + Netwerk
requirements = python3, kivy==2.3.0, pillow, openssl, requests, urllib3, certifi, chardet, libffi, hostpython3, toml

android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Stabiele instellingen voor Android 13/14 ondersteuning
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.accept_sdk_license = True

# We laten buildozer zelf de gradle-versie bepalen voor meer stabiliteit
android.use_setup_py = False

[buildozer]
log_level = 2
warn_on_root = 1

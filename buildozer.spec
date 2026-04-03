[app]
title = Paradise
package.name = paradise
package.domain = org.paradise

# Omdat main.py en de .spec in de 'paradise' map staan:
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,toml
# Zorg dat alle submappen worden meegenomen
source.include_patterns = backend/*, engine/*, ui/*

version = 1.0.0
orientation = portrait
fullscreen = 0

# Belangrijk voor je AI en trading functies:
requirements = python3, kivy==2.3.0, pillow, openssl, requests, urllib3, certifi, chardet, libffi, hostpython3, toml

android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1

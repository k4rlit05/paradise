[app]
title = Paradise
package.name = paradise
package.domain = org.paradise

# Omdat de .spec IN de paradise map staat bij de main.py:
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,toml

# Vertel Buildozer specifiek welke mappen hij moet inpakken:
source.include_patterns = backend/*, engine/*, ui/*

version = 1.0.0
orientation = portrait
fullscreen = 0

# Belangrijk voor je AI-trading en UI:
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

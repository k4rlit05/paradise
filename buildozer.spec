[app]
title = Paradise
package.name = paradise
package.domain = org.paradise
source.dir = paradise
source.include_exts = py,png,jpg,kv,atlas,toml
source.include_patterns = backend/*, engine/*, ui/*, __init__.py
version = 1.0.0
orientation = portrait
fullscreen = 0
requirements = python3, kivy==2.3.0, pillow, openssl, requests, urllib3, certifi, chardet, libffi, hostpython3, toml
android.permissions = INTERNET, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.accept_sdk_license = True
android.enable_androidx = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1

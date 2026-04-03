[app]
# (Algemene informatie)
title = Paradise
package.name = paradise
package.domain = org.paradise

# Omdat je main.py en code in de map 'paradise' staan:
source.dir = paradise
source.include_exts = py,png,jpg,kv,atlas,toml

# Vertel Buildozer om alle submappen en de __init__.py bestanden mee te nemen
source.include_patterns = backend/*, engine/*, ui/*, __init__.py

version = 1.0.0
orientation = portrait
fullscreen = 0

# Essentiële bibliotheken voor Kivy, Netwerk en AI. 
# hostpython3 is verplicht voor cross-compiling op GitHub Actions.
requirements = python3, kivy==2.3.0, pillow, openssl, requests, urllib3, certifi, chardet, libffi, hostpython3, toml

# Rechten voor internettoegang (nodig voor je trading/AI functies)
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Stabiele Android API & NDK instellingen voor Kivy 2.3.0
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.accept_sdk_license = True
android.enable_androidx = True

# Gebruik de master branch van python-for-android voor de nieuwste Gradle fixes
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1

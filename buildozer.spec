[app]
# (Algemene informatie)
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

# Essentiële bibliotheken voor Kivy, Netwerk en AI (toml toegevoegd)
# hostpython3 is verplicht voor cross-compiling op GitHub
requirements = python3, kivy==2.3.0, pillow, openssl, requests, urllib3, certifi, chardet, libffi, hostpython3, toml

# Rechten voor internettoegang
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Stabiele Android API & NDK instellingen voor Kivy 2.3.0
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21
android.archs = arm64-v8a
android.accept_sdk_license = True
android.enable_androidx = True

# Gebruik de nieuwste fixes van python-for-android (lost gradle-fouten op)
p4a.branch = master

# We laten buildozer zelf de gradle-versie bepalen voor meer stabiliteit met Java 17
# (Verwijder handmatige gradle_dependencies regels als die er nog stonden)

[buildozer]
log_level = 2
warn_on_root = 1

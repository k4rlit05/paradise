[app]
# (Algemene informatie)
title = Paradise
package.name = paradise
package.domain = org.paradise

# Omdat je code in de map 'paradise' staat:
source.dir = paradise
source.include_exts = py,png,jpg,kv,atlas,toml
# Zorg dat alle submappen in 'paradise' worden meegenomen
source.include_patterns = backend/*, engine/*, ui/*

version = 1.0.0
orientation = portrait
fullscreen = 0

# TOEGEVOEGD: 'toml' en hulp-libs voor 'requests' (certifi, chardet)
requirements = python3, kivy==2.3.0, pillow, openssl, requests, urllib3, certifi, chardet, libffi, hostpython3, toml

# Rechten voor internettoegang
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# Stabiele API-instellingen
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# Beperk tot arm64 om de buildtijd in GitHub Actions te verkorten
android.archs = arm64-v8a

# Vereist voor automatische builds in GitHub Actions
android.accept_sdk_license = True

# Gradle instellingen
android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.2'
android.use_setup_py = False

[buildozer]
log_level = 2
warn_on_root = 1

[app]
# (De algemene info)
title = Paradise
package.name = paradise
package.domain = org.paradise
source.dir = paradise
version = 1.0.0
orientation = portrait
fullscreen = 0

# TOEGEVOEGD: certifi en chardet zijn nodig voor 'requests' op Android
# VERWIJDERD: dubbele hostpython3 (al inbegrepen bij p4a meestal)
requirements = python3, kivy==2.3.0, pillow, openssl, requests, urllib3, certifi, chardet, libffi, hostpython3

# TOEGEVOEGD: ACCESS_NETWORK_STATE helpt bij stabiele internetverbindingen
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# GEWIJZIGD: API 33 is momenteel de stabiele standaard voor Kivy/Buildozer
android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# GEWIJZIGD: Alleen arm64-v8a om de buildtijd in GitHub Actions te halveren en crashes te voorkomen
android.archs = arm64-v8a

# BELANGRIJK: Zorg dat deze op True staat voor automatische builds
android.accept_sdk_license = True

# Optimalisatie voor Gradle
android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.2'
android.use_setup_py = False

[buildozer]
log_level = 2
warn_on_root = 1

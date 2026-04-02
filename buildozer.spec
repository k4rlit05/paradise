[app]
# ... (title, package name, etc.)

# (list) Application requirements
# Added 'libffi' and 'openssl' which are needed for 'requests' to work on Android
requirements = python3,kivy==2.3.0,pillow,openssl,requests,urllib3,libffi,hostpython3

# (list) Permissions
android.permissions = INTERNET

# --- ANDROID SETTINGS ---
# Use these exact versions for maximum compatibility
android.api = 31
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# Modern phone architectures
android.archs = arm64-v8a, armeabi-v7a

# CRITICAL: Forces the build to bypass the license check crash
android.accept_sdk_license = True

# Standardizes the build environment to prevent "Bad Gateway" during Gradle sync
android.gradle_dependencies = 'com.android.tools.build:gradle:7.4.2'

# (bool) use_setup_py = False (Usually safer for modern Kivy)
android.use_setup_py = False

[buildozer]
log_level = 2
warn_on_root = 1

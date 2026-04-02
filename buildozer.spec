[app]
# App metadata
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise
version = 1.0.0

# Source files
source.dir = .
source.include_exts = py,kv,png,jpg,json

# Python and Kivy requirements
requirements = python3,kivy==2.3.1,pillow,requests,urllib3,cython<3

# UI configuration
orientation = portrait
fullscreen = 0

# Permissions
android.permissions = INTERNET

# --- ANDROID CONFIG ---
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.sdk_api = 33

# Build tools
android.build_tools_version = 33.0.2

# SDK/NDK paths (leave empty for auto-download)
android.sdk_path =
android.ndk_path =

# Gradle & AndroidX
android.gradle_dependencies = com.android.tools.build:gradle:7.4.2
android.use_androidx = True
android.accept_sdk_license = True

# Architectures to build
android.archs = arm64-v8a

[buildozer]
# Log verbosity (2 = normal)
log_level = 1
warn_on_root = 1
force_build = 0  # Only rebuild if necessary

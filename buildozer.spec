[app]
title = Paradise Trading App
package.name = paradisetrading
package.domain = org.paradise

source.dir = .
source.include_exts = py,kv,png,jpg,json

version = 1.0.0

requirements = python3,kivy==2.3.1,pillow

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# --- ANDROID CONFIG ---
android.api = 33
android.minapi = 21
android.ndk_api = 21
android.sdk_api = 33

# This MUST match your GitHub Actions workflow
android.build_tools_version = 33.0.2

# Leave these empty so Buildozer uses the GitHub Actions environment
android.sdk_path =
android.ndk_path =

# Force modern Gradle build system
android.gradle_dependencies = com.android.tools.build:gradle:7.0.2
android.use_androidx = True
android.enable_legacy_aapt = False

android.allow_backup = True


[buildozer]
log_level = 2
warn_on_root = 1

# Accept SDK licenses automatically
android.accept_sdk_license = True

# ❗ IMPORTANT: DO NOT SET "path = ..."
# Buildozer will use the PATH from GitHub Actions correctly.

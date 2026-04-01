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
android.build_tools_version = 33.0.2

# IMPORTANT: Leave these EMPTY so Buildozer uses the GitHub Actions environment
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

[app]

# (str) Title of your application
title = Solo Leveling System

# (str) Package name
package.name = sololevelingsystem

# (str) Package domain
package.domain = org.abakria46

# (str) Source code
source.dir = .

# (str) Main file
source.main = app_main.py

# (list) Source extensions
source.include_exts = py,png,jpg,json,kv,atlas

# (str) Version
version = 1.0

# (list) Requirements
requirements = python3,kivy

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (str) Icon
icon.filename = icon.png

# (list) Permissions
android.permissions = INTERNET

# Android API
android.api = 35

# Minimum Android API
android.minapi = 24

# Android NDK
android.ndk = 25b

# Android architecture
android.archs = arm64-v8a, armeabi-v7a
# Android bootstrap
p4a.bootstrap = sdl2

# Log level
log_level = 2

# Copy libraries
android.copy_libs = 1

# Use AndroidX
android.enable_androidx = True

# Presplash (اختياري)
# presplash.filename = presplash.png

# Splash (اختياري)
# android.presplash_color = #111111

# الشاشة تبقى مضاءة
android.wakelock = False

# السماح بالنسخ الاحتياطي
android.allow_backup = True

# عدم إنشاء نسخة AAB
android.release_artifact = apk

# إضافة ملفات البيانات
source.exclude_dirs = .git,.github,__pycache__,bin,.buildozer
source.exclude_patterns = *.pyc,*.pyo

[buildozer]

log_level = 2

warn_on_root = 1
# (str) Android entry point
android.entrypoint = org.kivy.android.PythonActivity

# (bool) Enable fullscreen on Android
android.fullscreen = 0

# (str) Application theme
android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) Files to include
include_patterns = assets/*

# (list) Files to exclude
exclude_patterns = *.bak,*.tmp

# (str) Build mode
build_dir = .buildozer

# نهاية الملف

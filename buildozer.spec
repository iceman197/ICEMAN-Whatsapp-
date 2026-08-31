[app]
title = ICEMAN Math Solver
package.name = icemanmath
package.domain = org.iceman
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 35
android.minapi = 23
android.ndk = 27c
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

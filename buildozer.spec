[app]
title = YuMusic
package.name = yumusic
package.domain = org.waiyan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# 'customtkinter' will crash the build. Use 'kivy' instead.
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True
android.sdk_build_tools_version = 34.0.0
android.ndk_api = 23

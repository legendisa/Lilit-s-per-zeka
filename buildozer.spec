[app]
title = Lilit
package.name = lilit
package.domain = org.isa
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
# A7 32-bit olduğu için burası kritik:
android.archs = armeabi-v7a
android.allow_backup = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1

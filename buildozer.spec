[app]
title = TroyZx
package.name = troyzx
package.domain = org.troyzx
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

# İkonları tamamen sildik, sistem varsayılanını kullanacak
android.api = 31
android.arch = armeabi-v7a
android.permissions = SYSTEM_ALERT_WINDOW

[buildozer]
log_level = 2
warn_on_root = 1

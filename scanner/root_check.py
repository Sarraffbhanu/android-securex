import os

def check_root():
    return os.path.exists("/system/xbin/su") or os.path.exists("/system/bin/su")

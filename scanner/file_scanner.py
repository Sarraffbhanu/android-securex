import os

def scan_files():
    suspicious_keywords = ["keylogger", "hack", "spy"]
    results = []
    for root, _, files in os.walk("/sdcard"):
        for f in files:
            if any(k in f.lower() for k in suspicious_keywords):
                results.append(os.path.join(root, f))
    return results

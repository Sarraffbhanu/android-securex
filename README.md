# Android SecureX 🔒

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-Android%2FTermux-green)
![License](https://img.shields.io/badge/license-MIT-orange)

Advanced Android security analysis toolkit for vulnerability detection and system hardening

## Features 🛡️
- **Root/Jailbreak Detection**  
  Identifies compromised device status
- **Permission Auditor**  
  Scans for dangerous app permissions (INTERNET, CAMERA, etc)
- **File System Sentinel**  
  Hunts suspicious files in critical directories:
  ```/system/bin, /system/xbin, /sdcard/Download```
- **App Vulnerability Check**  
  Detects outdated/unmaintained applications
- **CVE Database Integration**  
  Cross-references found vulnerabilities with public CVE database
- **Automated Reporting**  
  Generates timestamped scan reports in `logs/` directory

## Installation 📦

### Prerequisites
- Termux (Android) or Linux environment
- Python 3.8+
- Active internet connection

```bash
git clone https://github.com/sarraffbhanu/android-securex.git
cd android-securex
pip install -r requirements.txt


## usage 
python main.py

from scanner import root_check, permissions, file_scanner, app_checker, cve_checker
from utils.reporter import generate_report
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import os, platform

console = Console()

def banner():
    console.print(Panel.fit("[bold red]ANDROID SECUREX[/bold red]\n[green]Supercharged Android Threat Analyzer[/green]", border_style="blue"))

def main():
    banner()
    device_info = {
        "Platform": platform.system(),
        "Release": platform.release()
    }

    console.print(f"[bold yellow]Scanning Device:[/bold yellow] {device_info['Platform']} {device_info['Release']}")

    results = {
        "Root": root_check.check_root(),
        "Dangerous Permissions": permissions.scan_permissions(),
        "Suspicious Files": file_scanner.scan_files(),
        "Outdated Apps": app_checker.check_apps(),
        "CVEs": cve_checker.check_cves(platform.release())
    }

    generate_report(results)

if __name__ == "__main__":
    main()

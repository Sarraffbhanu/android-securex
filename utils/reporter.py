from datetime import datetime

def generate_report(results):
    filename = f"logs/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        for key, val in results.items():
            f.write(f"{key}:\n{val}\n\n")
    print(f"\n[+] Report saved to {filename}")

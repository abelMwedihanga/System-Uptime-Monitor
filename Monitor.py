import urllib.request
import datetime

print("=== System Uptime Monitor ===")
print("By Abel Mwedihanga | NAMPOL ICT - System Monitoring\n")

# Systems to check - you can change these to NAMPOL systems later
systems = {
    "Google": "https://www.google.com",
    "GitHub": "https://www.github.com",
    "NAMPOL Website": "https://www.nampol.gov.na",
}

log_file = "uptime_log.txt"

for name, url in systems.items():
    try:
        # Try to connect, timeout after 5 seconds
        urllib.request.urlopen(url, timeout=5)
        status = "UP ✅"
    except Exception as e:
        status = "DOWN ❌"

    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result = f"[{time_now}] {name} ({url}) - {status}"
    print(result)

    # Save to log file
    with open(log_file, "a") as f:
        f.write(result + "\n")

print(f"\nDone! Results saved to {log_file}")
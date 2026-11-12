# System Uptime Monitor

Checks if critical systems are UP or DOWN and logs results with timestamps.

Built by Abel Mwedihanga | NAMPOL ICT - System Monitoring

## What it does
- Checks Google, GitHub, and NAMPOL Website
- Shows UP ✅ / DOWN ❌ status
- Saves every check to uptime_log.txt with date & time
- 5-second timeout so it never hangs

## How to run
python Monitor.py

## Example Output
[2026-11-12 08:16:24] Google - UP ✅
[2026-11-12 08:16:30] NAMPOL Website - DOWN ❌

## Use at work
Change the URLs in Monitor.py to your internal NAMPOL systems to monitor them.
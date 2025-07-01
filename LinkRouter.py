import sys
import subprocess

url = sys.argv[1] if len(sys.argv) > 1 else ""

# Paths to browsers (change these if yours are different)
brave = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Choose browser
if "instagram.com" in url:
    subprocess.Popen([brave, url])
else:
    subprocess.Popen([chrome, url])
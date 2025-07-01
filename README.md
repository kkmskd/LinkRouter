# LinkRouter
Intelligently routes each link to your browser of choice - open Instagram in Firefox, TikTok in Chrome, automatically.


# URL Browser Router

A simple Python script that opens a given URL in a specific browser based on your preference.

---

## Description

This script accepts a URL as a command-line argument and launches it in one of two browsers depending on the URL content.

- URLs containing **`instagram.com`** will open in **Browser A**.
- All other URLs will open in **Browser B**.

This allows you to customize which browser handles certain websites automatically.

---

## Requirements

- Python 3.x installed on your system.
- The target browsers must be installed and their executable paths updated in the script.

---

## Setup

1. Edit the script to set the paths to your browsers.  
   Replace the paths for `browser_a_path` and `browser_b_path` with the correct locations on your system:

   ```python
   browser_a_path = r"C:\Path\To\BrowserA\browser.exe"
   browser_b_path = r"C:\Path\To\BrowserB\browser.exe"

2. Before running the script the file needs to be convert to .exe first by open cmd in the file path and enter
```
pip install pyinstaller
pyinstaller --onefile --noconsole smart_browser.py

```

4. Run .reg file and restart computer.


5. Change the default apps to LinkRouter

@echo off
rem Re-render og-image.jpg (the WhatsApp/X link preview) from tools/og.html.
cd /d "%~dp0.."
"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1200,630 --virtual-time-budget=4000 --screenshot="%TEMP%\bd-og.png" "file:///%CD:\=/%/tools/og.html"
python -c "from PIL import Image; Image.open(r'%TEMP%\bd-og.png').convert('RGB').save('og-image.jpg', quality=88, optimize=True, progressive=True)"

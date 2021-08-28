# Translate (in progressing)
Translates messages on the left bottom croner to english.  
The target area is configured to the Rust in game chat but can be placed everywhere. To change the target area play with the h(height), w(width), x and y coordinates.

## Installation
- Install tesseract from this site: https://github.com/UB-Mannheim/tesseract/wiki  
and set the path in translater.py line 10 to your tesseract.exe installation  
Be sure to install all the languages you want: https://ocrmypdf.readthedocs.io/en/latest/languages.html

- pip install numpy  
- pip install opencv-python
- pip install pyautogui
- pip install pytesseract  
- pip install -U deep-translator

## Problems
- text recognition needs high contrast to work

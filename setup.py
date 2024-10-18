import pyautogui
import time
from dotenv import load_dotenv
import os
import webbrowser

#AutoHotKeyをsuspendする
pyautogui.hotkey('ctrl', 'alt', 's')

# winボタンプッシュ
pyautogui.press('win')
time.sleep(1)
pyautogui.write('notion')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('win')
time.sleep(1)
pyautogui.write('duck')
pyautogui.press('enter')


# outlookを表示
webbrowser.open("https://outlook.office.com/mail/")
webbrowser.open("https://b.hatena.ne.jp/hotentry/it")
webbrowser.open("https://www.nikkei.com/")
webbrowser.open("https://feedly.com/i/my")
webbrowser.open("https://copilot.cloud.microsoft/")

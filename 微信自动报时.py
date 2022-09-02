import datetime
import time

import pyautogui
import pyperclip


def main():
    while True:
        date = datetime.datetime.now()
        m = date.minute
        date = date.hour
        if m or not (date in [15, 16, 17]):
            time.sleep(1)
            continue
        r = pyautogui.locateOnScreen('bin/start.png')
        x, y = r[0], r[1]
        pyautogui.moveTo(x + 100, y + 10)
        pyautogui.click()
        time.sleep(2)
        pyperclip.copy('猿人')
        with pyautogui.hold('ctrl'):
            pyautogui.press('v')
        time.sleep(2)
        pyautogui.move(0, 100)
        pyautogui.click()
        pyperclip.copy(f'现在是北京时间 {date}点整')
        with pyautogui.hold('ctrl'):
            pyautogui.press('v')
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(60)


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)
            time.sleep(1)
            continue

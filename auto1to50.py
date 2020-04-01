import pyautogui

for number in range(1, 5):
    pyautogui.click('assets' + str(number) + '.png')

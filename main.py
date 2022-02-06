import pyautogui
import time
import keyboard
import random

def getColorDiff(colorArray):
    diffPoint = []
    for i in colorArray:
        temp = []
        for j in colorArray:
            temp.append(abs(i[0] - j[0]) + abs(i[1] - j[1]) + abs(i[2] - j[2]))

        diffPoint.append(temp[0]+ temp[1]+ temp[2]+temp[3])
    return diffPoint

mousePosition4 = [
    (155, 456),
    (341, 456),
    (155, 620),
    (341, 620)
    ]


for i in range(4):
    time.sleep(0.5)
    currentColor4 = []
    for i in mousePosition4:
        currentColor4.append(pyautogui.pixel(i[0], i[1]))

    diffpoint = getColorDiff(currentColor4)
    print(diffpoint)
    index = diffpoint.index(max(diffpoint))
    print(index)
    pyautogui.click(mousePosition4[index][0], mousePosition4[index][1])
    


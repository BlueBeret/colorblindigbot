import pyautogui
import time
import random
from datetime import datetime
from pymouse import PyMouse
import keyboard

time.sleep(1)

mouse = PyMouse()
def getColorDiff(colorArray):
    logColor(colorArray)
    diffPoint = []
    for i in colorArray:
        temp = []
        for j in colorArray:
            temp.append(abs(i[0] - j[0]) + abs(i[1] - j[1]) + abs(i[2] - j[2]))

        diffPoint.append(temp[0]+ temp[1]+ temp[2]+temp[3])
    logDiff(diffPoint)
    return diffPoint

def logColor(colorArray):
    with open("logColor.txt", "a") as f:
        f.write(str(colorArray))
        f.write("\n")

def logDiff(diffPoint):
    with open("logDiff.txt", "a") as f:
        f.write(str(diffPoint))
        f.write("\n")



mousePosition4 = [
    (155, 456),
    (341, 456),
    (155, 620),
    (341, 620)
    ]

mousePosition6 = [
    (119,407),
    (235,418),
    (356,416),
    (120,535),
    (235,535),
    (361,535),
    (119,591),
    (235,591),
    (356,591),

]

mousePosition16= [
    (111,394),
    (196,394),
    (277,394),
    (365,394),
    (111,482),
    (196,482),
    (277,482),
    (365,482),
    (111,569),
    (196,569),
    (277,569),
    (365,569),
    (111,615),
    (196,615),
    (277,615),
    (365,615),
]

mousePosition25= [
    (83,369),
    (161,369),
    (236,369),
    (319,369),
    (394,369),
    (83,450),
    (161,450),
    (236,450),
    (319,450),
    (394,450),
    (83,525),
    (161,525),
    (236,525),
    (319,525),
    (394,525),
    (83,600),
    (161,600),
    (236,600),
    (319,600),
    (394,600),
    (83,643),
    (161,643),
    (236,643),
    (319,643),
    (394,643),
]

def click(x,y):
    mousex = pyautogui.position()[0]
    if mousex > 1000:
        exit()
    # mouse.click(725,233)
    # mouse.press(x,y)
    # time.sleep(random.choice(range(1,5)) * 0.1)
    # mouse.release(x,y)
    mouse.click(x,y)
    # pyautogui.click(x,y)

for j in range(4):
    print(4)
    time.sleep(0.5)
    currentColor4 = []
    im = pyautogui.screenshot()
    for i in mousePosition4:
        currentColor4.append(im.getpixel(i))

    
    diffpoint = getColorDiff(currentColor4)

    index = diffpoint.index(max(diffpoint))
    click(mousePosition4[index][0], mousePosition4[index][1])



for _ in range(15):
    print(6)
    time.sleep(1)
    currentColor6 = []
    im = pyautogui.screenshot()
    time.sleep(0.5)
    for i in mousePosition6:
        currentColor6.append(im.getpixel(i))

    
    diffpoint = getColorDiff(currentColor6)

    index = diffpoint.index(max(diffpoint))
    click(mousePosition6[index][0], mousePosition6[index][1])

for _ in range(16):
    print(16)
    time.sleep(1.6)
    currentColor16 = []
    im = pyautogui.screenshot()
    time.sleep(0.5)
    for i in mousePosition16:
        currentColor16.append(im.getpixel(i))

    
    diffpoint = getColorDiff(currentColor16)

    index = diffpoint.index(max(diffpoint))
    click(mousePosition16[index][0], mousePosition16[index][1])

for _ in range(15):
    print(25)
    time.sleep(1.5)
    currentColor25 = []
    im = pyautogui.screenshot()
    time.sleep(0.5)
    for i in mousePosition25:
        currentColor25.append(im.getpixel(i))

    diffpoint = getColorDiff(currentColor25)

    index = diffpoint.index(max(diffpoint))
    click(mousePosition25[index][0], mousePosition25[index][1])
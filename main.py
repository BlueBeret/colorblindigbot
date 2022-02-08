from cmath import sqrt
import pyautogui
import time
import random
from datetime import datetime
from pymouse import PyMouse
import keyboard

time.sleep(1)

mouse = PyMouse()

DELAY = [0.5, 0.8,]

def deltaRgb(rgb1, rgb2):
    rmean = (rgb1[0] + rgb2[0]) // 2
    r = rgb1[0] - rgb2[0]
    g = rgb1[1] - rgb2[1]
    b = rgb1[2] - rgb2[2]

    temp = (((512+rmean)*r*r)>>8) + 4*g*g + (((767-rmean)*b*b)>>8)
    assert(temp >= 0)
    return temp

def getColorDiff(colorArray, advance=False):
    logColor(colorArray)
    diffPoint = []
    for i in colorArray:
        temp = 0
        for j in colorArray:
            # temp.append(abs(i[0] - j[0]) + abs(i[1] - j[1]) + abs(i[2] - j[2]))
            # temp.append((i[0] - j[0])**2 + (i[1] - j[1])**2 + (i[2] - j[2])**2)
            
            if advance:
                temp += deltaRgb(i,j)
            else:
                temp += (i[0] - j[0])**2 + (i[1] - j[1])**2 + (i[2] - j[2])**2

        diffPoint.append(temp)
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
    mouse.click(x,y)

for j in range(4):
    print(4)
    time.sleep(DELAY[0])
    currentColor4 = []
    im = pyautogui.screenshot()
    for i in mousePosition4:
        currentColor4.append(im.getpixel(i))

    
    diffpoint = getColorDiff(currentColor4)


    index = diffpoint.index(max(diffpoint))
    click(mousePosition4[index][0], mousePosition4[index][1])



for _ in range(15):
    print(9)
    time.sleep(DELAY[1])
    currentColor6 = []
    im = pyautogui.screenshot()
    time.sleep(0.5)
    for i in mousePosition6:
        currentColor6.append(im.getpixel(i))

    
    diffpoint = getColorDiff(currentColor6)

    index = diffpoint.index(max(diffpoint))
    click(mousePosition6[index][0], mousePosition6[index][1])

for _ in range(15):
    print(16)
    time.sleep(0.8)
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
    time.sleep(1)
    currentColor25 = []
    im = pyautogui.screenshot()
    time.sleep(0.5)
    for i in mousePosition25:
        currentColor25.append(im.getpixel(i))

    diffpoint = getColorDiff(currentColor25, True)

    # reverse = False
    # sortedDiff = sorted(diffpoint, reverse=False)
    # choseddiff = []
    # for i in range(len(sortedDiff)):
    #     tempj = sortedDiff.count(sortedDiff[i])
    #     if tempj > 1:
    #         continue
    #     else:
    #         choseddiff.append(sortedDiff[i])
    # index = diffpoint.index(random.choice(choseddiff))
    # index = diffpoint.index(max(choseddiff))
    # logDiff(index)
    # click(mousePosition25[index][0], mousePosition25[index][1])
    index = diffpoint.index(max(diffpoint))
    
    logDiff(index)
    click(mousePosition25[index][0], mousePosition25[index][1])
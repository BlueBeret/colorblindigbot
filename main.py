import pyautogui
import time
import random
from datetime import datetime
from pymouse import PyMouse

mouse = PyMouse()
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

def click(x,y):
    # mouse.click(725,233)
    print("clicking")
    # mouse.press(x,y)
    # time.sleep(random.choice(range(1,5)) * 0.1)
    # mouse.release(x,y)
    mouse.click(x,y)
    # pyautogui.click(x,y)

for j in range(4):
    time.sleep(0.5)
    currentColor4 = []
    starttime = datetime.now()
    for i in mousePosition4:
        currentColor4.append(pyautogui.pixel(i[0], i[1]))

    
    diffpoint = getColorDiff(currentColor4)

    index = diffpoint.index(max(diffpoint))
    print(f"{len(currentColor4)} {[(i[0],i[1],i[2]) for i in currentColor4]}")
    print(diffpoint)
    # print(index)

    # print(datetime.now() - starttime)
    # starttime = datetime.now()
    click(mousePosition4[index][0], mousePosition4[index][1])
    # print(f"time to click {datetime.now() - starttime}")



for _ in range(15):
    time.sleep(0.5)
    currentColor6 = []
    
    for i in mousePosition6:
        currentColor6.append(pyautogui.pixel(i[0], i[1]))

    
    diffpoint = getColorDiff(currentColor6)

    index = diffpoint.index(max(diffpoint))
    click(mousePosition6[index][0], mousePosition6[index][1])
    # print(f"{len(currentColor6)} {currentColor6}")
    # print(diffpoint)
    # print(index)
    # mouse.press(mousePosition6[index][0], mousePosition6[index][1])
    # time.sleep(1)
    # mouse.release(mousePosition6[index][0], mousePosition6[index][1])
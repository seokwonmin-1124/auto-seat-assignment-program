import random
import numpy as np

stdNum = 30

def createNewPlacement(stdNum, n): # n = 줄 몇개로 쪼갤지
    stdList = []
    stdNumList = []

    for i in range(stdNum):
        stdNumList.append(i+1)
    random.shuffle(stdNumList)

    for i in range((len(stdNumList) + n - 1) // n ):
        stdList.append(stdNumList[i * n:(i + 1) * n])
        
    return stdList
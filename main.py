import random
import numpy as np
import streamlit as st

stdNum = 30

def 풀어서적은코드(stdNum, n): # n = 줄 몇개로 쪼갤지
    stdList = []
    stdNumList = []

    for i in range(stdNum):
        stdNumList.append(i+1)
    random.shuffle(stdNumList)

    for i in range((len(stdNumList) + n - 1) // n ):
        stdList.append(stdNumList[i * n:(i + 1) * n])

    return stdList

st.write('### 교탁')
st.write(np.asarray(풀어서적은코드(stdNum, 5)))
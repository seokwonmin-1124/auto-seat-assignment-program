import random

def 네이밍뭐로하지(stdNum, n):
    stdList = [i+1 for i in range(stdNum-1)]
    random.shuffle(stdList)
    return [stdList[i * n:(i + 1) * n] for i in range((len(stdList) + n - 1) // n )]

print(네이밍뭐로하지(30, 5))

# def 풀어서적은코드(stdNum, n):
#     stdList = []
#     _stdList = []

#     for i in range(stdNum):
#         _stdList.append(i+1)
#     random.shuffle(_stdList)

#     for i in range((len(_stdList) + n - 1) // n ):
#         stdList.append(_stdList[i * n:(i + 1) * n])
#     return stdList

# print(풀어서적은코드(30, 5))
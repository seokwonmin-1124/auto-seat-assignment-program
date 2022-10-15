import random

def 네이밍뭐로하지(stdNum, n):
    stdList = [i+1 for i in range(stdNum-1)]
    random.shuffle(stdList)
    return [stdList[i * n:(i + 1) * n] for i in range((len(stdList) + n - 1) // n )]

print(네이밍뭐로하지(30, 5))
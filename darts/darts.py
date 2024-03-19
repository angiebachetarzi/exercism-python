import math

def score(x, y):
    dist = math.sqrt(x**2 + y**2)
    if dist > 10:
        return 0
    elif dist > 5:
        return 1
    elif dist > 1:
        return 5
    elif dist >= 0:
        return 10
    return -1
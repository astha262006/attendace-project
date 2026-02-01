import random

def kth_smallest(arr, k):
    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k <= len(lows):
        return kth_smallest(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return kth_smallest(highs, k - len(lows) - len(pivots))






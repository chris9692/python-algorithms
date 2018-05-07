def poly(x, a, b, c):
    return a * x ** 2 + b * x + c

def polySorted(arr, a, b, c):
    if a == 0 or len(arr) <= 1:
        return [poly(x1, a, b, c) for x1 in arr]
    
    xLen = len(arr)
    y = list(arr).copy()
    x0 = -1.0 * b / (2 * a)
    minDistance = abs(arr[0] - x0)
    index0 = 0
    for i, n in enumerate(arr):
        if abs(x0 - n) < minDistance:
            index0 = i
            minDistance = abs(x0 - n)
    
    if a > 0:
        start = 0
        step = 1
    else:
        start = -1
        step = -1
    
    i = 1
    j = 1
    y[start] = poly(arr[index0], a, b, c)
    start += step
    while index0 - i >= 0 and index0 + j < xLen:
        if abs(x0 - index0 + i) >= abs(x0 - index0 - j):
            y[start] = poly(arr[index0 + j], a, b, c)
            start += step
            j += 1
        else:
            y[start] = poly(arr[index0 - i], a, b, c)
            start += step
            i += 1
            
    while index0 - i >= 0:
        y[start] = poly(arr[index0 - i], a, b, c)
        start += step
        i += 1
            
    while index0 + j < xLen:
        y[start] = poly(arr[index0 + j], a, b, c)
        start += step
        j += 1
    
    return y

polySorted(range(9), 3, -8, 5)

def maxSum(a):
    rSum = a[0] if len(a) > 0 else 0
    mSum = a[0] if len(a) > 0 else 0
    for n in a:
        rSum += n
        mSum = max(rSum, mSum)
    return mSum

def maxSubArrySum(a):
    if len(a) <= 1:
        return sum(a)
    
    if len(a) == 2:
        return max(max(a), sum(a))
    
    c = len(a) // 2
    mSum = a[c]
    maxLSum = maxSum(a[c-1:-1:-1])
    maxRSum = maxSum(a[c + 1:])
    
    mSum += max(maxLSum, maxRSum, maxLSum + maxRSum)
    
    return max(maxSubArrySum(a[:c-1]), maxSubArrySum(a[c+1:]), mSum)

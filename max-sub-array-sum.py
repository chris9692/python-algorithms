# linear with dynamic programming

def maxSubArrySum2(a):
    if len(a) <= 1:
        return sum(a)
    
    maxRSum = a[0]
    thisRSum = a[0]
    
    for i in range(1, len(a)):
        maxRSum = max([a[i], a[i] + thisRSum, maxRSum])
        thisRSum = max([a[i], a[i] + thisRSum])
        
    return maxRSum

# devide and conquer  nlog(n)

def maxSum(a):
    rSum = a[0] if len(a) > 0 else 0
    mSum = a[0] if len(a) > 0 else 0
    for n in a:
        rSum += n
        mSum = max(rSum, mSum)
    return mSum

def maxSubArrySum2(a):
    if len(a) <= 1:
        return sum(a)
    
    if len(a) == 2:
        return max(max(a), sum(a))
    
    c = len(a) // 2
    mSum = a[c]
    maxLSum = maxSum(a[c-1:-1:-1])
    maxRSum = maxSum(a[c + 1:])
    
    mSum += max(maxLSum, maxRSum, maxLSum + maxRSum)
    
    return max(maxSubArrySum2(a[:c-1]), maxSubArrySum2(a[c+1:]), mSum)

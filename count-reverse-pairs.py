import numpy as np

def getInvCount_BF(a):
    """
    This is the brute force method that takes O(n^2) time
    and no extra space
    """
 
    count = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if (a[i] > a[j]):
                count += 1
 
    return count
 
if __name__ == '__main__':
    assert(getInvCount_BF([1, 20, 6, 4, 5]) == 5)

def merge(al, ar):
    count = 0
    i = 0
    j = 0
    a = []
    while i < len(al) and j <= len(ar):
        if j < len(ar) and al[i] > ar[j]:
            a.append(ar[j])
            j += 1 
        else:
            a.append(al[i])
            count += j 
            i += 1
    #print(count, a, al, ar)
    return count, a
        
def getInvCount_MS(a):
    """
    This is the brute force method that takes O(n^2) time
    and no extra space
    """
    count = 0
    
    if len(a) < 2:
        return 0, a
    
    if len(a) == 2:
        count = 1 if a[0] > a[1] else 0
        a.sort()
        return count, a
 
    m = len(a) // 2
    
    nl, al = getInvCount_MS(a[:m])
    nr, ar = getInvCount_MS(a[m:])
    nm, am = merge(al, ar)
    
    return nl + nr + nm, am

if __name__ == '__main__':
    print(getInvCount_MS([1, 20, 6, 4, 5]))

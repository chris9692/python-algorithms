

import numpy as np

def _palindrom(s, st, start, end):
    if st[start, end] != -1:
        return st[start, end]
    
    if s[start] == s[end] and _palindrom(s, st, start + 1, end - 1) > 0:
        st[start, end] = end - start + 1
    else:
        st[start, end] = 0
        
    return st[start, end]

def maxPalindromSubString(s):
    
    # initialize states and set base cases
    # for strings of len 1, 2, 3
    states = np.ones(len(s)) * -1 + np.eye(len(s)) * 2
    
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            states[i, i + 1] = 2
            
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            states[i, i + 2] = 3
            
    for i in range(len(s)-1):            
        for j in range(i+1, len(s)):
            if s[i] != s[j]:
                states[i, j] = 0
            else:
                _palindrom(s, states, i, j)
            
    return np.max(states)

if __name__ == '__main__':
    assert(maxPalindromSubString('qeyhgerthejxxxaabcbaaxxxje') == 17)

def maxPalindromSubString2(s):
    """
    The centers method
    """
    if len(s) == 0:
        return 0
    
    # initialize states and set base cases
    # for strings of len 1, 2, 3
    centers = {}
    
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            centers[(i, i + 1)] = 2
            
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            centers[(i, i + 2)] = 3

    if len(centers) == 0:
        return 1
    
    for c, l in centers.items():
        for i in range(1, len(s)):
            if c[0] - i < 0 or c[1] + i >= len(s):
                break
            if s[c[0] - i] == s[c[1] + i]:
                centers[c] += 2
        
    return max(centers.values())

if __name__ == '__main__':
    assert(maxPalindromSubString2('qaabcbaax') == 7)
    assert(maxPalindromSubString2('qeyejxxxaabcbaaxxxje') == 17)

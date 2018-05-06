
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
            
    print(np.max(states))

if __name__ == '__main__':
    maxPalindromSubString('qeyhgerthejxxxaabcbaaxxxje')

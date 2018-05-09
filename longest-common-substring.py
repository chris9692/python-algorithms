import numpy as np

def _commonSubString(states, x, y, px, py):
    if states[px, py] != -1:
        return states[px, py]
    
    if x[px] != y[py]:
        states[px, py] = 0
    elif px == 0 or py == 0:
        states[px, py] = 1
    else:
        states[px, py] = _commonSubString(states, x, y, px - 1, py - 1) + 1
    return states[px, py]

def longestCSS(x, y):
    states = np.array([-1] * len(x) * len(y)).reshape((len(x), len(y)))
    for i in range(len(x)):
        for j in range(len(y)):
            _commonSubString(states, x, y, i, j)
    return np.max(states)

if __name__ == '__main__':
    assert(longestCSS("GeeksforGeeks", "GeeksQuiz") == 5)
    assert(longestCSS("abcdxyz", "xyzabcd") == 4)
    assert(longestCSS("zxabcdezy", "yzabcdezx") == 6)

LCS(s1, s2, i, j):
    if(i == -1 || j == -1)
        return 0
    if(s1[i] == s2[j])
        return 1 + LCS(s1, s2, i-1, j-1)
    return max(LCS(s1, s2, i-1, j), LCS(s1, s2, i, j-1))

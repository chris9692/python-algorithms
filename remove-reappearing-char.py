def removeDupChar0(s):
    """
    deereererererereerer => der
    Brute Force, complexity = O(n^2)
    """
    asize = len(s)
    result = ''
    for i in range(asize):
        if s[i] not in s[i+1:]:
            result += s[i]
    return result

def removeDupChar1(s):
    """
    deereererererereerer => der
    regular expression, complexity O(n^2)
    """
    s1 = ''
    while s != s1:
        s1 = s
        s = re.sub(r'([a-z])(.*)\1{1,}', r'\1\2', s1)
    return s

def removeDupChar(s):
    """
    deereererererereerer => der
    hashtable, complexity O(n)
    """
    asize = len(s)
    hasht = {}
    result = ''
    for c in s:
        if c not in hasht:
            hasht[c] = 1
            result += c
        else:
            continue
    return result
    
assert(removeDupChar0('deereererererereerer') == 'der')
assert(removeDupChar0('deereererererereerer') == removeDupChar1('deereererererereerer'))
assert(removeDupChar0('deereererererereerer') == removeDupChar('deereererererereerer'))

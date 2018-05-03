def balanced_string(s):
    
    # create a symbos dictionary like {'}':'{', ')': '(', ']':'['}
    # with closing brackets as keys, and opening brackets as values
    symbols = dict(zip('}])', '{[(')) 
    
    # create a stack to track opening brackets
    stack = []
    
    for c in s:
        if c in symbols.values():
            stack.append(c)
        elif c in symbols.keys():
            if len(stack) > 0 and stack.pop() == symbols[c]: continue
            return False
        else:
            #discard all other characters
            continue
            
    return len(stack) == 0

if __name__ == '__main__':
    assert(False == balanced_string('[]()(x)(sed(((x[x])))'))
    assert(True == balanced_string('[](x)()((x([x])))'))
    assert(False == balanced_string('[(,,,(,,[])]'))

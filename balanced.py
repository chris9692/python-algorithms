def balanced_string(s):
    symbols = {'}':'{', ')': '(', ']':'['}
    stack = []
    for c in s:
        if c in symbols.values():
            stack.append(c)
        elif c in symbols.keys():
            if len(stack) > 0 and stack.pop() == symbols[c]:
                continue
            else:
                return False
    return len(stack) == 0

if __name__ == '__main__':
    assert(False == balanced_string('[]()(x)(sed(((x[x])))'))
    assert(True == balanced_string('[](x)()((x([x])))'))
    assert(False == balanced_string('[(,,,(,,[])]'))

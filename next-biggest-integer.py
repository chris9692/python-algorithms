def greater_number(n: int) -> int:
    """
    give an integer number, find the next bigest number 
    formed by the same set of digits
    """
    if n < 10: 
        return n
    
    newstr = ''
    nstr = str(n)
    
    for i in range(len(nstr)-2, -1, -1):
        if nstr[i] < nstr[i+1]:
            newstr = nstr[:i]+nstr[-1]+(''.join(sorted(nstr[i:-1])))
            break
    return int(newstr) if len(newstr) > 0 else None

if __name__ == '__main__':
    assert(greater_number(218765) == 251678)
    assert(greater_number(1234) == 1243)
    assert(greater_number(4321) == None)
    assert(greater_number(534976) == 536479)

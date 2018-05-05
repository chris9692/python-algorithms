def any_sum(s, *args):
    """
    export all combinations of numbers, one from each
    set as given in args, that add up to s
    param s: the sum 
    param args: sets of unique integers
    """
    if len(args) < 2:
        return []
    
    if len(args) == 2:
        combinations = []
        lookup = {(s-n): n for n in args[0]}
        for n in args[1]:
            if lookup.get(n) != None:
                combinations.append([lookup[n], n])
    else:
        combinations = []
        for n in args[-1]:
            subsum = any_sum(s-n, *args[:-1])
            combinations.extend([(*x,n) for x in subsum if n not in x])
            
    return list(set(tuple(sorted(c)) for c in combinations))
        

if __name__ == '__main__':
    print(any_sum(0, range(10), range(-9,0), range(10)))

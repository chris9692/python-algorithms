
def two_sum(a, b):
    """
    export all combinations of number pairs, one from each
    set, that add up to 0
    param a: set of integers
    param b: set of integers
    """
    lookup = {(0-n): n for n in a}
    for n in b:
        if lookup.get(n) != None:
            print(lookup[n], n)

if __name__ == '__main__':
    two_sum(range(10), range(-9,0))


def two_sum2(a, b, s):
    """
    export all combinations of number pairs, one from each
    set, that add up to s
    param a: set of unique integers
    param b: set of unique integers
    param s: the sum 
    """
    lookup = {(s-n): n for n in a}
    for n in b:
        if lookup.get(n) != None:
            print(lookup[n], n)

if __name__ == '__main__':
    two_sum2(range(10), range(-9,0), 1)    

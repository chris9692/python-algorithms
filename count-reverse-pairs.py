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

def _merge(al, ar):
    count = 0
    i = 0
    j = 0
    temp = []
    while i < len(al) and j < len(ar):
        if al[i] > ar[j]:
            temp.append(ar[j])
            j += 1 
            if j == len(ar):
                # the right array was all processed
                # add anything remain in left
                while i < len(al):
                    temp.append(al[i])
                    count += j 
                    i += 1
        else:
            temp.append(al[i])
            count += j 
            i += 1
            if i == len(al): 
                # the left array was all processed
                # add anything remain in right
                while j < len(ar):
                    temp.append(ar[j])
                    j += 1 
    return count, temp
        
def _getInvCount_MS(a):
    if len(a) <= 2:
        x = a[0]
        a.sort
        return 1 if x != a[0] else 0, a
    
    m = len(a) // 2
    
    nl, al = _getInvCount_MS(a[:m])
    nr, ar = _getInvCount_MS(a[m:])
    nm, am = _merge(al, ar)
    
    return nl + nr + nm, am

def getInvCount_MS(a):
    c, x = _getInvCount_MS(a)
    return c

if __name__ == '__main__':
    assert(getInvCount_MS([1, 20, 6, 4, 5]) == 5)

class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        if val is None:
            self.count = 0
        else:
            self.count = 1
        
    def search(self, val):
        if self.value is None:
            return 0
        if val < self.value:
            return (self.count if self.left is None else 
                    (self.count + self.left.search(val)))
        else:
            return 0 if self.right == None else self.right.search(val)

    def insert(self, val):
        if self.value is None:
            self.value = val
            self.count = 1
        elif self.value == val:
            self.count += 1
        else:
            if val < self.value: 
                if self.left is not None:
                    self.left.insert(val)
                else:
                    self.left = Node(val)
            else:
                self.count += 1
                if self.right is not None:
                    self.right.insert(val)
                else:    
                    self.right = Node(val)
    
def getInvCount_BST(a):
    bst = Node(None)    
    count = 0
    for n in a:
        count += bst.search(n)
        bst.insert(n)
    return count

if __name__ == '__main__':
    assert(getInvCount_BST([1, 10, 20, 6, 4, 5]) == 8)

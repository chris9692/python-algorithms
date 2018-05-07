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

def merge(al, ar):
    count = 0
    i = 0
    j = 0
    a = []
    while i < len(al) and j <= len(ar):
        if j < len(ar) and al[i] > ar[j]:
            a.append(ar[j])
            j += 1 
        else:
            a.append(al[i])
            count += j 
            i += 1
    #print(count, a, al, ar)
    return count, a
        
def getInvCount_MS(a):
    """
    This is the merge sort method that takes O(nlogn) time
    and with side effects
    """
    count = 0
    
    if len(a) < 2:
        return 0, a
    
    if len(a) == 2:
        count = 1 if a[0] > a[1] else 0
        a.sort()
        return count, a
 
    m = len(a) // 2
    
    nl, al = getInvCount_MS(a[:m])
    nr, ar = getInvCount_MS(a[m:])
    nm, am = merge(al, ar)
    
    return nl + nr + nm, am

if __name__ == '__main__':
    print(getInvCount_MS([1, 20, 6, 4, 5]))

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
        """
        the assumption is that elements will be inserted
        from left to right into the BST, therefore, the 
        search is looking for any prior numbers that is 
        larger than current
        """
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
    """
    This is the BST method that takes O(nlogn) time
    and O(n) extra space
    """
    bst = Node(None)    
    count = 0
    for n in a:
        count += bst.search(n)
        print(n, count)
        bst.insert(n)
    return count

if __name__ == '__main__':
    assert(getInvCount_BST([10, 20, 6, 4, 5]) == 8)
    

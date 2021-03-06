
import numpy as np
class minHeap(object):
    """
    """
    def __init__(self):
        self.heap = []
        self.size = 0
 
    # for a sub-tree of size n (not neccessarily the same as "size")
    # make sure any node has value less than its children
    

    def heapify(self, r, n):
        left = 2 * r + 1
        right = 2 * r + 2
 
        nextR = r
        if left < n and self.heap[left] < self.heap[r]:
            nextR = left

        if right < n and self.heap[right] < self.heap[r]:
            nextR = right
 
        if nextR != r:
            self.heap[r], self.heap[nextR] = self.heap[nextR], self.heap[r] 
            self.heapify(nextR, n)
    
    def heapSort(self, arr):
        self.heap = arr[:]
        self.size = len(arr)
        
        # heapify, starting from the last non-leaf node
        for r in range((self.size - 1) // 2, -1, -1):
            self.heapify(r, self.size)
            
        # in each loop, take the smallest from heap[0]
        # and save it in the end, and then recreate
        # the min heap for the rest numbers
        
        for i in range(self.size - 1, -1, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.heapify(0, i)
        self.heap = self.heap[-1::-1]    
            
        return self.heap

    def nlargest(self, n):
        return self.heap[max(self.size - n, 0):]
    
    def nsmallest(self, n):
        return self.heap[0: min(n, self.size)]

mh = minHeap()
mh.heapSort([33, 17, 14, 27, 18, 9, 5, 19, 11, 21])

class Node(object):
    def __init__(self, val=None, next=None):
        self.value = val
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    def addNode(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            prevNode = None
            nextNode = self.head
            while nextNode is not None and val > nextNode.value:
                prevNode = nextNode
                nextNode = nextNode.next
                
            if prevNode is not None:
                prevNode.next = Node(val, nextNode)    
            else:
                self.head = Node(val, nextNode)
        self.size += 1
        return self.size    
    
    def removeDuplidate(self):
        if self.head is None:
            return True
        thisNode = self.head
        while thisNode is not None:
            nextNode = thisNode.next
            while nextNode is not None and thisNode.value == nextNode.value:
                nextNode = nextNode.next
            thisNode.next = nextNode
            thisNode = thisNode.next
            
    
    def printme(self):
        out = ''
        nextNode = self.head
        while nextNode:
            out += str(nextNode.value) + ','
            nextNode = nextNode.next
        print(out)

ll = LinkedList()        
print(ll.addNode(3))
print(ll.addNode(2))
print(ll.addNode(5))
print(ll.addNode(5))
print(ll.addNode(6))
ll.printme()
print(ll.removeDuplidate())
ll.printme()

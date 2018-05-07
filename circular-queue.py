class CircularQueue:

    #Constructor
    # holds maxSize - 1 data elements
    def __init__(self, maxSize):
        self.queue = [0] * maxSize
        self.head = 0
        self.tail = 0
        self._size = 0
        self.maxSize = maxSize

    #Adding elements to the queue
    def enqueue(self,data):
        if self.size() == self.maxSize - 1:
            return None
        self.queue[self.tail] = data
        self.tail = (self.tail + 1) % self.maxSize
        self._size += 1
        return data

    #Removing elements from the queue
    def dequeue(self):
        if self.size() == 0:
            return None
        data = self.queue[self.head]
        self.head = (self.head + 1) % self.maxSize
        self._size -= 1
        return data

    #Calculating the size of the queue
    def size(self):
        return self._size
    
    def printme(self):
        out = ''
        for i in range(self.maxSize):
            if i == self.head:
                out += str(self.queue[i]) + 'H,'
            elif i == self.tail:
                out += 'T,'
            else:
                out += str(self.queue[i]) + ','
        print(out)           

q = CircularQueue(8)
q.enqueue(1);print(q.printme())
q.enqueue(2);print(q.printme())
q.enqueue(3);print(q.printme())
q.enqueue(4);print(q.printme())
q.enqueue(1);print(q.printme())
q.enqueue(2);print(q.printme())
q.enqueue(3);print(q.printme())
q.enqueue(4);print(q.printme())
q.dequeue();print(q.printme())
q.dequeue();print(q.printme())
q.enqueue(5);print(q.printme())
q.enqueue(5);print(q.printme())
q.enqueue(5);print(q.printme())
q.dequeue();print(q.printme())
q.dequeue();print(q.printme())
q.dequeue();print(q.printme())
q.dequeue();print(q.printme())
q.dequeue();print(q.printme())
q.dequeue();print(q.printme())
q.dequeue();print(q.printme())
q.dequeue();print(q.printme())
q.dequeue();print(q.printme())

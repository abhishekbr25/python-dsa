import sys
class Node:
    def __init__(self, prev=None, item =None, next=None):
        self.prev = prev
        self.item = item
        self.next = next
    
class CDLL:
    def __init__(self, start=None):
        self.start = start
    def isempty( self ):
        return self.start == None
    def printList(self):
        temp = self.start
        while temp.next is not self.start:
            print(temp.item, end=" ")
            temp = temp.next
        print(temp.item, end=" ")
    def insslast(self, data):
        n=Node(None, data)
        if not self.isempty():
            n.next = self.start 
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start = n
            return
        n.prev = n
        n.next = n
        self.start = n
    def insslast (self, data):
        n=Node(None, data, None)
        if not self.isempty():
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
            return
        self.start = n
        n.prev = self.start
        n.next=self.start
    def search(self, data):
        if not self.isempty():
            temp = self.start
            if temp.item == data:
                return temp
            else:
                temp = temp.next
            while temp is not self.start:
                if temp.item == data:
                    return temp
                temp = temp.next
            return None
    def insafter(self,temp, data):
        if temp is not None:
            n=Node(temp, data, temp.next)
            temp.next.prev = n
            temp.next = n
    def delfirst(self):
        if not self.isempty():
            if self.start.next == self.start:
                self.start = None
                return
            else:
                self.start.next.prev = self.start.prev
                self.start.prev.next = self.start.next
                self.start = self.start.next
    def dellast(self):
        if not self.isempty():
            if self.start.next == self.start:
                self.start = None
                return
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
    def delItem(self, data):
        if not self.isempty():
            temp = self.start
            if temp.item == data:
                self.delfirst()
            else:
                temp = temp.next
                while temp is not self.start:
                    if temp.item == data:
                        temp.next.prev = temp.prev
                        temp.prev.next = temp.next
                        return
                    temp = temp.next
    def __iter__(self):
        return CDLLIterator(self.start)
    
class CDLLIterator:
    def __init__(self, start = None):
        self.current = start
        self.start = start
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.count == 1 and self.current==self.start:
            raise StopIteration
        else:
            self.count=1
            data = self.current.item
            self.current = self.current.next
            return data
    

ll = CDLL()
ll.insslast(19)
ll.insslast(11)
ll.insslast(14)
ll.insslast(13)
ll.insslast(12) 
# print(ll.search(1))
# ll.printList()
print("getsizeof(ll):", sys.getsizeof(ll))
for i in ll:
    print(i, end=" ")
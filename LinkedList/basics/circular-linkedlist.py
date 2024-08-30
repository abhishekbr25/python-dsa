import sys
class Node:
    def __init__(self, item = None, next=None):
        self.next = next
        self.item = item

class Cll:
    def __init__(self, last=None):
        self.last=last

    def is_empty(self):
        return self.last == None
    def insert_at_start(self, data):
        n=Node(data)
        if self.is_empty():
            self.last=n
            n.next=n
        else:
            n.next=self.last.next
            self.last.next=n
    def insert_at_start(self, data):
        n=Node(data)
        if self.is_empty():
            self.last = n
            n.next = n
        else:
            n.next = self.last.next
            self.last.next = n 
    def search(self, data):
        if not self.is_empty():
            temp=self.last
            if self.last.next == self.last:
                if self.last.item == data:
                    return self.last
            while temp.next is not self.last:
                if temp.next.item == data:
                    return temp.next
                temp = temp.next
    def insert_after(self, temp, data):
        if temp is not None:
            n=Node(data, temp.next)
            temp.next = n
            if temp is self.last:
                self.last = n 
    def print_list(self):
        if not self.is_empty():
            temp=self.last.next
            while temp is not self.last:
                print(temp.item)
                temp = temp.next
            print(temp.item)
    def delete_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last = None
            self.last.next = self.last.next.next

    def delete_last(self):
        if not self.is_empty():
            if self.last is self.last.next:
                self.last = None
                return
            else:
                temp=self.last
                while temp.next is not self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp 
    def delete_item(self, data):
        if not self.is_empty():
            if self.last == self.last.next:
                if self.last.item == data:
                    self.last = None
                    return 
            temp = self.last.next
            if temp.item == data:
                self.last.next = temp.next
                return
            while temp.item is not data:
                if temp.next.item == data and temp.next is self.last:
                    temp.next = temp.next.next
                    self.last = temp
                    return
                elif temp.next.item == data and temp.next is not self.last:
                    temp.next = temp.next.next 
                    return
                temp = temp.next
    def __iter__ (self):
        if self.last ==None:
            return CllIterator(self.last)    
        else:
            return CllIterator(self.last.next)

class CllIterator:
    def __init__(self,start):
        self.current = start
        self.start = start
        self.count =0
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.start == None:
            raise StopIteration
        if self.current == self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
            data = self.current.item
            self.current = self.current.next
            return data
 
            
cll = Cll() 
cll.insert_at_start(2)
cll.insert_at_start(1)
cll.insert_at_start(1)
cll.insert_at_start(0)
cll.insert_at_start(11)

print("getsizeof(ll):", sys.getsizeof(cll))
# cll.print_list()

# cll.delete_item(0)

# print(end="**\n")
# print(cll.last.item)


# print(end="**\n")
# cll.print_list() 

for i in cll:
    print(i, end=" ")
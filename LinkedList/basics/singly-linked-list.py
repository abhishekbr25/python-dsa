import sys
class Node:
    def __init__(self, item=None, next = None):
        self.item = item
        self.next = next

class Sll:
    def __init__(self,start=None):
        self.start = None
    def is_empty(self):
        return self.start == None
    def insert_at_start(self, data):
        n=Node(data, self.start)
        self.start = n
    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start=n
    def Search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next              
        return None
    def insert_after_data(self, item, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                n=Node(item,temp.next)
                temp.next=n
                return #fn shoul exit immediately so node doesnot insert after other same data node(1,2,3,2,4)
            temp = temp.next
        return None
    def insert_after_node(self, item, temp):
        if temp is not None:
            n=Node(item, temp.next)
            temp.next=n
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp = temp.next
    def delete_first(self):
        if self.start is not None:
            temp = self.start
            self.start = temp.next
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
    def delete_item(self, data):
        if self.start is None:
            return
        elif self.start.next is None or self.start.item==data:
            self.start=self.start.next
        else:
            temp = self.start
            while temp.next is not None:
                if temp.next.item == data:
                    temp.next=temp.next.next
                    return
                temp=temp.next
    def insert_before_node(self, data, node):
        if node is None or self.start is None:
            return
        elif self.start == node:
            n=Node(data, self.start)
            self.start = n
            return
        temp=self.start
        while temp.next is not None:
            if temp.next == node:
                n=Node(data, temp.next)
                temp.next=n
                return
            temp=temp.next
    def __iter__(self):
        return SllIterator(self.start)
    

#make sll iterable
class SllIterator:
    def __init__(self, start) :
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current = self.current.next
        return data

            

# divercode
mylist = Sll()
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_at_start(5)
mylist.insert_after_data(15, 10)
mylist.insert_after_node(17, mylist.Search(15))
mylist.delete_first()
mylist.delete_item(17)
print()

print("getsizeof(ll):", sys.getsizeof(mylist))
print("---------------------------")
for item in mylist: 
    print(item, end=" ")
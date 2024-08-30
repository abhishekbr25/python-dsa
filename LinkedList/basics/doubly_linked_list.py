class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev=prev
        self.item=item
        self.next=next
class Dll:
    def __init__(self, start=None):
        self.start=start
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next
    def insert_at_start(self, data):
        n=Node(None, data, self.start)
        if self.start is not None:
            self.start.prev=n
        self.start = n
    def insert_at_last(self, data):
        temp = self.start
        if temp is not None: 
            while temp.next is not None:
                temp = temp.next
            n=Node(temp, data, None)
            temp.next = n
            return
        n= Node(temp, data, None)
        temp.start=n
    def Search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
    def insert_after_node(self, node, data):
        if node is not None:
            n=Node(node, data, node.next)
            if node.next is not None:
                node.next.prev=n
            node.next = n
    def delete_from_start(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None: 
                self.start.prev = None 
    def delete_from_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def delete_after_node(self, node):
        if node is not None:
            temp = self.start
            while not temp==node:
                temp = temp.next    
            temp.next = temp.next.next
    def delete_item(self, data):
        if self.start is None:
            pass
        # elif self.start.next is None:
        #     if self.start.item == data:
        #         self.start = None
        else:
            temp = self.start
            # if self.start.item == data:
            #     self.start = self.start.next
            #     temp.next.prev = None
            # else:
            while temp is not None:
                if temp.item==data:
                    if temp.prev is not None:
                        temp.next.prev = temp.prev
                    elif temp.next is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    return
                temp = temp.next
    def __iter__(self):
        return DllIterator(self.start)

class DllIterator:
    def __init__(self, start=None):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data=self.current.item
            self.current = self.current.next
            return data


            
# driver code 
dll = Dll()

dll.insert_at_start(12)
dll.insert_at_start(13)
dll.insert_at_start(14)
dll.insert_at_start(15)
dll.insert_at_start(16)
dll.insert_at_last(11)
dll.delete_after_node(dll.Search(17))
for i in dll:
    print(i)
# print(dll.Search(146))

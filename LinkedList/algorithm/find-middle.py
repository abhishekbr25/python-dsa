'''
tortoise and heir algo
or 
slow and fast pointer
https://www.naukri.com/code360/problems/middle-of-linked-list_973250

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

'''

def findMiddle(head):
    # Write your code here
    # head denoted head of linked list
    slow  = head
    fast =  head
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow
    pass
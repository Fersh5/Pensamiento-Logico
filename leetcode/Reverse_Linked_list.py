# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Example 2:
# Input: head = [1,2]
# Output: [2,1]

# Example 3:
# Input: head = []
# Output: []

from typing import Optional,List 

# Definition for singly-linked list.
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        temp = head
        while temp:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
        return prev
    
def print_linked_list(head:Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=' -> ')
        current=current.next
    print(None)

def create_linked_list(nodes:List):
    head = ListNode(nodes[0])
    current=head
    for value in nodes[1:]:
        current.next=ListNode(value)
        current=current.next
    return head

list_1 = create_linked_list([1,2,3,4,5])
print_linked_list(list_1)

case_1=Solution()
print_linked_list(case_1.reverseList(list_1))


        
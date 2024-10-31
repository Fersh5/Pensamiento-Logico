# You are given two non-empty linked lists representing two non-negative integers. 
# The most significant digit comes first and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]

# Example 2:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [8,0,7]

# Example 3:
# Input: l1 = [0], l2 = [0]
# Output: [0]

from typing import Optional,List

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_linked_list(head:ListNode):
            new_head= None
            current=head
            while current:
                next_node=current.next
                current.next = new_head
                new_head=current
                current=next_node
            return new_head
        l1=reverse_linked_list(l1)
        l2=reverse_linked_list(l2)
        head=ListNode((l1.val+l2.val)%10)
        carry=(l1.val+l2.val)//10
        l1=l1.next
        l2=l2.next
        val_1 = l1.val if l1 else 0
        val_2 = l2.val if l2 else 0
        current=head
        while l1 or l2 or carry:
            current.next=ListNode((val_1+val_2+carry)%10)
            carry=(val_1+val_2+carry)//10
            current=current.next
            if l1==None:
                val_1=0
            elif l1.next==None:
                l1=l1.next
                val_1=0
            else:
                l1=l1.next
                val_1=l1.val
            
            if l2==None:
                val_2=0
            elif l2.next==None:
                l2=l2.next
                val_2=0
            else:
                l2=l2.next
                val_2=l2.val
        return reverse_linked_list(head)
        

def created_linked_list(lista:List) -> ListNode:
    head=ListNode(lista[0])
    current=head
    for element in lista[1:]:
        current.next=ListNode(element)
        current=current.next
    return head

def print_linked_list(head:ListNode):
    current=head
    while current:
        print(current.val,end=' -> ')
        current = current.next
    print(None)

case_1=Solution()
lista1=created_linked_list([7,2,4,3])
print_linked_list(lista1)
lista2=created_linked_list([5,6,4])
print_linked_list(lista2)
lista3=case_1.addTwoNumbers(lista1,lista2)

# print_linked_list(lista1)
# print_linked_list(lista2)
print_linked_list(lista3)

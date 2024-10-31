# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

from typing import Optional,List

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
        return head
    

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

case1=Solution()    

lista_1=created_linked_list([9,9,9,9,9,9,9])
lista_2=created_linked_list([9,9,9,9])
lista_3=(case1.addTwoNumbers(lista_1,lista_2))
print_linked_list(lista_1)
print_linked_list(lista_2)
print_linked_list(lista_3)

lista_1=created_linked_list([2,4,3])
lista_2=created_linked_list([5,6,4])
lista_3=(case1.addTwoNumbers(lista_1,lista_2))
print_linked_list(lista_1)
print_linked_list(lista_2)
print_linked_list(lista_3)


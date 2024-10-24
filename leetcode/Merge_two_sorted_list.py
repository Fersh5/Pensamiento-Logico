# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Example 2:
# Input: list1 = [], list2 = []
# Output: []

# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
 
# Definition for singly-linked list.

from typing import Optional, List

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if list1:
#             index_1=0
#             lim1=len(list1)
#             v_list1=True
#         else:
#             v_list1=False
#         if list2:
#             index_2=0
#             lim2=len(list2)
#             v_list2=True
#         else:
#             v_list2=False
#         r_list=[]
#         while True:
#             if v_list1 and v_list2:
#                 if list1[index_1]<list2[index_2]:
#                     r_list.append(list1[index_1])
#                     index_1+=1
#                     if lim1==index_1:
#                         v_list1=False
#                 else:
#                     r_list.append(list2[index_2])
#                     index_2+=1
#                     if lim2==index_2:
#                         v_list2=False
#             elif v_list1:
#                 r_list+=list1[index_1:]
#                 return r_list
#             elif v_list2:
#                 r_list+=list2[index_2:]
#                 return r_list

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val<list2.val:
            head=list1
            list1=list1.next
        else:
            head=list2
            list2=list2.next
        act=head
        n_node=0
        while list1 is not None or list2 is not None:
            if list1 is None:
                act.next=list2
                break
            if list2 is None:
                act.next=list1
                break
            if list1.val < list2.val:
                act.next=list1
                act=act.next
                list1=list1.next
            else:
                act.next=list2
                act=act.next
                list2=list2.next
        return head
    
def create_linked_list(values:List):
    if not values:
        return None
    head=ListNode(values[0])
    current=head
    for value in values[1:]:
        current.next=ListNode(value)
        current=current.next
    return head

def print_linked_list(head):
    current=head
    while current:
        print(current.val, end= " -> ")
        current=current.next
    print(None)

list_1=create_linked_list([1,2,4])
list_2=create_linked_list([1,3,4])      

case_1=Solution()
print_linked_list(case_1.mergeTwoLists(list_1,list_2))


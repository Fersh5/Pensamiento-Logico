# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a 
# time (in the order specified by bills). Each customer will only buy one lemonade and pay with either 
# a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that 
# the customer pays $5.

# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide 
# every customer with the correct change, or false otherwise.

# Example 1:
# Input: bills = [5,5,5,10,20]
# Output: true
# Explanation: 
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.

# Example 2:
# Input: bills = [5,5,10,10,20]
# Output: false
# Explanation: 
# From the first two customers in order, we collect two $5 bills.
# For the next two customers in order, we collect a $10 bill and give back a $5 bill.
# For the last customer, we can not give the change of $15 back because we only have two $10 bills.
# Since not every customer received the correct change, the answer is false.

from typing import List

# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         amount={5:0,10:0,20:10}
#         for bill in bills:
#             amount[bill]+=1
#             if bill == 10:
#                 if amount[5]:
#                     amount[5]-=1
#                 else:
#                     return False
#             elif bill == 20:
#                 if amount[10] and amount[5]:
#                     amount[10]-=1
#                     amount[5]-=1
#                 elif amount[5]>2:
#                     amount[5]-=3
#                 else:
#                     return False
#         return True

# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         cash=[]
#         for bill in bills:
#             if bill == 10:
#                 cash.append(bill)
#                 if 5 in cash:
#                     cash.remove(5)
#                 else:
#                     return False
#             elif bill ==5:
#                 cash.insert(0,bill)
#             else:
#                 if 10 in cash and 5 in cash:
#                     cash.remove(5)
#                     cash.pop()
#                 elif cash.count(5)>2:
#                     cash.pop(0)
#                     cash.pop(0)
#                     cash.pop(0)
#                 else:
#                     return False
#         return True

# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         den_5=0
#         den_10=0
#         for bill in bills:
#             if bill == 5:
#                 den_5+=1
#             elif bill == 10:
#                 den_5-=1
#                 den_10+=1
#             else:
#                 if den_10:
#                     den_5-=1
#                     den_10-=1
#                 else:
#                     den_5-=3
#             if den_5<0:
#                 return False
#         return True


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        den_5=0
        den_10=0
        for bill in bills:
            if bill == 5:
                den_5+=1
            elif bill == 10:
                if den_5:
                    den_5-=1
                    den_10+=1
                else:
                    return False
            else:
                if den_10 and den_5:
                    den_5-=1
                    den_10-=1
                elif den_5>2:
                    den_5-=3
                else:
                    return False
        return True 

        

case_1=Solution()
print(case_1.lemonadeChange([5,5,5,10,20]))
print(case_1.lemonadeChange([5,5,10,10,20]))
            
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing 
# the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To 
# accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

# from typing import List

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         index_1=0
#         index_2=0
#         aux=[]
#         if n!=index_2:
#             while index_1<len(nums1):
#                 if index_1<m:
#                     if aux and index_2<n:
#                         if nums2[index_2]<aux[0]:
#                             aux.append(nums1[index_1])
#                             nums1[index_1]=nums2[index_2]
#                             index_1+=1
#                             index_2+=1
#                         else:
#                             aux.append(nums1[index_1])
#                             nums1[index_1]=aux.pop(0)
#                             index_1+=1
#                     elif index_2<n:
#                         if nums2[index_2]<nums1[index_1]:
#                             aux.append(nums1[index_1])
#                             nums1[index_1]=nums2[index_2]
#                             index_1+=1
#                             index_2+=1
#                         else:
#                             index_1+=1
#                     else:
#                         aux.append(nums1[index_1])
#                         nums1[index_1]=aux.pop(0)
#                         index_1+=1
#                 else:
#                     if aux and index_2<n:
#                         if aux[0]<nums2[index_2]:
#                             nums1[index_1]=aux.pop(0)
#                             index_1+=1
#                         else:
#                             nums1[index_1]=nums2[index_2]
#                             index_2+=1
#                             index_1+=1
#                     elif aux:
#                         nums1[index_1]=aux.pop(0)
#                         index_1+=1
#                     else:
#                         nums1[index_1]=nums2[index_2]
#                         index_2+=1
#                         index_1+=1
#                 # print(nums1)
#         print(nums1)

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index_2,index_1=n-1,m-1
        i=m+n-1
        while index_2>=0:
            if index_1>=0 and nums1[index_1]>nums2[index_2]:
                nums1[i]=nums1[index_1]
                index_1-=1
            else:
                nums1[i]=nums2[index_2]
                index_2-=1
            i-=1




case_1=Solution()
case_1.merge([1,2,3,0,0,0],3,[2,5,6],3)
case_1.merge([1],1,[],0)
case_1.merge([4,5,6,0,0,0],3,[1,2,3],3)
case_1.merge([4,0,0,0,0,0],1,[1,2,3,5,6],5)
case_1.merge([1,2,4,5,6,0],5,[3],1)


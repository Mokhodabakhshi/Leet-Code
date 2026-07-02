from typing_extensions import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        nums1[:] = nums1 + nums2
        nums1[:] = self.merge_sort(nums1)
        
    def Merge(self, left, right):
        sorted_list = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        return sorted_list
    
    def merge_sort(self,arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        
        return self.Merge(left,right)
    
    

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

s = Solution()
s.merge(nums1,m,nums2,n)

print(nums1)
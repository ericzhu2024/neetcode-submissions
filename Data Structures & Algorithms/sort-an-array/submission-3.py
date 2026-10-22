class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def quickSort(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[len(arr)//2]
            left = [x for x in arr if x < pivot]
            mid = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
            return quickSort(left) + mid + quickSort(right)
        
        return quickSort(nums)
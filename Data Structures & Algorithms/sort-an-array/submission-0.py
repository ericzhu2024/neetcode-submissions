class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def merge_sort(arr):
            # Base case: A list of zero or one elements is already sorted
            if len(arr) <= 1:
                return arr

            # 1. DIVIDE: Find the midpoint and split the array
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            # Recursively sort both halves
            left_sorted = merge_sort(left_half)
            right_sorted = merge_sort(right_half)

            # 2. CONQUER: Merge the two sorted halves back together
            return merge(left_sorted, right_sorted)

        def merge(left,right):
            i = j = 0
            res = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            res += left[i:]
            res += right[j:]
            return res
        return merge_sort(nums)
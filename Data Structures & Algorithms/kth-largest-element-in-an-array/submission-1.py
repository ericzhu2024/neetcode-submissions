class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [ -n for n in nums]
        heapq.heapify(nums)
        res = None
        while k > 0:
            k -= 1
            res = heapq.heappop(nums)
        
        return -res
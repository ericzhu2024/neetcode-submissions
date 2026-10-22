class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        array = [ - n for n in nums]
        heapq.heapify(array)
        while k > 0:
            res = heapq.heappop(array)
            k -= 1
        return -res 
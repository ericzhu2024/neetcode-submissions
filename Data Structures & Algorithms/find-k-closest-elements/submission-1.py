class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0 
        count = 0

        for r in range(len(arr)):
            if count < k:
                count += 1
            elif count == k:
                if abs(arr[r] - x) < abs(arr[l] - x) or (arr[r] == arr[l]) :
                    l += 1
                else:
                    return arr[l:r]
        return arr[l:l+count]        

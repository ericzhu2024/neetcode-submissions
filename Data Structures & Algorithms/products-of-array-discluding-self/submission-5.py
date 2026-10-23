class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n

        pre_product = 1
        for i in range(n):
            pre[i] = pre_product
            pre_product *= nums[i]
        
        post = [0] * n
        post_product = 1
        for j in range(n - 1, -1, -1):
            post[j] = post_product
            post_product *= nums[j]
        
        res = [0] * n
        for k in range(n):
            res[k] = pre[k] * post[k]
        
        return res
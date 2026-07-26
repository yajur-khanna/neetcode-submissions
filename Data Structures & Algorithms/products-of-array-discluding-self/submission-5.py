class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        pre = [1] * n
        for i in range(1, n):
            pre[i] = prefix * nums[i-1]
            prefix *= nums[i-1]
        postfix = 1
        post = [1] * n
        for i in range(n-2, -1, -1):
            post[i] = postfix * nums[i+1]
            postfix *= nums[i+1]
        res = []
        for i in range(n):
            res.append(post[i]*pre[i])
        return res
# https://leetcode.com/problems/product-of-array-except-self/
#
class Solution:
    def productExceptSelf(self, nums: list) -> list:
        # initial

        # size = len(nums)
        # product = 1
        # zero_indices = []
        # for i in range(size):
        #     if nums[i] is 0:
        #         zero_indices.append(i)
        #         continue
        #     product *= nums[i]

        # if zero_indices:
        #     answer = [0] * size
        #     if len(zero_indices) == 1:
        #         for zero_idx in zero_indices:
        #             answer[zero_idx] = product
        # else:
        #     answer = [product] * size
        #     for i in range(size):
        #         answer[i] //= nums[i]
        # return answer

        # Follow-up, optimization
        
        # size = len(nums)
        # product = 1
        # zero_count = 0
        # for i in range(size):
        #     if nums[i] == 0:
        #         zero_count += 1
        #     else:
        #         product *= nums[i]
        # if zero_count == 0:
        #     answer = [ product // nums[i] for i in range(size) ]
        # elif zero_count == 1:
        #     answer = [ product if nums[i] == 0 else 0 for i in range(size) ]
        # else:
        #     answer = [0] * size
        # return answer

        # without division
        pre = []
        product = 1
        for i in range(len(nums)):
            pre.append(product)
            product *= nums[i]

        post = []
        product = 1
        for i in range(len(nums)-1, -1, -1):
            post.append(product)
            product *= nums[i]

        return [pre[i] * post[len(nums)-i-1] for i in range(len(nums))]

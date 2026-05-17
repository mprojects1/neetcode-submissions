class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1]*len(nums)

        i = 0 

        while i < len(nums):

            for j in range(len(nums)):
                if j == i: continue
                output[i] = output[i]*nums[j]

            i += 1  

        return output
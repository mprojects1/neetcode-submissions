class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for i in nums:
            if i in num_dict:
                return True
            num_dict[i] = 1
        
        return False
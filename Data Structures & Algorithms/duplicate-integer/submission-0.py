class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for i in nums:
            num_dict[i] = num_dict.get(i, 0) + 1

        for keys , value in num_dict.items():
            if value > 1:
                return True
        
        return False
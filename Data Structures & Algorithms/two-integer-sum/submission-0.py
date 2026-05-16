class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        map = {}

        for i in range(len(nums)):

           cur_num = nums[i]
           req = target - cur_num 
           
           if req in map:
                return [map[req], i]

           map[cur_num] = i 

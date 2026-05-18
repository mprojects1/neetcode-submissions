class Solution:
    def trap(self, height: List[int]) -> int:
        
        pre_max = [0]*len(height)
        suf_max = [0]*len(height)

        total_water = 0
        prefix = 0
        for i in range(len(height)):
            pre_max[i] = prefix
            prefix = max(prefix, height[i])
        
        suffix = 0

        for i in range(len(height)-1, -1 ,-1):
            suf_max[i] = suffix
            suffix = max(suffix,height[i])


        for i in range(len(height)):
            water = min(pre_max[i], suf_max[i]) - height[i]
            if water <= 0:
                continue
            else:
                total_water += water



        return total_water
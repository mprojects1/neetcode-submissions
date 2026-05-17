class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort

        count = {}

        bucket = [[] for _ in range(len(nums) + 1)]

        output = []

        for i in nums:
            count[i] = count.get(i,0) + 1
        
        for key, value in count.items():
            bucket[value].append(key)

        for item in range(len(bucket)-1, 0, -1):
            if len(output) >= k: break
            if bucket[item] != []: output.extend(bucket[item])
        
        return output


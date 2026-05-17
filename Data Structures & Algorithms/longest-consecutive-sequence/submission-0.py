class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        heapq.heapify(nums)

        prev = heapq.heappop(nums)
        cur_max = 1
        abs_max = 1

        while nums:

            cur = heapq.heappop(nums)

            if cur == prev:
                continue
            elif cur == prev + 1 :
                cur_max += 1
                abs_max = max(abs_max, cur_max)
            else:
                cur_max = 1
            
            prev = cur


        return abs_max  



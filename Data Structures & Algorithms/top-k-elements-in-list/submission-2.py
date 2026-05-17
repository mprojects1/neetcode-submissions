class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for i in nums:
            count[i] = count.get(i,0) + 1

        # Define an empty heap
        my_heap = []

        for key, value in count.items():
            heapq.heappush(my_heap, (value, key))

            if len(my_heap) > k:
                heapq.heappop(my_heap)

        output = []

        for i, j in my_heap:
            output.append(j)

        return output
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        top_k = count.most_common(k)

        output = []

        for i in top_k:
            output.append(i[0])
        
        return output

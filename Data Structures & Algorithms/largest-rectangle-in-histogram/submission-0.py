class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        n = len(heights)
        max_rec_area = 0

        for i in range(n):
            height = heights[i]

            right = i+1

            while right<n and heights[right] >= height:
                right +=1

            left = i

            while left>=0 and heights[left] >=height:
                left -=1

            area = (right - left - 1) * height 

            max_rec_area = max(area, max_rec_area)
        return max_rec_area

             
            
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        la = len(nums1)
        lb = len(nums2)

        len_left = (lb + la + 1) // 2

        if la > lb:

            nums1, nums2 = nums2, nums1 

        l = 0 

        r = len(nums1) 

        while True:

            i = (l+r) // 2

            j = len_left - i

            aleft = nums1[i-1] if i-1 >= 0 else float("-infinity")
            aright = nums1[i] if i < len(nums1) else float("+infinity")
            bleft = nums2[j-1] if j-1 >= 0 else float("-infinity")
            bright = nums2[j] if j < len(nums2) else float("+infinity")

            if aleft <= bright and bleft <= aright:
                
                if (len(nums1)+len(nums2)) % 2:
                    return max(aleft,bleft)
                    
                else: return(max(aleft,bleft)+ min(aright,bright))/2

            elif aleft > bright:
                r = i - 1

            else:

                l = i+1




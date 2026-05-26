class Solution:

    def canfinish(self, mid, piles):
        timetaken = 0
        for i in piles:

            timetaken += (i+mid-1)//mid

        return timetaken 
    

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = 0

        

        for i in piles:
            r = max(r, i)

        k = r

        while l<=r:

            mid = (l+r)//2

            result = self.canfinish(mid, piles)

            if result <=  h:
                
                r = mid -1

                k = min(k,mid)

            elif result > h:

                l = mid + 1
            
        return k
                







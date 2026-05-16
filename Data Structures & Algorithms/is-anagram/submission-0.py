class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        else:
            count_s = {}
            count_t = {}
            for i in s:
                count_s[i] = count_s.get(i,0) + 1
            for i in t:
                count_t[i] = count_t.get(i,0) + 1

            for key in count_s.keys():
                if count_s[key] != count_t.get(key,0):
                    return False
            
            return True
class Solution:

    def is_anagram(self, s: str, t: str):

        if len(s) != len(t):
            return False
        count = [0]*26
        for i in range(len(s)):

            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        return count == [0]*26


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        output = []

        if len(strs) == 1:
            output.append(strs)
            return output

        visited = [False] * len(strs)

        for i in range(len(strs)):
            
            if visited[i]:
                continue

            group = [strs[i]]
            visited[i] = True

            for j in range(i+1, len(strs)):
                if visited[j]:
                    continue
                check = self.is_anagram(strs[i], strs[j])

                if check:
                    group.append(strs[j])
                    visited[j] = True

            output.append(group)
        
        return output
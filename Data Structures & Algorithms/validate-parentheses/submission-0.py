class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        match_dict = {")":"(","]":"[","}":"{"}

        for c in s:

            if c in match_dict.keys():
                
                top_value = stack.pop() if stack else "#"

                if top_value != match_dict[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0


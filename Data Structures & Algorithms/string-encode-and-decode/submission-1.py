class Solution:

    def encode(self, strs: List[str]) -> str:

       output = ""

       for s in strs:
        output += f"{len(s)}#{s}"

       return output 
    

    def decode(self, s: str) -> List[str]:
        
        result = []
        i = 0

        while i < len(s):

            j = i 

            #find # using j pointer
            while s[j] != '#':

                j +=1

            #get length from eg i->4#<-jhello
            str_len = int(s[i:j])

            #move i ahead of #
            i = j+1

            orig_str = s[i:str_len+i]

            result.append(orig_str)

            i+=str_len

        return result  

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k = 0
        n = []
        min = len(strs[0])
        l = len(strs)
        have = False
        for i in range(l):
            
            min_t = len(strs[i])
            if min_t < min:
                min = min_t
        
        for j in range(min):
            n.append(list(strs[0])[j])
            t = 0




            for m in range(l):
                if "".join(n) == strs[m][:j+1]:
                    t += 1
            if t == l:
                have = True
                if j+1 == min:
                    k = 1
                else:
                    continue
            else:  
                break
        
        

        if len(n) == 1 or k == 1:
            if have:
                return "".join(n)
            else:
                return ""
        else:
            if have:
                return "".join(n[:-1])
            else:
                return ""

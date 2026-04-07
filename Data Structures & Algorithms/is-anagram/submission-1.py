class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seens={}
        seent={}

        for c in s:
            if c not in seens:
                seens[c]=1
            else:
                seens[c]+=1

        for c in t:
            if c not in seent:
                seent[c]=1
            else:
                seent[c]+=1

        return seens == seent
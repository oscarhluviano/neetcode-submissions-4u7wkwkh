class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seens={}
        seent={}

        for c in s:
            seens[c] = seens.get(c, 0)+1

        for c in t:
            seent[c] = seent.get(c, 0)+1

        return seens == seent
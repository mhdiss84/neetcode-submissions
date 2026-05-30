class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if lengths are not equal, cannot be anagrams
            return False 

        countS, countT = {}, {} # define two hashmaps to map each character count

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # keep updating the count on each key
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0): # check if each character count matches in both maps
                return False
        
        return True
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mpping charCount to list of anagrams | deafultdict(list) instead of {}

        for s in strs: # go through every string that we're given in the input
            count = [0] * 26 # an array: a ... z

            for c in s: # go through every single character in each string
                count[ord(c) - ord("a")] += 1 # mapping a to index 0 and z to index 25
                #     ^^^^^^   ^^^^^^^^ 
                #   ASCII value of the current characte - ASCII value of a
            
            # group all anagrams for this particular count | in python lists can't be keys -> make count a tuple
            res[tuple(count)].append(s) 

        return list(res.values())
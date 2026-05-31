class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # value : index

        for i, n in enumerate(nums): # track both the index and the value
            diff = target - n # difference between target and the value
            if diff in prevMap: # if diff is in the map, return the indices 
                return [prevMap[diff], i]
            prevMap[n] = i # map the value to its index
        return
        
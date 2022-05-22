#USE HASHMAP to see if number has been traversed.
#Save the remaining value required for target
#Check if it is present in hashmap
#Else store with value as index and keep traversing

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,val in enumerate(nums):
            remaining = target - val
            if remaining in seen:
                return [seen[remaining],i]
            seen[val] = i
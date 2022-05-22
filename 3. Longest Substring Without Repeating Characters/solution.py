class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charDict = {}
        i=0
        j=0
        maxCount = 0
        for ind,c in enumerate(s):
            if c in charDict:
                i = max(i, charDict[c] + 1) #consider abab for maximum logic
            charDict[c] = ind
            j = ind
            maxCount = max(maxCount, j-i+1)
        return maxCount
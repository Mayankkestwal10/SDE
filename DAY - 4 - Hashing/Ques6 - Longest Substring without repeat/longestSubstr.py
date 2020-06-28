class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        
        maxLength = 0
        
        d = set()
        n = len(s)
        
        while(start<n and end<n):
            if(s[end] not in d):
                d.add(s[end])
                end+=1
                maxLength = max(end-start, maxLength)
            else:
                d.remove(s[start])
                start+=1

        return maxLength
#Using sliding window approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        tab = {}
        i = 0
        for j in range(n):
            if s[j] in tab:
                i = max(tab[s[j]],i)
            ans = max(ans, j-i+1)
            tab[s[j]] = j+1
        return ans
                
                
    
        
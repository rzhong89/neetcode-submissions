class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxFreq = 0
        window = defaultdict(int)
        res = 0

        for r in range(len(s)):
            window[s[r]] += 1
            maxFreq = max(maxFreq, window[s[r]])

            while r - l + 1 - maxFreq > k:
                window[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        charSet = set()
        res = 0

        for r in s:
            while r in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(r)
            res = max(res, len(charSet))

        return res


            


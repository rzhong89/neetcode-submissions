class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = Counter(t)
        window = defaultdict(int)
        
        have = 0
        need = len(tMap)
        
        left = 0
        res = ""
        resLength = float('inf')

        for r in range(len(s)):
            if s[r] in tMap:
                window[s[r]] += 1

                if window[s[r]] == tMap[s[r]]:
                    have += 1
            
            while have == need:
                if r - left + 1 < resLength:
                    res = s[left: r + 1]
                    resLength = r - left + 1
                
                if s[left] in tMap:
                    if window[s[left]] == tMap[s[left]]:
                        have -= 1
                    window[s[left]] -= 1

                left += 1
        
        return res

        


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for w in strs:
            key = [0] * 26

            for c in w:
                key[ord('a') - ord(c)] += 1

            res[tuple(key)].append(w)

        return list(res.values())
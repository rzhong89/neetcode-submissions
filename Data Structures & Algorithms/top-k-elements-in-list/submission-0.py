class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqBucket = [[] for i in range(len(nums) + 1)]
        freqMap = Counter(nums)

        for n in freqMap.keys():
            freqBucket[freqMap[n]].append(n)

        res = []
        
        for i in range(len(freqBucket) - 1, -1, -1):
            for n in freqBucket[i]:
                if len(res) != k:
                    res.append(n)
                else:
                    break

        return res



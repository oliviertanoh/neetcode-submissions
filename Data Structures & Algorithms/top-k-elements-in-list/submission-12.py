class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        arr = []
        res = []

        for nb in nums :
            if nb not in counter :
                counter[nb] = 1
            else : 
                counter[nb] = counter[nb] + 1

        for nb, freq in counter.items():
            arr.append([freq, nb])
        arr.sort()

        i = len(arr)

        while len(res) < k:
            res.append(arr.pop()[1])

        return res
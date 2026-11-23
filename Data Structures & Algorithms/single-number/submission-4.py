class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = []
        for nb in nums :
            if nb not in counter :
                counter.append(nb)
            else :
                counter.remove(nb)

        return counter[0]
        
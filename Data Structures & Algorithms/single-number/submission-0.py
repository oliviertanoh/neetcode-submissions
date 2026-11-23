class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for nb in nums :
            if nb not in counter :
                counter[nb] = 1
            else :
                counter[nb] = counter[nb] + 1

        for key, value in counter.items() :
            if value == 1 :
                return key
        
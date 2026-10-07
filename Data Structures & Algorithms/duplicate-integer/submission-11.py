class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = {}

        for nb in nums :

            if nb in seen :
                return True
            else :
                seen[nb] = True

        return False
        
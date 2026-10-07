class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        
        _duplicateValue = False
        _seenValue = set()

        for i in range(0, len(nums)):

            if nums[i] in _seenValue :
                _duplicateValue = True
                break
            _seenValue.add(nums[i])

        return _duplicateValue
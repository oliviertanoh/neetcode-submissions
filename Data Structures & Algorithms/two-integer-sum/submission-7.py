class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_nums = {}
        
        for i in range (0, len(nums)):

            target_hit = target - nums[i]

            if target_hit in hash_nums :
                return [hash_nums[target_hit] ,i] 

            hash_nums[nums[i]] = i 
            
        return 
            

                    
        
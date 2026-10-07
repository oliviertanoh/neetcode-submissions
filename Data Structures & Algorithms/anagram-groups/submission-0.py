class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_ = {}

        for i in range (0, len(strs)):

            value = "".join(sorted(strs[i]))

            if value not in hash_ :
                hash_[value] = [strs[i]]
            else :
                hash_[value].append(strs[i])
            
        return list(hash_.values())
                
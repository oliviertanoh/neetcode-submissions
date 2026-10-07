class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict_s = {}
        dict_t = {}
        count = 0 

        if len(s) != len(t) : 
            return False

        for lt in s :
            dict_s[lt] = dict_s.get(lt, 0) + 1

        for lt in t :
           dict_t[lt] = dict_t.get(lt, 0) + 1
        
        for lt in s :
            
            if dict_s.get(lt) != dict_t.get(lt) :

                return False
            

        return True
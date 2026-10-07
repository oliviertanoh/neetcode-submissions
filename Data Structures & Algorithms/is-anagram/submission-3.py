class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict_s = {}
        dict_t = {}
        count = 0 

        if len(s) >= len(t) : 
            count = dict_s
        else :
            count = dict_t

        for lt in s :
            dict_s[lt] = dict_s.get(lt, 0) + 1

        for lt in t :
           dict_t[lt] = dict_t.get(lt, 0) + 1
        
        for lt in count :
            
            if lt in dict_s and lt in dict_t :

                if dict_s[lt] != dict_t[lt] :

                    return False
            else : 

                return False

        return True
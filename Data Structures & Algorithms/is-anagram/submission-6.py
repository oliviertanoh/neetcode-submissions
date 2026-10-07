class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count_t = {}
        count_s = {}
        is_anagram = False

        if len(s) != len(t) :
            return False

        for ch1 in s :
            if ch1 in count_s :
                count_s[ch1] = count_s[ch1] + 1
            else :
                count_s[ch1] = 1


        for ch2 in t : 
            if ch2 in count_t :
                count_t[ch2] = count_t[ch2] + 1
            else :
                count_t[ch2] = 1

        if count_t != count_s :
            return False

        return True

            




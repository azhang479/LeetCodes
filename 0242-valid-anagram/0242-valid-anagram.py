class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict_s = {}
        mydict_t = {}

        for char in s:
            if char in mydict_s:
                mydict_s[char] += 1
            else:
                mydict_s[char] = 1
        for char in t:
            if char in mydict_t:
                mydict_t[char] += 1
            else:
                mydict_t[char] = 1
        
        for key in mydict_t:
            if key not in mydict_s:
                return False
            if mydict_s[key] != mydict_t[key]:
                return False
        for key in mydict_s:
            if key not in mydict_t:
                return False
            if mydict_t[key] != mydict_s[key]:
                return False
        return True      
        
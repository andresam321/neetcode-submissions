class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_string = {}
        t_string = {}
        for char in s: 
            if char in s_string:
                s_string[char] += 1
            else:
                s_string[char] = 1
        for char in t:
            if char in t_string:
                t_string[char] += 1
            else:
                t_string[char] = 1
        # print(t_string)
        # print(s_string)
        return s_string == t_string
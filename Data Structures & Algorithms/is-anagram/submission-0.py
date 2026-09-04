class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = set(s)
        t_chars = set(t)
        if len(s_chars) != len(t_chars):
            return False

        for char in s_chars:
            if s.count(char) != t.count(char):
                return False
        
        return True
            
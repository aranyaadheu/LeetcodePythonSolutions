class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Make sure the strings have same lengths. 
        if len(s) != len(t):
            return False
        # Sort both strings and compare them.
        return sorted(s) == sorted(t)

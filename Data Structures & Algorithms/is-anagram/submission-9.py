class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = [0]*26

        for i in range(len(s)):
            freq[ord(s[i])- ord('a')] += 1
            freq[ord(t[i])- ord('a')] -= 1
        
        return freq == [0]*26

# freq = [0]*26 create a zero array with size of 26
# ord(char x) return ASCII integer repsentation
# chr(int x) doese the inverse



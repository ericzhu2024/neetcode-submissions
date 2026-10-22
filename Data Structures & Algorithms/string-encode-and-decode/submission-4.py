class Solution:

    def isNum(self, char: str) -> bool:
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if char in nums: return True 
        return False
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s))
            res += '#'
            res += s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            i = j + 1
            j = i + l
            res.append(s[i: j])
            i = j
        return res
    


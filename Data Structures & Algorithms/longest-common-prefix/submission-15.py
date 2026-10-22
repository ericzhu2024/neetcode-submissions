class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(len(prefix)):
            for k in range(len(strs)):
                if i >= len(strs[k]) or prefix[i] != strs[k][i]:
                    return prefix[:i]
        return prefix


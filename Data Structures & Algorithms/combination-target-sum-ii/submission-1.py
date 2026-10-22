class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, output, total):
            if total == target:
                res.append(output.copy())
                return 
            if i >= len(candidates) or total > target:
                return 
            
            output.append(candidates[i])
            total += candidates[i]
            dfs(i + 1, output, total)

            output.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, output, total - candidates[i])
        
        dfs(0, [], 0)
        return res
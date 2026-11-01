"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        created = {}

        def dfs(cur):
            if cur.val in created:
                return created[cur.val]

            new = Node(cur.val)
            created[cur.val] = new
            for n in cur.neighbors:
                new_neighbor = dfs(n)
                new.neighbors.append(new_neighbor)
            return new

        if not node:
            return None
        return dfs(node)    
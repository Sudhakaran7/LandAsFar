import numpy as np
class Solution:
    def maxDistance(self, grid) -> int:
        n = len(grid)
        q = [[i, j] for i in range(n) for j in range(n) if grid[i][j]]
        if n **2 == len(q) : return -1
        ans = -1
        while len(q) != 0 :
            deque = []
            for i, j in q:
                for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                        grid[x][y] = 1 
                        deque.append([x, y]) 
            q = deque
            ans += 1 
        return ans
val=Solution()
n=int(input())
R=n
C=n
entries = list(map(int, input().split())) 
matrix = np.array(entries).reshape(R, C)
print(val.maxDistance(matrix))

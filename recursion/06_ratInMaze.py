class Solution:
    def ratInMaze(self, maze):
        n = len(maze)
        direction = "DLRU"
        dr = [1, 0, 0, -1]
        dc = [0, -1, 1, 0]

        def isValid(row, col):
            return 0 <= row < n and 0 <= col < n and maze[row][col] == 1

        def findPath(row, col, currentPath, ans):
            if row == n - 1 and col == n - 1:
                ans.append(currentPath)
                return
            maze[row][col] = 0

            for i in range(4):
                nextRow = row + dr[i]
                nextCol = col + dc[i]

                if isValid(nextRow, nextCol):
                    findPath(nextRow, nextCol, currentPath + direction[i], ans)
            maze[row][col] = 1

        result = []
        if maze[0][0] == 1 and maze[n - 1][n - 1] == 1:
            findPath(0, 0, "", result)
        return result

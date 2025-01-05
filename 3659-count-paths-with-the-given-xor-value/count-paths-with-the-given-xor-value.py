class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[i][j][xor] = number of paths to (i,j) with XOR value xor
        dp = [[[0] * 16 for _ in range(n)] for _ in range(m)]
        
        # Initialize starting point
        dp[0][0][grid[0][0]] = 1
        
        # Fill first row
        for j in range(1, n):
            curr_xor = grid[0][j]
            for prev_xor in range(16):
                dp[0][j][prev_xor ^ curr_xor] = dp[0][j-1][prev_xor]
        
        # Fill first column
        for i in range(1, m):
            curr_xor = grid[i][0]
            for prev_xor in range(16):
                dp[i][0][prev_xor ^ curr_xor] = dp[i-1][0][prev_xor]
        
        # Fill rest of the dp table
        for i in range(1, m):
            for j in range(1, n):
                curr_xor = grid[i][j]
                for prev_xor in range(16):
                    # Add paths from left and up
                    dp[i][j][prev_xor ^ curr_xor] = (
                        dp[i][j-1][prev_xor] + dp[i-1][j][prev_xor]
                    ) % MOD
        
        return dp[m-1][n-1][k]
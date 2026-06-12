class Solution:
    def climbStairs(self, n: int) -> int:
        ### Recursive solution O(2^n):
        # def dfs(i):
        #     if i >= n:
        #         return i == n
        #     return dfs(i + 1) + dfs(i + 2)
        # return dfs(0)
        
        ### DP solution O(n):
        # if n <= 2:
        #     return n

        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-2] + dp[i-1]

        # return dp[n]

        ### Space-optimized DP solution O(n), space O(1):
        if n <= 2:
            return n
        one = 1
        two = 2
        for _ in range(3, n+1):
            temp = two
            two += one
            one = temp
        
        return two


class Solution:
    def climbStairs(self, n: int) -> int:
        ### Recursive solution O(n^n)
        # ways = 0
        # def climb(steps):
        #     nonlocal ways
        #     if steps == n:
        #         ways += 1
        #         return
        #     if steps > n:
        #         return
        #     climb(steps + 1)
        #     climb(steps + 2)
        
        # climb(0)
        # return ways
        
        ### DP solution
        if n <= 2:
            return n

        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n]

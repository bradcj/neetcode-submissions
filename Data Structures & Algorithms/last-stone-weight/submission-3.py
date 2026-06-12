class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        m = max(stones)
        bucket = [0] * (m+1)
        for w in stones:
            bucket[w] += 1
        x = None
        i = m
        while i > 0:
            if x and bucket[i] > 0:
                y = i
                bucket[x] -= 1
                bucket[y] -= 1
                bucket[x - y] += 1
                i = max(i, x - y)
                x = None
            else:
                bucket[i] %= 2
                if bucket[i] > 0:
                    x = i
                i -= 1

        return x if x else 0

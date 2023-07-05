from typing import List


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        ans = []
        primes = [1 for _ in range(n + 1)]
        primes[0] = 0
        primes[1] = 0
        p = 2

        # Sieve of Eratosthenes algorith used to find all primes less than n
        while p ** 2 <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = 0
            p += 1

        p, r = 2, n + 1
        while p < r:
            if primes[p] and primes[n - p]:
                ans.append([p, n - p])
                # not repeating the same pair
                r = n - p
            p += 1
        return ans


solution = Solution()
n = 10
print(solution.findPrimePairs(n))

from typing import List
from collections import defaultdict

# class Solution:
#     def numMatchingSubseq(self, s: str, words: List[str]) -> int:
#         dist = {}
#         for word in words:
#             if word in dist:
#                 dist[word] += 1
#             else:
#                 dist[word] = 1
#         ans = 0
#
#         for word, count in dist.items():
#             i, j = 0, 0
#             while i < len(s) and j < len(word):
#                 if s[i] == word[j]:
#                     j += 1
#                 i += 1
#             if j == len(word):
#                 ans += count
#         return ans



# 2nd solution
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        d = defaultdict(list)
        for w in words:
            d[next(it := iter(w))].append(it)
        for c in S:
            for it in d.pop(c, []):
                if (k := next(it, None)):
                    d[k].append(it)
        return len(words) - sum(len(v) for v in d.values())



sol = Solution()
print(sol.numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))

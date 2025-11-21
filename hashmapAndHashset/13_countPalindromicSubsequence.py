# 1930. Unique Length-3 Palindromic Subsequences
from collections import defaultdict
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        mp = defaultdict(list)
        for idx, ch in enumerate(s):
            mp[ch].append(idx)
        ans = 0
        for key, val in mp.items():
            first = val[0]
            last = val[-1]
            seen = set()
            for i in range(first+1, last):
                if s[i] not in seen:
                    ans += 1
                    seen.add(s[i])
        return ans
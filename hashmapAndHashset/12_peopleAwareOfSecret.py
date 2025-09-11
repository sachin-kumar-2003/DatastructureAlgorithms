from collections import defaultdict
mod = 10 ** 9 + 7
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mp = defaultdict(int)
        mp[1] = 1
        curr = 0
        for i in range(delay + 1, n + 1):
            num = mp.get((i - delay), 0)
            curr += num
            forg = mp.get((i - forget), 0)
            curr -= forg
            mp[i] = curr
        ans = 0
        for day , val in mp.items():
            if day > n - forget:
                ans += (val) % mod
        return ans % mod

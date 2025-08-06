'''3479. Fruits Into Baskets III'''
from typing import List
class SegmentTree:
    def __init__(self, baskets: List[int]):
        self.n = len(baskets)
        self.tree = [-1] * (4 * self.n)
        self.build(0, 0, self.n - 1, baskets)

    def build(self, i: int, l: int, r: int, baskets: List[int]):
        if l == r:
            self.tree[i] = baskets[l]
            return
        mid = (l + r) // 2
        self.build(2 * i + 1, l, mid, baskets)
        self.build(2 * i + 2, mid + 1, r, baskets)
        self.tree[i] = max(self.tree[2 * i + 1], self.tree[2 * i + 2])

    def query(self, i: int, l: int, r: int, val: int) -> bool:
        if self.tree[i] < val:
            return False

        if l == r:
            self.tree[i] = -1  
            return True

        mid = (l + r) // 2
        placed = False

        if self.tree[2 * i + 1] >= val:
            placed = self.query(2 * i + 1, l, mid, val)
        else:
            placed = self.query(2 * i + 2, mid + 1, r, val)

        self.tree[i] = max(self.tree[2 * i + 1], self.tree[2 * i + 2])
        return placed


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        st = SegmentTree(baskets)
        unplaced = 0

        for fruit in fruits:
            if not st.query(0, 0, n - 1, fruit):
                unplaced += 1

        return unplaced

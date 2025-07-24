from typing import List
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        choose = []
        visited = set()
        ans = set()
        def recursion(choose , visited ):
            if len(choose) == 3:
                if choose[0] != 0 and choose[2] % 2 ==0:
                    num = choose[0] * 100 + choose[1] * 10 + choose[2]
                    ans.add(num)
                return 
            
            for i in range(len(digits)):
                if i not in visited:
                    visited.add(i)
                    recursion( choose + [digits[i]] , visited)
                    visited.remove(i)
        recursion(choose , visited )
        return len(ans)

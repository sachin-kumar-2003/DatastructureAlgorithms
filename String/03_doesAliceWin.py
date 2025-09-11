# 3227. Vowels Game in a String
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        cnt = s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')
        if cnt == 0:return False
        return True
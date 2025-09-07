# 165. Compare Version Numbers
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        vlist1 = version1.split('.')
        vlist2 = version2.split('.')
        fl = len(vlist1)
        sl = len(vlist2)

        vlist1.extend(['0'] * sl)
        vlist2.extend(['0'] * fl)
        n = len(vlist1)
        
        for a, b in zip(vlist1, vlist2):
            a = int(a)
            b = int(b)
            if a < b: return -1
            elif a > b:return 1
        return 0
        
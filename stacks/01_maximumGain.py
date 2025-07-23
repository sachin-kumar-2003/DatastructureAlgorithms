'''1717. Maximum Score From Removing Substrings'''
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            hp ="ab"
            lp = "ba"
            a= x
            b= y
        else:
            hp = "ba"
            lp = "ab"
            a = y
            b= x
        ans = 0
        stack = []
        for ch in s:
            if ch == 'a' or ch == 'b':
                if stack:
                    lc =stack[-1]
                    if lc+ch == hp:
                        ans += a
                        stack.pop()
                    else:
                        stack.append(ch)
                else:
                    stack.append(ch)
            else:
                stack.append(ch)
        stack2 = []
        s = ''.join(stack)

        for ch in s:
            if stack2:
                if stack2[-1] == 'a' or stack2[-1] == 'b':
                    lc = stack2[-1]
                    if lc+ch == lp:
                        ans += b
                        stack2.pop()
                    else:
                        stack2.append(ch)
                else:
                    stack2.append(ch)
            else:
                stack2.append(ch)

        return ans
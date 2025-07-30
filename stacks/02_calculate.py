'''224. Basic Calculator'''
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num , res , sign = [0 , 0 , 1]
        for ch in s:
            if ch.isdigit():
                num = (num * 10) + int(ch)
            elif ch == '+':
                res += (num * sign)
                num = 0
                sign = 1
            elif ch == '-':
                res += (num * sign)
                num = 0
                sign = -1
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
                num = 0
            elif ch == ')':
                res += (sign * num)
                num = 0
                lastSign = stack.pop()
                lastRes = stack.pop()
                res = (res * lastSign)
                res += lastRes
        res += (num * sign)
        return res
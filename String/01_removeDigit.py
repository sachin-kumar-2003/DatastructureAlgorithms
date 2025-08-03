'''2259. Remove Digit From Number to Maximize Result'''
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = []
        for i in range(len(number)):
            if number[i] == digit:
                strg = number[:i] + number[i+1:]
                ans.append((strg))
        return max(ans)
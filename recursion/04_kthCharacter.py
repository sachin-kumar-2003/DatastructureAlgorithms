class Solution:
  def kthCharacter(self, k: int) -> str:
    def recursion(curr,final,k):
      if len(curr)>=k:
        return curr
      temp=""
      for ch in curr:
        nextChar=chr((ord(ch)-ord('a')+1)%26+ord('a'))
        temp+=nextChar
      return recursion(curr+temp,final,k)
      
    final=""
    final=recursion("a",final,k)
    return final[k-1] 

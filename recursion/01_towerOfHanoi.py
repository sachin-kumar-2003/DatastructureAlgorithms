class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        if n==1:
            return 1
        count=self.towerOfHanoi(n-1,fromm,aux,to)
        count+=1
        count+=self.towerOfHanoi(n-1,fromm,to,aux)
        return count
        
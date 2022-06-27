class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #use the split func.
        
        sum=0
        n1=num1.split()
        n2=num2.split()
        n3=n1+n2
        for i in n3:
            sum+=int(i) #sum is an int
        return str(sum)
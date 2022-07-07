class Solution:
    def countSegments(self, s: str) -> int:
        #use split func
        #then use for loop and return count
       
        count=0
        final=s.split()
        for i in final:
            count=count+1
        return count
    
    #or you could just use len func
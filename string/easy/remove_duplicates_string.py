class Solution:
    def removeDuplicates(self, s: str) -> str:
       
    #push values into stack one by one
    #now remove all of the elements that are the same when being enterred into stack
    #if stack element is same then remove
    
        stack = []
        
        for i in s:
            if len (stack) and stack[-1]==i:  #if value in stack and value in string
                stack.pop()
            else:
                stack.append(i)

        return ''.join(stack)
    
    
    
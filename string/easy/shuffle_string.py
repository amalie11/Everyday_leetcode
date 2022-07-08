class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        #create for loop to loop through all of the indices(values)
        #then we'll store the indices in 
        
        
        
        answer=""
        for i in range(len(indices)):
            answer =answer+s[indices.index(i)]
        return answer
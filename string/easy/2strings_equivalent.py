class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
      # go through the array,using a loop then concatenate the words in the array 
    #if arrray1 and array2 == same return true
    
        string1 = ''
        string2 = ''
        for i in range(0,len(word1)):
            for char in word1[i]:
                string1 = string1 +  char
            
        for i in range(0,len(word2)):
            for char in word2[i]:
                string2 =  string2 +  char    
        
        if string1 == string2:
            return True
        else:
            return False
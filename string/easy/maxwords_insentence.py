class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
    #get num of of words using split() function
        #then get max num
       
    # res = len(str.split(''))
        #final=max(res) this is wrong.
        
        max=0
        for i in sentences:
          
          if max < len(i.split(' ')):
            max = len(i.split(' '))
        return max
 
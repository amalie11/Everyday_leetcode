class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        #use split func on only text string
        #check if the elements in text are in brokenletters
       
        
        text = text.split()
        n = len(text)
        for i in text:
            for j in brokenLetters:
                if j in i:
                    n -= 1
                    break
        return n
            


            
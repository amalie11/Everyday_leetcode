class Solution:
    def capitalizeTitle(self, title: str) -> str:
        #check 'else'
        
        title = title.split(" ")
        result = []
        for i in title:
            if len(i) == 1 or len(i) == 2:
                result.append(i.lower())
            else:
                result.append(i[0].upper()+i[1:].lower())
        return " ".join(result)
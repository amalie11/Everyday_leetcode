class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = "Hello World"

         # use -1 index to start from the end
        s = s.split()
        s = s[-1]
        return len(s)
        
class Solution:
    def balancedStringSplit(self, s: str) -> int:
    #we are going to have two pointers left and right
    #then if they meet each other we should return the amount of times theyve met
    #till you go through the whole loop
     
        bal_str = 0
        right = 0
        left = 0
        for i in range(len(s)):
            if s[i] == 'R':
                right += 1
            else:
                left += 1

            if left == right:
                bal_str += 1
        return bal_str   
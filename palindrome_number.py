class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        rev=0
        if n<0:
            return False
        else:
            while n:
                m=n%10
                rev=rev*10+m
                n//=10
            return rev==x

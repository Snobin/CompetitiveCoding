def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        
        temp=x
        x=str(x)
        temp=str(temp)[::-1]
        return temp==x
    
#Test Case
x=121
print(isPalindrome(x))

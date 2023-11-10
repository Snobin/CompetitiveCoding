def isPalindrome( s):
    first,last=0,len(s)-1
    while first<last:
        if not s[first].isalnum():
            first+=1
        elif not s[last].isalnum():
            last-=1
        elif s[first].lower()!=s[last].lower():
            return False
        else:
            first+=1
            last-=1
        return True
    
#Test Case

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
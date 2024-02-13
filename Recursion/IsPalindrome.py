# isPalindrome
# Write a recursive function called isPalindrome which returns true if the string passed to it is a palindrome (reads the same forward and backward). Otherwise it returns false.

# Examples

# isPalindrome('awesome') # false
# isPalindrome('foobar') # false
# isPalindrome('tacocat') # true
# isPalindrome('amanaplanacanalpanama') # true
# isPalindrome('amanaplanacanalpandemonium') # false



def isPalindrome(strng):
    if len(strng) ==1 or len(strng) == 0:
        return True
    if strng[0] != strng[-1]:
        return False
    return isPalindrome(strng[1:-1])
        

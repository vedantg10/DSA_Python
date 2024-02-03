# Problem Statement:  Given a number check if it is a palindrome.

# An integer is considered a palindrome when it reads the same backward as forward.

# Examples:

# Example 1:
# Input: N = 123
# Output: Not Palindrome Number
# Explanation: 123 read backwards is 321.Since these are two different numbers 123 is not a palindrome.


def palindrome(num):
    reverse_number = 0
    original_number = num
    while num!=0:
        last_digit = num%10
        reverse_number = reverse_number*10 + last_digit
        num = num//10
    if reverse_number == original_number:
        print ('Palindrome Number')
    else:
        print ('Not a Palindrome Number')


palindrome(121)
# Problem Statement: Given a number N reverse the number and print it.

# Examples:

# Example 1:
# Input: N = 123
# Output: 321
# Explanation: The reverse of 123 is 321


def reverse(num):
    reverse_number = ""
    while num !=0:
        last_digit = num%10
        reverse_number = reverse_number*10 + last_digit
        num = num//10
    return int(reverse_number)

print(reverse(124))

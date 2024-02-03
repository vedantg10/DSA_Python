# Count digits in a number
# Problem Statement: Given an integer N, write a program to count the number of digits in N.


def find_digits(num):
    count = 0
    last_digit = 0
    while num != 0:
        last_digit = last_digit + num%10
        num=num//10
        count +=1 
    return last_digit


print(find_digits(12345))

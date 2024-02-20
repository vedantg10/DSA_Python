def sumNumbers(n):
    if n<1:
        return n
    return n+sumNumbers(n-1)


print(sumNumbers(3))
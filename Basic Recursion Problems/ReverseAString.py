def reverse(strng):
    if len(strng) == 0:
        return ""
    return str(strng[-1]) + reverse(strng[:-1])


print(reverse([1,2,3,4,5,6]))
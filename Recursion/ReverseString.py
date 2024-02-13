
# reverse
# Write a recursive function called reverse which accepts a string and returns a new string in reverse.

# Examples

# reverse('python') # 'nohtyp'
# reverse('appmillers') # 'srellimppa'



def reverse(strng):
    if len(strng) <1:
        return strng
    else:
        last_char = strng[-1]
        return (last_char + reverse(strng[:-1]))
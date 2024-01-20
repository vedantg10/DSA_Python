my_dict = {'a': 5, 'b': 9, 'c': 2}
def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)


max_value_key(my_dict)
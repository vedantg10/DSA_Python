
newTuple = ('a', 'b', 'c', 'd', 'e')

print('a' in newTuple)
print('f' in newTuple)

print(newTuple.index('c'))

def seachTuple(p_tuple, element):
    for i in range(len(p_tuple)):
        if p_tuple[i] == element:
            return f'the {element} is found at {i}'
    return 'The element is not found'

print(seachTuple(newTuple, 'b'))
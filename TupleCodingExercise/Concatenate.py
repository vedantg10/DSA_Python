
# Concatenate
# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

# Example

# input_tuple = ('Hello', 'World', 'from', 'Python')
# output_string = concatenate_strings(input_tuple)
# print(output_string)  # Expected output: 'Hello World from Python'

def concatenate_strings(input_tuple):
    output_string = ''
    for word in input_tuple:
        if word == input_tuple[-1]:
            output_string = output_string + word
        else:
            output_string = output_string + word + ' '
    return output_string


#Solution 2
def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)
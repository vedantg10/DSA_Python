
# Elementwise Sum
# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

# Example

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)  # Expected output: (5, 7, 9)

def tuple_elementwise_sum(tuple1, tuple2):
    temp_list = []
    for i in range(len(tuple1)):
        temp = tuple1[i] + tuple2[i]
        temp_list.append(temp)
    return tuple(temp_list)

print(tuple_elementwise_sum(tuple1, tuple2))



#solution 2

def tuple_elementwise_sum(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Input tuples must have the same length.")
 
    result = tuple(a + b for a, b in zip(t1, t2))
    return result
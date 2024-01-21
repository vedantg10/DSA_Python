# Sum and Product
# Write a function that calculates the sum and product of all elements in a tuple of numbers.

# Example

# input_tuple = (1, 2, 3, 4)
# sum_result, product_result = sum_product(input_tuple)
# print(sum_result, product_result)  # Expected output: 10, 24



def sum_product(input_tuple):
    t_sum = 0
    t_product = 1
    for element in input_tuple:
        t_sum = t_sum +element
        t_product = element * t_product
    return t_sum, t_product

print(sum_product((1, 2, 3, 4)))
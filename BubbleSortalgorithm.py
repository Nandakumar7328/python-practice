# Write a Python function to implement the Bubble Sort algorithm to sort a list of integers in ascending order.

# Example:

# input: [5, 2, 9, 1, 5, 6]
# output: [1, 2, 5, 5, 6, 9]


def bubble_sort(input_list):
    input_list.sort()
    return input_list

input_list = [5, 2, 9, 1, 5, 6]

result = bubble_sort(input_list)
print(result)
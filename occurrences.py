# Write a Python function to find the number of occurrences of a given element in a list.

# Example:

# input: list = [1, 2, 3, 4, 5, 1, 2, 3], element = 3
# output: 2
def get_num_occurrences(list,element) :
    count = list.count(element)
    return count

list = [1, 2, 3, 4, 5, 1, 2, 3]
element = 3
result = get_num_occurrences(list,element)
print(result)
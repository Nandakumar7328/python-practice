# Write a Python function to find the second largest number in a list of integers.

# Example:

# input: [5, 2, 9, 1, 5, 6]
# output: 6 

def get_second_largest_num(input_list):
    get_max =max(input_list)
    new_list = []
    for i in input_list:
        if i != get_max :
            new_list.append(i)
    return max(new_list)

input_list = [5, 2, 9,1, 5, 6]

result = get_second_largest_num(input_list)
print(result)
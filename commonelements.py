# Write a Python function to find the common elements between two lists.

# Example:

# input: list1 = [1, 2, 3, 4, 5], list2 = [3, 4, 5, 6, 7]
# output: [3, 4, 5]

def get_common_num(list1,list2) :
    set_1 = set(list1)
    set_2 = set(list2)
    common_element = list(set_1 & set_2) 
    return common_element

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = get_common_num(list1,list2)
def get_count_x_and_b(matrix_list,row,column) :
    result_list = []
    for i in range(row):
        for j in range(column):
            if matrix_list[i][j] == "X" or matrix_list[i][j] == "B":
                result_list.append((i,j))
    return result_list
    
def main(row,column):
    matrix_list = []
    for _ in range(row):
        temp_input = input().split()
        matrix_list.append(temp_input)
    result = get_count_x_and_b(matrix_list,row,column)
    print(result)
row = int(input())
column = int(input())

main(row,column)
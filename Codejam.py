import threading
from collections import defaultdict

def save_matrix_input():
    test_cases = int(input("Test cases -->"))
    matrix_size = int(input("Size -->"))
    array = []
    test_input = dict()
    i = 0
    t = 1
    while t < test_cases:
        while i < matrix_size:
           matrix_line = input(f"Enter the elements in {i}th row of array \n")
           i=i+1
           a=matrix_line.split(" ")
           array.append(a)
        test_input[t] = array
    return test_input


def check_latin_square(array, diag, dup_rows, dup_columns, i, j):
    length = len(array[i])
    col = defaultdict(set)
    for i in range(0, length):
        for j in range(0, length):
            if i not in dup_rows and j+1 < length and array[i][j] in array[i][j+1:]:
                dup_rows.append(i)
            if j not in dup_columns and i+1 < length and array[i][j] in array[i+1:][j]:
                dup_columns.append(j)
            if i == j:
                diag = diag + array[i][j]
        return
    return diag, dup_rows, dup_columns, i, j


#t1 = threading.Thread(target=thread_task, args=(arg1,))
#t2 = threading.Thread(target=thread_task, args=(arg1,))
test_array = save_matrix_input()
for t in test_array:
    diag, dup_rows, dup_cols, _, _ = check_latin_square(test_array[t], 0, [], [], 0, 0)


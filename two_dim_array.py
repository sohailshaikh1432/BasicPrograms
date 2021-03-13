# Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from standard input and printing them out to standard output.
# I/P -> M rows, N Cols, and M * N inputs for 2D Array.
# Logic -> create 2 dimensional array in memory to read in M rows and N cols
# O/P -> Print function to print 2 Dimensional Array in Python and print the output to the screen.


def user_input_loop(num_rows,num_columns):
    # For user input
    """

    :param num_rows: referring numbers of rows from user input
    :param num_columns: referring numbers of rows from user input
    :return:
    """
    try:
        for row_loop in range(num_rows):          # A for loop for row entries
            array_list =[]
            for column_loop in range(num_columns):  # A for loop for column entries
                array_list.append(input())
            matrix.append(array_list)
        # return user_input_loop
    except Exception as excp:
        print("Exception occured : ", excp)


def matrix_printing():
    # For printing the matrix
    for outer in range(num_rows):
        for inner in range(num_columns):
            print(matrix[outer][inner], end=" ")
        print()


if __name__ == '__main__':
    # A basic code for matrix input from user

    num_rows = int(input("Enter the number of rows:"))
    num_columns = int(input("Enter the number of columns:"))

    # Initialize matrix
    matrix = []
    print("Enter the entries rowwise:")
    print('_' * 150)
    user_input_loop(num_rows,num_columns)
    print('_' * 150)
    matrix_printing()
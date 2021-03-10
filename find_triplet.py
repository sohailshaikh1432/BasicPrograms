def find_triplets(arr, n):
    found = False
    for loop_1 in range(0, n - 2):

        for loop_2 in range(loop_1 + 1, n - 1):

            for loop_3 in range(loop_2 + 1, n):

                if arr[loop_1] + arr[loop_2] + arr[loop_3] == 0:
                    print(arr[loop_1], arr[loop_2], arr[loop_3])
                    found = True

    # If no triplet with 0 sum
    # found in array
    if (found == False):
        print(" not exist ")


if __name__ == '__main__':
    arr = [0, -1, 2, -3, 1]
    n = len(arr)
    find_triplets(arr, n)

# Cite  : https://www.geeksforgeeks.org/check-whether-two-strings-are-anagram-of-each-other/
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort


def are_anagram(str1, str2):
    try:
        """
    
        # function to check whether two strings are anagram of each other
        :param str1: user input
        :param str2: user input
        :return:
        """
        # Get lengths of both strings
        length_str_1 = str1
        length_str_2 = str2

        # If length of both strings is not same, then they cannot be anagram
        # if length_str_1 != length_str_2:
        #     return 0

        # Sort both strings
        str1 = bubble_sort(str1)
        str2 = insertion_sort(str2)

        # Compare sorted strings
        for current_index in range(0, length_str_1):
            if str1[current_index] != str2[current_index]:
                return 0
        return 1
    except Exception as excpt:
        print("Error occurred : ", excpt)


if __name__ == '__main__':

    str1 = int(input("Please enter 1'st string : "))
    str2 = int(input("Please enter 2'nd string : "))

    if are_anagram(str1, str2):
        print(f"The '{str1}' is Anagram of '{str2}' ")
    else:
        print(f"The '{str1}' is not Anagram of '{str2}' ")

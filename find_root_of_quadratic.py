import math


def root1():
    root1_val = (-b_val + math.sqrt(delta)) / (2 * a_val)
    return root1_val


def root2():
    root2_val = (-b_val - math.sqrt(delta)) / (2 * a_val)
    return root2_val


def quadratic():
    print("For root 1  X value is : ", a_val * root1() ** 2 + b_val * root1() + c_val)
    print("For root 2  X value is : ", a_val * root2() ** 2 + b_val * root2() + c_val)


if __name__ == '__main__':
    a = int(input("Enter 'a' value and a≠0 : "))
    if a != 0:
        a_val = a
    else:
        print("Please enter valid input")
        a_val = int(input("Enter 'a' value : "))
    b_val = int(input("Enter 'b' value : "))
    c_val = int(input("Enter 'c' value : "))
    delta = b_val * b_val - 4 * a_val * c_val
    print("Root 1 of X is : ", root1())
    print("Root 2 of X is : ", root2())
    quadratic()

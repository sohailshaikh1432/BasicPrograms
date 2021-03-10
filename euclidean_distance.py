import math


def euclidean_distance():
    """
    Euclidean distance from the point (A, B) to the origin (0, 0),
    point 'A' is origin which x,y-axis value is (0,0) and point 'B' is which x,y-axis value is user define
    """
    euclidean_distance_result = math.sqrt((x_axis_val - 0) ** 2 + (y_axis_val - 0) ** 2)
    return euclidean_distance_result


if __name__ == '__main__':
    x_axis_val = int(input("Enter 'X' axis value of point 'B' : "))
    y_axis_val = int(input("Enter 'Y' axis value of point 'B' : "))
    euclidean_distance()
    print(euclidean_distance())

def main():
    year = int(input("Enter Year : "))

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is Leap Year".format(year))
            else:
                print("{0} is not a Leap Year".format(year))
        else:
            print("{0} is Leap Year".format(year))
    else:
        print("{0} is not a Leap Year".format(year))

if __name__ == '__main__':
    main()
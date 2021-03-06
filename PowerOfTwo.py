def main():

    n = int(input("Enter number : "))

    if n<31:
        for x in range(n):
            power = 2 ** x
            print("Power 2^", x, " is :", power)
    else:
        print("Power of 2^", n, " is :", 1)

if __name__ == '__main__':
    main()
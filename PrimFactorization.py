def main():
    # Python Program to find Prime Factors of a number

    number = int(input(" Please Enter any number: "))

    for i in range(2, number + 1):
        if number % i == 0:
            is_prime = 1
            for j in range(2, (i // 2 + 1)):
                if i % j == 0:
                    is_prime = 0
                    break

            if is_prime == 1:
                print(" %d is a Prime Factor of a Given number %d" % (i, number))


if __name__ == '__main__':
    main()

# todo
Exception handling
create method
maintain doc string
creating branch on Git
format string
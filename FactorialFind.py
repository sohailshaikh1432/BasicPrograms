def main():
    # declaring vairiables
    input = userInput
    fact = 1
    #!For loop to find factorial of given input
    for i in range(1, input+1):
        fact= fact*i
    print("Factorial of ", input ," is :", fact)


if __name__ == "__main__":
    # Taking input from the user
    userInput = int(input("Enter number : "))
    main()
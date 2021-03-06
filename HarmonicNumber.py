def main():

    num = int(input("Enter number : "))
    harmoic_num = 1
    i = 1
    for i in range(1,num+1):
        harmoic_num = harmoic_num + 1 / i
        print("Harmonic number is :", harmoic_num)
if __name__ == '__main__':
    main()


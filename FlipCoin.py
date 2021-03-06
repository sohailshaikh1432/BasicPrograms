def main():
    import random

    num_head, num_tail, total_flip = 0, 0, 0

    for y in range(10):
        x = random.random()
        if x < 0.5:
            num_tail += 1
            print("Tail")
        else:
            num_head += 1
            print("Head")

    total_flip = num_head + num_tail

    print("number of Heads", num_head * 100 / total_flip)
    print("number of Tails", num_tail * 100 / total_flip)

if __name__ == '__main__':
    main()
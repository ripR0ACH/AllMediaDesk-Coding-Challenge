# name: Zachary Morrison


def peters_number(num, ind, last, test):
    l = len(num)
    if (ind == l):
        if test <= int(num): return test
        return 0
    else:
        dig = 9
        while dig >= last:
            n = test * 10 + dig
            result = peters_number(num, ind + 1, dig, n)
            if result and result > 0: return result
            dig -= 1

def main():
    num = input("Input a number: ")
    peter = peters_number(num, 0, 0, 0)
    print(peter)


if __name__ == "__main__":
    main()
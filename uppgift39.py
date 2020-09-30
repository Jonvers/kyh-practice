def highest_number(a, b, c):
    biggest_number = a
    if biggest_number < b:
        biggest_number = b
    if biggest_number < c:
        biggest_number = c
    return biggest_number


def add_list(num_list):
    summed_list = 0
    for num in num_list:
        summed_list += num

    return summed_list


def multiply_list(num_list):
    summed_list = 1
    for num in num_list:
        summed_list *= num

    return summed_list


def main():
    print(highest_number(5, 4, 3))
    print(add_list([1, 2, 3, 4]))
    print(multiply_list([1, 2, 3, 4]))


if __name__ == '__main__':
    main()

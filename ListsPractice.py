def is_it_too_long(name, number):
    return len(name) > number


def main():
    try:
        number = int(input("Hur långt får namnet vara?"))

    except ValueError:
        print("Olagligt nummer, sätter den tillåtna längden till 5")
        number = 5

    students = input("Skriv personernas namn").split(',')

    for name in students:
        if is_it_too_long(name, number):
            print(f"{name.title()} är för långt!")


if __name__ == '__main__':
    main()

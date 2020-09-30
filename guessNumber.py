from random import randint

n = randint(1, 100)
print("Jag tänker på ett nummer mellan 1 och 100. Gissa vilken?")


def ask_number():
    return int(input("Gissa nummmer"))


def mainloop():
    user_guess = 0
    while True:
        text = ask_number()
        as_number = int(text)
        user_guess = user_guess + 1

        if as_number == n:
            print("Korrekt!")
            return user_guess

        if as_number < n:
            print("Fel, mitt nummer är högre... Försök igen!")

        if as_number > n:
            print("Fel, mitt nummer är lägre... Försök igen!")


guess = str(mainloop())
print(f"Du har gissat {guess} gånger")

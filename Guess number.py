import random


n = random.randint(1, 100)
print("Jag tänker på ett nummer mellan 1 och 100. Gissa vilken?")

def ask_number():
    return int(input("Gissa nummmer"))


def mainloop():
    guess = 0
    while True:
        text = ask_number()
        as_number = int(text)
        guess = guess + 1

        if as_number == n:
            print("Korrekt!")
            return guess

        if as_number < n:
            print("Fel, mitt nummer är högre... Försök igen!")

        if as_number > n:
            print("Fel, mitt nummer är lägre... Försök igen!")

guess = str(mainloop())
print("Du har gissat " + guess + " gånger")
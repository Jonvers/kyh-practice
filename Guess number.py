import random

n = random.randint(1, 100)
print("Jag tänker på ett nummer mellan 1 och 100. Gissa vilken?")

guess = 0
while True:
    text = input("Din gissning: ")
    as_number = int(text)
    guess = guess + 1

    if as_number == n:
        print("Korrekt! Du har gjort " + str(guess) + " gissningar")
        break

    if as_number < n:
        print("Fel, mitt nummer är högre... Försök igen!")

    if as_number > n:
        print("Fel, mitt nummer är lägre... Försök igen!")
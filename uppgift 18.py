

def main():
    people = {
    "Fredrik": "0702778511",
    "Olof": "123456789",
    "Lisa": "9999999999",
    "Bodil": "555-666-789"
    }


    menu_number = input("1:Slå upp ett nummer\n2:Lägga till ett nummer")
    if(menu_number == "1"):
        vem = input(f"Det finns {len(people)} personer i Katalogen\nVem vill du ringa?")
        if vem not in people:
           print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
        else:
            number = people[vem]
            print(f"Numret till {vem} är {number}")

    elif menu_number == "2":
        name = input("Namn:")
        people[name] = input("Telefonnummer")
        print(people)

if __name__ == '__main__':
    main()
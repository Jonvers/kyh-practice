import random

def game():
    correct_answers = 0

    for i in range(3):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        while(True):
            try:
                answer = input(f"{a} + {b}")
                number = int(answer)
                break;
            except:
                print("Not a number, try again")

        if number == a + b:
            print("Rätt!")
            correct_answers += 1

        else:
            print(f"Fel... Det blir {a+b}")
            print("---")
    print(f"Du fick {correct_answers} av 3 rätt.")
if __name__ == '__main__':
    game()
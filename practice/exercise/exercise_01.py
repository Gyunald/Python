import random

def guessing_game():
    count = 1
    number = random.randint(0,10)
    while s := float(input("숫자를 맞춰보세요.")):
        if count == 3 :
            print("game over")
            break
        if s == number :
            print("Just right")
            break
        elif s > number :
            count += 1
            print("Too high")
        elif s < number :
            count += 1
            print("Too low")
if __name__ == "__main__" :
    guessing_game()
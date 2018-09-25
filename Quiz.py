import random

print("Welcome to Guess the number Game ! ")
RandomNumber = random.randint(0, 50)


while True:
    UserInput = int(input("Try to guess the number between 0 - 50 : "))
    if UserInput == RandomNumber:
        print("Congratulations the number was", +RandomNumber)
        break
    elif UserInput > RandomNumber:
        print("Too big")
    elif UserInput < RandomNumber:
        print("too small")
    3
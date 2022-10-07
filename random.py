import random
num=random.randrange(1,10)
guess=int(input("Enter the guessing number:"))
while num!=guess:
    if guess<num:
        print("youser guess Too low...")
        guess = int(input("Enter the guessing number"))
    elif guess>num:
        print("youser guess Too high...")
        guess = int(input("Enter the guessing number"))
    else:
        break
print("you guess correct number")



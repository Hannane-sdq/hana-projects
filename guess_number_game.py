import random
print("Welcome to my [guess number] game! \nAre you ready to start?")
a=input("yes/no \n")
if a=="yes":
    b=True
elif a=="no":
    b=False
    print("goodbye. See you later!")

while b:
    i=0
    b2=True
    num=random.randint(1,100)
    guess=int(input("Write your guess:"))
    while b2: 
        i+=1
        if guess>num:
            print("number is smaller than yor guess \n try again")
            guess=int(input("Write your guess:"))
        elif guess<num:
            print("number is bigger than yor guess \n try again")
            guess=int(input("Write your guess:"))
        else: 
            b=False
            b2=False
            print(f"\n Brovo! the number was={num} \n count of your try={i}\n")
            print("do you want play again?")
            a=input("yes/no \n")
            if a=="yes":
                b=True
            elif a=="no":
                b=False
                print("goodbye. See you later!")
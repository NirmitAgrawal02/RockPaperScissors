import random
import time

while True:
    n = input("Do you want to play Rock Paper Scissors\n1. Yes\n0.Exit\n")
    if n == 0:
        print("Hope You Enjoyed Your Stay! GoodBye")
        break
    variables = ["Rock", "Paper", "Scissor"]
    print(variables)
    user_input = input("Enter Your Choice\n")
    bot = random.choice(variables)
    if user_input == bot:
        print('-'*30)
        print(f"Both players selected {user_input}. It's a tie!")
        print('-'*30)
    else:
        if user_input == "Rock":
            if bot == "Scissor":
                print("Rock Beat Scissor")
                print('-'*30)
                print("User Won")
                print('-'*30)
            else:
                print("Paper Beat Rock")
                print('-'*30)
                print("User Lost")
                print('-'*30)
        elif (user_input == "Paper"):
            if bot == "Rock":
                print("Paper Beat Rock")
                print('-'*30)
                print("User Lost")
                print('-'*30)
            else:
                print("Scissor Beat paper")
                print('-'*30)
                print("User Won")
                print('-'*30)
        else:
            if bot == "Rock":
                print("Rock Beat Scissor")
                print('-'*30)
                print("User Won")
                print('-'*30)
            else:
                print("Scissor Beat paper")
                print('-'*30)
                print("User Lost")
                print('-'*30)
    time.sleep(1)

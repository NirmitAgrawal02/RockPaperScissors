import random
import time
import tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Rock Paper Scissors Game")

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

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
        USER_SCORE += 0.5
        COMP_SCORE += 0.5
    else:
        if user_input == "Rock":
            if bot == "Scissor":
                print("Rock Beat Scissor")
                print('-'*30)
                print("User Won")
                print('-'*30)
                USER_SCORE += 1
            else:
                print("Paper Beat Rock")
                print('-'*30)
                print("User Lost")
                print('-'*30)
                COMP_SCORE += 1
        elif (user_input == "Paper"):
            if bot == "Rock":
                print("Paper Beat Rock")
                print('-'*30)
                print("User Lost")
                print('-'*30)
                COMP_SCORE = COMP_SCORE + 1
            else:
                print("Scissor Beat paper")
                print('-'*30)
                print("User Won")
                print('-'*30)
                USER_SCORE = USER_SCORE + 1
        else:
            if bot == "Rock":
                print("Rock Beat Scissor")
                print('-'*30)
                print("User Won")
                print('-'*30)
                USER_SCORE = USER_SCORE + 1
            else:
                print("Scissor Beat paper")
                print('-'*30)
                print("User Lost")
                print('-'*30)
                COMP_SCORE = COMP_SCORE + 1
    time.sleep(1)

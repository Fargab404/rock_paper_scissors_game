import random
from datetime import datetime
import os

values = [1, 0, -1]
win,lose,tie = 0,0,0
"""
rock = 1
paper = 0
scissors = -1
"""

print("Welcome to my Rock paper scissors game....")
def play_game():
    global win, tie, lose
    computer=random.choice(values)
    item = {1 : "rock", 0 : "paper", -1 : "scissors"}
    print("Choose Rock for 1\nPaper for 0\nscissors for -1\n")
    while True:
        try:
            user = int(input("Your choice is: "))
            if user not in [1, 0, -1]:
                print("Invalid choice! Please choose 1, 0, or -1.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a number (1, 0, or -1).")
            continue
        
    print(f"\nYou chose {item[user]}\nand Computer chose {item[computer]}")
    if(computer==user):
            print("Its DRAW!!")
            tie +=1
    elif(computer==1 and user==0):
            win+=1
            print("You Win!")
    elif(computer==1 and user==-1):
            lose+=1
            print("You lose!")
    elif(computer==0 and user ==1):
            lose+=1
            print("You lose!")
    elif(computer==0 and user==-1):
            win+=1
            print("You Won!")
    elif(computer==-1 and user==0):
            lose+=1
            print("You lose!")
    elif(computer==-1 and user == 1):
            win+=1
            print("You Won!")
    else:
            print("Wrong!")

def save_score():
    if win == 0 and lose == 0 and tie == 0:
        print("No scores to save. Play the game first!")
        return
    try: 
        with open ("rockpapergamescore.txt", "a") as f:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{now}] Number of win: {str(win)} and Number of lose: {str(lose)} and Number of tie: {str(tie)}\n")
    except FileNotFoundError:
        print("You haven't play the game yet, please play the game first then you are free to save the file")
def view_scores():
    try:
        #to print the data
        with open("rockpapergamescore.txt") as f:
            data = f.readlines()
            if data:
                print("\nYour Wines and loses:")
                for idx, line in enumerate(data, start=1):
                    print(f"{idx}. {line.strip()}")
            else:
                print("No scores to display.")
    except FileNotFoundError:
        print("You haven't play the game yet, please play the game first.")

def delete_scores():
    try:
        os.remove("rockpapergamescore.txt")
    except FileNotFoundError:
           print("File not found!")         
       
# Initialize scores

print("Welcome to my Rock, Paper, Scissors game!")
while True:
    choice = input("\nType:\n'p' to Play\n'save' to Save Score\n's' to View Scores\n'd' to Delete Scores\n'q' to Quit\n").lower()

    if choice == "p":
        play_game()
    elif choice == "save":
        save_score()
        win, tie, lose = 0, 0, 0  # Reset scores after saving
    elif choice == "s":
        view_scores()
    elif choice == "d":
        delete_scores()
    elif choice == "q":
        print("We hope you come soon,Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please try again.")
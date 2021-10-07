from random import randint
import time

playOptions = ["Stone" , "Paper" , "Scissors"]
computer = playOptions[randint(0, 2)]

player = False

while True :
    player = input("Stone, Paper, Scissors : ")

    if computer == player:
        print(f"Computer choosed {computer}")
        time.sleep(2)
        print("Tie!")
    
    elif player == "Stone" :
        if computer == "Paper" :
            print(f"Computer choosed {computer}")
            time.sleep(2)
            print(f"You lose! {computer} covers {player}")
        else :
            print(f"Computer choosed {computer}")
            time.sleep(2)
            print(f"You win! {player} smashes {computer}")
    elif player == "Paper" :
        if computer == "Scissors" :
            print(f"Compuert choosed {computer}")
            time.sleep(2)
            print(f"You lose... {computer} cuts {player}")
        else :
            print(f"Computer choosed {computer}")
            time.sleep(2)
            print(f"You win!! {player} covers {computer}")
    elif player == "Scissors" :
        if computer == "Stone" :
            print(f"Compuert choosed {computer}")
            time.sleep(2)
            print(f"You lose... {computer} smashes {player}")
        else :
            print(f"Computer choosed {computer}")
            time.sleep(2)
            print(f"You win! {player} cuts {computer}")
    else :
        print("The choice you have enter does not match the given ones... Pls try again")

    computer = playOptions[randint(0, 2)]


#cut
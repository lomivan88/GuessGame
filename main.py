import guessing_game, os
import random as rd

run = True
while run:
    os.system("cls")
    logo = guessing_game.logo
    max_turns = 0
    guessed_number = rd.randint(1, 100)
    player_tip = 0

    print(logo)
    print("Welcome in the game Guess the number! Beat the computer!\nGuess the number between 1 and 100.")
    difficulty = input("Choose difficulty (easy/hard): ")

    if difficulty == "hard":
        max_turns = 5
    else:
        max_turns = 10

    game_over = True

    for i in range(max_turns):
        print(f"Remaining turns {max_turns - i}. ")
        player_tip = int(input("Try guess the number: "))
        if player_tip == guessed_number:
            print(f"Good job! You beat the computer and you need {i + 1} turns.")
            game_over = False
            break
        elif player_tip < guessed_number and player_tip > 0:
            print(f"Low guess!")
        elif player_tip > guessed_number and player_tip <= 100:
            print(f"High guess!")
        else:
            print("You are out of range! Choose number between 1 and 100!")

    if game_over:
        print("Game over, to much guesses!")

    again = input("Do you want to run again? (yes/no)")

    if again.lower() != "yes":
        run = False

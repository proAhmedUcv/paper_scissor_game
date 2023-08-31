  
# 1. Start the game.
# 2. Set the number of available attempts (e.g., six attempts) and initialize the count of completed attempts to zero.(Set attempts = 6, completed_attempts = 0.
# )
# 3. Repeat the following steps until reaching the maximum number of attempts or the game ends:
#    - Prompt the player to enter their choice (rock, paper, or scissors) through the user interface.
#    - Generate a random choice for the computer.
#    - Display the player's choice and the computer's choice.
#    - Compare the choices to determine the winner or a tie.
#    - Print the final result (winner or tie).
#    - Increment the count of completed attempts.
# 4. If the game ends due to reaching the maximum number of attempts, print a message indicating that the game is over ( "Game over! You have used all your attempts.").
# 5. End the game.
 



import random

def play_game(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

def main():
    print("Welcome to Rock-Paper-Scissors game!")
    print("Enter your choice: rock, paper, or scissors")

    attempts = 6
    while attempts > 0:
        player_choice = input().lower()

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        play_game(player_choice)
        attempts -= 1

        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")
        else:
            print("Game over! You have used all your attempts.")

if __name__ == "__main__":
    main()
import random

def get_user_choice():
    user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").capitalize()
    return user_choice

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        print("\nRound", rounds + 1)
        print("User Score:", user_score)
        print("Computer Score:", computer_score)

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("User chose:", user_choice)
        print("Computer chose:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "Computer" in result:
            computer_score += 1

        rounds += 1

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nFinal Scores:")
    print("User Score:", user_score)
    print("Computer Score:", computer_score)
    print("Thank you for playing!")

# Run the game
play_game()

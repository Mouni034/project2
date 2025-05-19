import random
import time

def play_number_guessing_game():
    """Plays multiple rounds of a number guessing game with difficulty, timer, hints, and high score."""

    print("Welcome to the Number Guessing Game!")
    print("I will think of a number between 1 and 100.")
    print("Try to guess it!")
    print("\nGame Rules:")
    print("- You need to guess a number that I have randomly selected.")
    print("- You can choose the difficulty level, which determines the number of attempts you get.")
    print("- After each guess, I will tell you if my number is higher or lower than your guess.")
    print("- You can ask for a hint if you are stuck (costs one attempt).")
    print("- The game ends when you guess the correct number or run out of chances.")

    high_score = {"easy": float('inf'), "medium": float('inf'), "hard": float('inf')}

    while True:
        while True:
            difficulty = input("\nChoose your difficulty level (easy, medium, hard): ").lower()
            if difficulty in ["easy", "medium", "hard"]:
                break
            else:
                print("Invalid difficulty level. Please choose from easy, medium, or hard.")

        if difficulty == "easy":
            attempts_limit = 10
        elif difficulty == "medium":
            attempts_limit = 7
        else:  # hard
            attempts_limit = 5

        secret_number = random.randint(1, 100)
        attempts_taken = 0
        start_time = time.time()
        hint_used = False

        print(f"\nYou have {attempts_limit} attempts for {difficulty} difficulty.")

        while attempts_taken < attempts_limit:
            try:
                action = input("Make a guess or type 'hint' for a clue: ").lower()

                if action == "hint":
                    if not hint_used:
                        if secret_number % 2 == 0:
                            print("Hint: The number is even.")
                        else:
                            print("Hint: The number is odd.")
                        attempts_taken += 1
                        hint_used = True
                        if attempts_taken < attempts_limit:
                            print(f"You have {attempts_limit - attempts_taken} attempts remaining.")
                        else:
                            print(f"\nYou ran out of attempts. The number I was thinking of was {secret_number}.")
                            break
                    else:
                        print("You have already used the hint in this round.")
                    continue

                guess = int(action)
                attempts_taken += 1

                if guess < 1 or guess > 100:
                    print("Your guess must be between 1 and 100.")
                    continue

                if guess == secret_number:
                    end_time = time.time()
                    time_taken = round(end_time - start_time, 2)
                    print(f"\nCongratulations! You guessed the number {secret_number} in {attempts_taken} attempts.")
                    print(f"Time taken: {time_taken} seconds.")

                    if attempts_taken < high_score[difficulty]:
                        high_score[difficulty] = attempts_taken
                        print(f"New high score for {difficulty} difficulty: {high_score[difficulty]} attempts!")
                    else:
                        print(f"Your best score for {difficulty} difficulty is {high_score[difficulty]} attempts.")
                    break
                elif guess < secret_number:
                    print("Too low. Try again.")
                else:
                    print("Too high. Try again.")

                if attempts_taken < attempts_limit:
                    print(f"You have {attempts_limit - attempts_taken} attempts remaining.")
                else:
                    print(f"\nYou ran out of attempts. The number I was thinking of was {secret_number}.")

            except ValueError:
                print("Invalid input. Please enter a whole number or 'hint'.")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    play_number_guessing_game()

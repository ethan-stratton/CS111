import random

def catch_error(x):
    if not isinstance(x, int):
        raise ValueError("You put in a non-integer.")

def run_game():
    print("Number Guessing Game: ")
    user_range = input("What is the highest number you'd like to play with? ")
    try:
        catch_error(int(user_range))
    except Exception:
        raise ValueError("You put in a non-integer. Shame on you.")
    
    random_number = random.randrange(1, user_range + 1)
    user_guess = 0
    counter = 0
    
    while user_guess != random_number:
        
        user_guess = int(input("What's your guess? "))
        try:
            catch_error(int(user_guess))
        except Exception:
            raise ValueError("You put in a non-integer. Shame on you.")


        if user_guess > random_number:
            print("Too high")
            counter +=1
        elif int(user_guess) < random_number:
            print("Too low")
            counter +=1
        else:
            print("You won!")
            print(f"total amount of guesses: {counter}")
            break
    play_again = input("Would you like to play again? ")
    if play_again.lower() == "yes" or play_again.lower() == "y":
        run_game()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    """
    Range Customization: Allow the user to customize the range of numbers."""
    run_game()

    
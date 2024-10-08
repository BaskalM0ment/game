import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    
    # The random number
    number_to_guess = random.randint(1, 100)
    
    # Initialize variables
    attempts = 0
    guessed = False
    
    while not guessed:
        user_guess = input("Enter your guess: ")
        
        # Check if the input is a number
        if user_guess.isdigit():
            user_guess = int(user_guess)
            attempts += 1
            
            # Compare guess with the selected number
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the right number in {attempts} attempts!")
                guessed = True
        else:
            print("Please enter a valid number.")
    
    print("Thanks for playing!")

# Call the function to play
guess_the_number()

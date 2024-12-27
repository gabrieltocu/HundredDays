import random

print("""

 __    __                          __                                   ______                                          __                                                                       
/  \  /  |                        /  |                                 /      \                                        /  |                                                                      
$$  \ $$ | __    __  _____  ____  $$ |____    ______    ______        /$$$$$$  | __    __   ______    _______  _______ $$/  _______    ______          ______    ______   _____  ____    ______  
$$$  \$$ |/  |  /  |/     \/    \ $$      \  /      \  /      \       $$ | _$$/ /  |  /  | /      \  /       |/       |/  |/       \  /      \        /      \  /      \ /     \/    \  /      \ 
$$$$  $$ |$$ |  $$ |$$$$$$ $$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |      $$ |/    |$$ |  $$ |/$$$$$$  |/$$$$$$$//$$$$$$$/ $$ |$$$$$$$  |/$$$$$$  |      /$$$$$$  | $$$$$$  |$$$$$$ $$$$  |/$$$$$$  |
$$ $$ $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$    $$ |$$ |  $$/       $$ |$$$$ |$$ |  $$ |$$    $$ |$$      \$$      \ $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ | /    $$ |$$ | $$ | $$ |$$    $$ |
$$ |$$$$ |$$ \__$$ |$$ | $$ | $$ |$$ |__$$ |$$$$$$$$/ $$ |            $$ \__$$ |$$ \__$$ |$$$$$$$$/  $$$$$$  |$$$$$$  |$$ |$$ |  $$ |$$ \__$$ |      $$ \__$$ |/$$$$$$$ |$$ | $$ | $$ |$$$$$$$$/ 
$$ | $$$ |$$    $$/ $$ | $$ | $$ |$$    $$/ $$       |$$ |            $$    $$/ $$    $$/ $$       |/     $$//     $$/ $$ |$$ |  $$ |$$    $$ |      $$    $$ |$$    $$ |$$ | $$ | $$ |$$       |
$$/   $$/  $$$$$$/  $$/  $$/  $$/ $$$$$$$/   $$$$$$$/ $$/              $$$$$$/   $$$$$$/   $$$$$$$/ $$$$$$$/ $$$$$$$/  $$/ $$/   $$/  $$$$$$$ |       $$$$$$$ | $$$$$$$/ $$/  $$/  $$/  $$$$$$$/ 
                                                                                                                                     /  \__$$ |      /  \__$$ |                                  
                                                                                                                                     $$    $$/       $$    $$/                                   
                                                                                                                                      $$$$$$/         $$$$$$/                                    

""")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answers(user_guess, actual_answer, attempts):
    if user_guess > actual_answer:
        print("** Too high **")
        return attempts - 1
    elif user_guess < actual_answer:
        print("** Too low **")
        return attempts - 1
    else:
        print(f"You got it! The answer was {actual_answer}.")

def set_difficulty():
    if difficulty.lower() == 'easy':
        return EASY_LEVEL
    elif difficulty.lower() == 'hard':
        return HARD_LEVEL
    else:
        print("Invalid difficulty level.")
        exit()

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)

    turns = set_difficulty()
    guess = 0


    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answers(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            print(f"The number was {number}")
            break
        elif guess != number:
            print("Guess again.")

game()
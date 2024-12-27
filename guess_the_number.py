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

""")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")

if difficulty.lower() == 'easy':
    attempts = 10
elif difficulty.lower() == 'hard':
    attempts = 5
else:
    print("Invalid difficulty level.")
    exit()

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    elif guess > number:
        print("** Too high **")
    elif guess < number:
        print("** Too low **")
    attempts -= 1
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        print(f"The number was {number}")
    else:
        print("Guess again.")


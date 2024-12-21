import random
stages = [
'''
    +---+
    |   |
    O   |
    /|\\  |
/ \\  |
|
=========
''',
    '''
    +---+
    |   |
    O   |
    /|\\  |
    /    |
    |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    /|\\  |
    |
    |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    /|   |
    |
    |
    =========''',
    '''
    +---+
    |   |
    O   |
    |   |
    |
    |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
    |
    |
    |
    =========
    ''',
    '''
    +---+
    |   |
    |
    |
    |
    |
    =========
    ''',
    ]

from hangman_words import fruitsList, carsList, citiesList

## Choose a word list
print("Welcome to Hungarian Man!")

select = input("Choose a word list: Fruits, Cars or Cities? \n")

while select.lower() not in ["fruits", "cars", "cities"]:
    select = input("Choose a word list: Fruits, Cars or Cities? \n")

if select.lower() == "fruits":
    wordList = fruitsList
elif select.lower() == "cars":
    wordList = carsList
elif select.lower() == "cities":
    wordList = citiesList

# Select a random word from the list selected
chosen_word = random.choice(wordList).lower()
print("Chosen word: ", chosen_word)

# Placeholder "____"
hidden_word = "_" * len(chosen_word)
print(hidden_word)

game_over = False
correct_guesses = []
lives = 6


while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    print(stages[lives], f"You are left with {lives} lives.")
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guesses.append(guess)
        elif letter in correct_guesses:
            display += letter
        else :
            display += "_"
    print(display)


    if guess not in chosen_word:
        print("Wrong guess!")
        lives -= 1
        if lives == 0:
            game_over = True
            print("\n~~~~You lose!~~~~")

    if "_" not in display:
        game_over = True
        print("You win!")











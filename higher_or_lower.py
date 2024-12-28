import random
from tokenize import String

from data_higher_or_lower import data

LOGO = """
__  ___       __
/ / / (_)___ _/ /_  ___  _____
/ /_/ / / __ '/ __ \\/ _ \\/ ___/
/ __  / / /_/ / / / /  __/ /
/_/ ///_/\\__, /_/ /_/\\___/_/
/ /  /____/_      _____  _____
/ /   / __ \\ | /| / / _ \\/ ___/
/ /___/ /_/ / |/ |/ /  __/ /
/_____/\\____/|__/|__/\\___/_/
"""

VS = """
    _    __
    | |  / /____
    | | / / ___/
    | |/ (__  )
    |___/____(_)
"""


# Format the data for each person
def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

# Generate a random account from the game data
def generate_account():
    return random.choice(data)

# Compare the follower count of two accounts
def compare(account_a, account_b):
    if account_a["follower_count"] > account_b["follower_count"]:
        return "A"
    else:
        return "B"

score = 0
accountA = generate_account()
accountB = generate_account()

# Display the account data
def display(account_a, account_b):
    print(f"Compare A: {format_data(account_a)}")
    print(VS)
    print(f"Against B: {format_data(account_b)}")

# Display the game logo
print(LOGO)

game_over = False





# Start the game
while not game_over:

    while accountA == accountB:
        accountB = generate_account()
    display(accountA, accountB)

    guess = str(input("Who has more followers? Type 'A' or 'B': ")).upper()

    if guess == compare(accountA, accountB):
        score += 1
        print(f"Correct! Current score: {score}")
        accountA = accountB
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}")


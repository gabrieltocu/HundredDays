import random

### Beginning of the setup

def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a Draw 🐈"
    elif c_score == 0:
        return "You lose, the computer has a blackjack"
    elif u_score == 0:
        return "You win with a BlackJack 👍🙌"
    elif u_score > 21:
        return "Went over, you lose :(("
    elif c_score > 21:
        return "Opponent went over. You win :))"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You Lose"

user_cards = []
computer_cards = []
computer_score = -1
user_score = -1
is_game_over = False

for _ in range(2): # The _ is a throwaway variable. It's a common convention to use _ for throwaway variables.
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

### End of the Setup

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards are: {user_cards}")
    print(f"Dealers cards are: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
        print(f"You lose!")
    else:
        user_should_deal = input("Stand or Hit?: \n").lower()
        if user_should_deal == "hit":
            print(user_cards.append(deal_card()))
        else:
            is_game_over = True

while computer_score != 0 and computer_score <= 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

print(f"Your final hand: {user_cards}. And your final score is: {sum(user_cards)}")
print(f"Dealer's final hand: {computer_cards}. And final {sum(computer_cards)}")
compare(user_score, computer_score)
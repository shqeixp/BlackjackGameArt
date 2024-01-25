from art import logo

def main():
    print(logo)

if __name__ == "__main__":
  main()

import random

def deal_card():
    """Return a random card from the deck."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return random.choice(cards)

def calculate_score(cards):
    """Calculate the total score of a hand."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, dealer_score):
    """Compare the scores and determine the winner."""
    if user_score == dealer_score:
        return "It's a draw!"
    elif dealer_score == 0:
        return "You lose! Dealer has Blackjack."
    elif user_score == 0:
        return "You win! Blackjack!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif dealer_score > 21:
        return "Dealer went over. You win!"
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print("Welcome to Blackjack!")

    user_cards = []
    dealer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            another_card = input("Type 'y' to get another card, 'n' to pass: ")
            if another_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print(compare(user_score, dealer_score))

# Main game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()

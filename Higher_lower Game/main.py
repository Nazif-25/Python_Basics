import random
from art import logo, vs
from game_data import data
from replit import clear

score = 0
print(logo)
account_b = random.choice(data)
game_should_continue = True

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)


    def format_data(account):
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        return f"{account_name}, a {account_descr}, from {account_country}"

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


    def check_answers(guess, a_followers, b_followers):
        if a_followers > b_followers:
            return guess == "A"
        else:
            return guess == "B"


    guess = input("Who has more followers? 'A' or 'B': ").upper()
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    is_correct = check_answers(guess, a_followers, b_followers)

    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")

    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")



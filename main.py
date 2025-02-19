import art
import game_data
import random

print(art.logo)

def start_game():
    score = 0
    choose(score)

def generate_choices():
    random.shuffle(game_data.data)
    choice_list = [game_data.data[0], game_data.data[1]]
    return choice_list

def increase_score(score):
    score += 1
    print(art.logo)
    print(f"You're right!  Current score: {score}")
    choose(score)

def end_game(score):
    print(f"Sorry, that's wrong. Final score: {score}")
    exit()

def compare_choices(choice, choices, score):
    if choice == "a" and choices[0].get("follower_count") > choices[1].get("follower_count"):
        increase_score(score)
    elif choice == "b" and choices[1].get("follower_count") > choices[0].get("follower_count"):
        increase_score(score)
    else:
        end_game(score)

def choose(score):
    choices = generate_choices()
    is_valid_choice = False
    while not is_valid_choice:
        print(f"Compare A: {choices[0].get("name")}, a {choices[0].get("description")} from {choices[0].get("country")}.")
        print(art.vs)
        print(f"B: {choices[1].get("name")}, a {choices[1].get("description")} from {choices[1].get("country")}.")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if choice == "a" or choice == "b":
            is_valid_choice = True
            compare_choices(choice, choices, score)
        else:
            print("Please enter 'A' or 'B'.")

start_game()


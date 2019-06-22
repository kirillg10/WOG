import random
import score


def generate_number(diff):
    secret_number = random.randint(1, diff)
    return  secret_number


def get_guess_from_user():
    guess = int(input("Please guess the number: "))
    while guess > 5 or guess < 1:
        print("Input should be a number between 1 - 5\n")
        guess = int(input("Please guess the number: \n"))
    return guess


def compare_results(generate_number, get_guess_from_user):
    if generate_number == get_guess_from_user:
        return True
    else:
        return False


def play(difficulty):
    random_number = generate_number(difficulty)
    user_input = get_guess_from_user()

    print(random_number , user_input)
    if compare_results(random_number,user_input) == True:
        print("True")
        score.add_score(difficulty)
    else:
        print("False")



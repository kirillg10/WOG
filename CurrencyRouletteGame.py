from currency_converter import CurrencyConverter
import random
import score


def generate_number():
    num = random.randint(1, 101)
    return  num

def get_money_interval(d):
    c = CurrencyConverter()
    number = generate_number()
    print("Dollars: ", number)
    t = int(c.convert(number, "USD", "ILS"))

    (min , max) = (t - (5 - d), t +(5 - d))

    return (min , max)

def get_guess_from_user():
    number = int(input("How much do you think it's worth in ILS? "))
    return number

def play(difficulty):
    interval = get_money_interval(difficulty)
    print(interval)
    guess = get_guess_from_user()
    if guess > interval[1]:
        print("False")
    elif guess < interval[0]:
        print("False")
    else:
        print("True")
        score.add_score(difficulty)


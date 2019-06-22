import random
import time
from utils import screen_cleaner
import score


def generate_sequence(difficulty):
    l = list()
    for e in range(difficulty):
        num = random.randint(1, 101)
        l.append(num)
    return l


def get_list_from_user(difficulty):
    l = list()
    for e in range(difficulty):
        num = int(input("Please enter a number between 1-100: "))
        l.append(num)
    return l

def is_list_equal(list1, list2):
    if list1 == list2:
        return True
    else:
        return False


def play(difficulty):
    list1 = generate_sequence(difficulty)
    print(list1)
    time.sleep(0.7)
    screen_cleaner()
    list2 = get_list_from_user(difficulty)

    if is_list_equal(list1,list2) == True:
        print("True")
        score.add_score(difficulty)
    else:
        print("False")




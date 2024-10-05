from random import randint
from time import sleep
import json

def get_score() -> tuple:
    with open("status.json") as file:
        status = json.load(file)
    win = status["win"]
    fail = status["fail"]
    plays = status["plays"]

    win = win*100//plays
    fail = fail*100//plays
    return win,fail,plays

print("Start the System?(y/n)")
if input("$ ") == "n":
    print("Show user data?(y/n)")
    if input("$ ") == "y":
        win,fail,plays = get_score()
        print(f"Win% = {win}\nLose% = {fail}\nTotal Plays = {plays}")
        exit(0)
get_score()
for _ in range(1,4):
    print("initialising"+"."*_,end="\r")
    sleep(0.7)
print("I selected 2 random numbers\nYou have to guess whether the first number is high or low than the previous")

def add_score(add: bool) -> None:
    
    with open("status.json") as file:
        status = json.load(file)
    win = status["win"]
    fail = status["fail"]
    plays = status["plays"]

    if add:
        data = {
            "win": win+1,
            "fail":fail,
            "plays":plays+1 
        }
        json.dump(data,open("status.json","wt"))
    else:
        data = {
            "win": win,
            "fail":fail+1,
            "plays":plays+1 
        }
        json.dump(data,open("status.json","wt"))

while True:
    target = randint(1,100)
    via = randint(1,100)
    sleep(0.3)

    print(f"so tell me\nIs {via} high or low than the target number?")
    while True:
        try:
            user = input("$ (h/l/bingo) :")
        except ValueError:
            print("Just enter h/l/bingo")

        if user == "h":
            if via < target:
                print(f"Noice it was {via} and {target}")
                add_score(True)
                break
            else:
                print(f"You lost! it was {via} and {target}")
                add_score(False)
                break
        elif user == "l":
            if via > target:
                print(f"Noice it was {via} and {target}")
                add_score(True)
                break
            else:
                print(f"You lost! it was {via} and {target}")
                add_score(False)
                break
        elif user == "bingo":
            if via == target:
                print(f"Noice it was {via} and {target}")
                add_score(True)
            else:
                print(f"You lost! it was {via} and {target}")
                add_score(False)
                break
        else:
            print(f"MF enter valid entry")
            continue

    print("play again?(y/n)")
    try:
        if input("$ ") == "y":
            continue
        else:
            break
    except:
        print("Your punishment, i wont log your win and lost %")
        break
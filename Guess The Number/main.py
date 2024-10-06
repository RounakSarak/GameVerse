import random
import time
import random
print("Hey, I have chosen a number between 1 and 100 and you have to find it.")
print("Write any number to start. And I will start the timer from there.")
randomNum = 0
startTime = 0

while True:
    if not randomNum:
        randomNum = int(random.random() * 100)
    try:
        userNum = int(input("I guess the number is : "))
    except ValueError:
        print("Just enter a number. Restarting...")
        continue
    if not startTime:
        startTime = time.time()

    if userNum == randomNum:
        print("Hey you caught it. ")
        print("The time taken is just ",int(time.time() - startTime),"sec")
        user = input("Want to play again (Enter y to continue) : ")
        if user == "y" or user == "Y":
            randomNum = 0
            startTime = 0
            print("Ok, Restarting...")
            continue
        else:
            break
    elif userNum > randomNum:

        print("Your number is larger than mine. Try smaller number.")
        print("Time used : ",int(time.time() - startTime),"sec")
    else:
        print("Your number is smaller than mine. Try larger number.")
        print("Time used : ", int(time.time() - startTime), "sec")


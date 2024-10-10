import random
import time
import requests

# API endpoint URL (change this to your server's API endpoint)
API_URL = "http://localhost/GameVerse/api/api.php"

# Function to send the result to the server
def send_result(player_name, win_status, time_taken):
    data = {
        'player_name': player_name,
        'win_status': win_status,
        'time_taken': time_taken
    }
    try:
        response = requests.post(API_URL, data=data)
        if response.status_code == 200:
            print("Result saved successfully.")
        else:
            print("Failed to save result.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Start of the game
print("Hey, I have chosen a number between 1 and 100 and you have to find it.")
player_name = input("Enter your name: ")
print("Write any number to start. And I will start the timer from there.")

randomNum = 0
startTime = 0

while True:
    if not randomNum:
        randomNum = int(random.random() * 100)
    try:
        userNum = int(input("I guess the number is: "))
    except ValueError:
        print("Just enter a number. Restarting...")
        continue
    if not startTime:
        startTime = time.time()

    if userNum == randomNum:
        time_taken = int(time.time() - startTime)
        print("Hey you caught it.")
        print("The time taken is just", time_taken, "sec")
        
        # Send win result to the server
        send_result(player_name, win_status=1, time_taken=time_taken)
        
        user = input("Want to play again (Enter y to continue) : ")
        if user == "y" or user == "Y":
            randomNum = 0
            startTime = 0
            print("Ok, Restarting...")
            continue
        else:
            break
    elif userNum > randomNum:
        print("Your number is larger than mine. Try a smaller number.")
        print("Time used:", int(time.time() - startTime), "sec")
    else:
        print("Your number is smaller than mine. Try a larger number.")
        print("Time used:", int(time.time() - startTime), "sec")

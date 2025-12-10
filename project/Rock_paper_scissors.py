import random
while True:
    my_answer = input("Please choose an option: Rock, Paper or Scissors").strip()
    my_answer = my_answer.lower()

    if my_answer == "quit":
        print("You decided to stop playing")
        break

    if my_answer != "rock" and my_answer != "paper" and my_answer != "scissors": 
        print(f"Please choose a correct option")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"]) 
    print(f"Computer's chooses: {computer_choice}")

    if my_answer == computer_choice:
        print("You Tied")
        continue

    elif my_answer == "rock" and computer_choice == "scissors":
        print("You Won")
        break

    elif my_answer == "scissors" and computer_choice == "paper":
        print("You Won")
        break

    elif my_answer == "paper" and computer_choice == "rock":
        print("You Won")
        break
    
    else:
        print("You lose, try again")
        break
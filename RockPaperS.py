from random import choice
options = ['rock', 'paper', 'scissors']

name = input("Enter your name: ")
print(f"Hello, {name}")

rating_file = open("rating.txt", 'r')

for line in rating_file:
    name_score = line.split()
    if name_score[0] == name:
        prev_score = int(name_score[1])
        break
    else:
        prev_score = 0


curr_score = prev_score


while True:
    user_op = input()
    computer_op = choice(options)
    if user_op == "!exit":
        print("\nBye!")
        break
    elif user_op == "!rating":
        print(f"Your rating: {curr_score}")
        continue
        
        
    if user_op == computer_op:
        print(f'There is a draw ({user_op})\n')
        curr_score += 50
        continue
        
    elif user_op == "rock" or user_op == "paper" or user_op == "scissors":
        
        win_ways = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
        if win_ways[user_op] == computer_op:
            print(f'Well done. The computer chose {computer_op} and failed\n')
            curr_score += 100
            continue
        else:
            print(f'Sorry, but the computer chose {computer_op}\n')
            continue
    else:
        print("Invalid input\n") 
        continue 

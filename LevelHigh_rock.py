from random import choice

#Key win -  when their key corresponding value of other player   
winning_cases = {
    "rock": ["fire", "scissors", "snake", "human", "wolf", "sponge", "tree"], 
    "fire": ["scissors", "paper", "snake", "human", "tree", "wolf", "sponge"],
    "scissors": ["air", "tree", "paper", "snake", "human", "wolf", "sponge"],
    "snake": ["human", "wolf", "sponge", "tree", "paper", "air", "water"],
    "human": ["tree", "wolf", "sponge", "paper", "air", "water", "dragon"],
    "tree": ["wolf", "dragon", "sponge", "paper", "air", "water", "devil"],
    "wolf": ["sponge", "paper", "air", "water", "dragon", "lightning", "devil"],
    "sponge": ["paper", "air", "water", "devil", "dragon", "gun", "lightning"],
    "paper": ["air", "rock", "water", "devil", "dragon", "gun", "lightning"],
    "air": ["fire", "rock", "water", "devil", "gun", "dragon", "lightning"],
    "water": ["devil", "dragon", "rock", "fire", "scissors", "gun", "lightning"],
    "dragon": ["devil", "lightning", "fire", "rock", "scissors", "gun", "snake"],
    "devil": ["rock", "fire", "scissors", "gun", "lightning", "snakes", "human"],
    "lightning": ["gun", "scissors", "rock", "tree", "fire", "snake", "human"],
    "gun": ["rock", "tree", "fire", "scissors", "snake", "human", "wolf"]
}

options = ['rock','gun','lightning','devil','dragon','water','air','paper','sponge','wolf','tree','human','snake','scissors','fire']

name = input("Enter your name: ")
print(f"Hello, {name}")

curr_score = 0


while True:
    user_op = input("rock, gun, lightning, devil, dragon, water, air, paper, sponge, wolf, tree, human, snake, scissors, fire : !exit : !rating\n")         
    computer_op = choice(options)
    if user_op == "!exit":
        print("\nBye!")
        break
        
    elif user_op == "!rating":
        print(f"Your rating: {curr_score}")
        continue
        
    elif user_op in winning_cases.keys():
        if user_op == computer_op:
            print(f'There is a draw ({user_op})\n')
            curr_score += 50
            continue 
        
        elif computer_op in winning_cases[user_op]:
            print(f'Well done. The computer chose {computer_op} and failed\n')
            curr_score += 100
            continue
        elif user_op in winning_cases[computer_op]:
            print(f'Sorry, but the computer chose {computer_op}\n')
            continue
    else:
        print("Invalid input\n") 
        continue 

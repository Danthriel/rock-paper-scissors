from random import randrange


def beats(choice1, choice2):
    if (choice1 == "rock" and choice2 == 'scissors') or (choice1 == "scissors" and choice2 == "paper") or (choice1 == "paper" and choice2 == "rock"): 
        return True
    elif (choice1 == "rock" and choice2 == 'paper') or (choice1 == "scissors" and choice2 == "rock") or (choice1 == "paper" and choice2 == "scissors"):
        return False
    elif (choice1 == choice2):
        return "draw"
    else:
        return "invalid"
        

def comp(x):
    if x < 1:
        return "rock"
    elif 1 <= x < 2:
        return "paper"
    else:
        return "scissors"
    

print("Welcome to rock paper scissors!")
print("Choose rock, paper, or scissors to play, or write quit to quit")

while True:
    rand = randrange(0,4)
    choice = input("What do you choose?")
    if choice == "quit":
        print("See you next time!")
        break
    elif beats(comp(rand), choice) == True:
        print("Your opponent choose " + comp(rand) + "... You lose")
    elif beats(comp(rand), choice) == False:
        print("Your opponent choose " + comp(rand) + "... You win!!!")
    elif beats(comp(rand), choice) == "draw":
        print("Your opponent also chose " + comp(rand) + "... It's a draw!")
    elif beats(comp(rand), choice) == "invalid":
        print("Sorry I only understand the words paper, scissors and rock, please try again!")
    elif choice == "quit":
        break

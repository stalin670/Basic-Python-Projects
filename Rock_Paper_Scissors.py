import random

def play():
    user=input("What's your choice ? 'r' for rock, 'p' for paper, 's' for scissors : \n")
    computer = random.choice(['r','p','s'])
    
    if computer==user :
        print("It's tie!")
    
    elif is_win(user,computer):
        print("You won!")
    else :
        print("You lost!")


def is_win(player,opponent):
    # r>s , s>p , p>r
    
    if (player=='r' and opponent=='s') or (player=='s' and opponent=='p') or (player=='p' and opponent=='r'):
        return True

play()

import random    

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while feedback!='c' and low!=high:
        if low!=high:
            guess=random.randint(low,high)
        else :
            guess=high
        
        feedback=input(f'Is {guess} too low (L) , too high (H) , or correct (C)').lower()
        
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
            
    print(f'yey! The computer guessed the number, {guess} correctly!')
    
computer_guess(100)
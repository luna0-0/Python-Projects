def winner(comp,you):
    if comp==you:
        return None
    if comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False
    if comp=='p':
        if you=='r':
            return True
        elif you=='s':
            return False
    if comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False
import random
print("Rock='r' Paper='p' Scissors='s'")
print("Computer's Turn...")
rn=random.randint(1,3)
if rn==1:
    comp='r'
elif rn==2:
    comp='p'
elif rn==3:
    comp='s'
you=input("Your Turn: ")
if you!='r':
    if you!='p':
        if you!='s':
            print("Invalid choice")
            exit()
win=winner(comp,you)
print(f"Computer's choice: {comp}")
print(f"Your choice: {you}")
if win==True:
    print("You Won!:)")
elif win==False:
    print("You Lose!:(")
else:
    print("Tie!:/")
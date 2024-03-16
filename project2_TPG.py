import random
rnum=random.randint(1,100)
guess=None
c=0
while(guess!=rnum):
    guess=int(input("Guess the number: "))
    if rnum>guess:
        print("Too low")
    elif rnum<guess:
        print("Too high")
    else:
        print("Perfect")
    c+=1
print(f"You guessed the number in {c} guess")

with open('high_score.txt','r') as f:
    high_score=int(f.read())
    print("Highscore=",high_score)

if high_score>c:
    print("Congratulations! You broke the highscore.")
    with open('high_score.txt','w') as f:
        f.write(str(c))
        print("Highscore=",c)
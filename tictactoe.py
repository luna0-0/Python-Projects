def board(xState,oState):
    zero='X' if xState[0] else 'O' if oState[0] else 0
    one='X' if xState[1] else 'O' if oState[1] else 1
    two='X' if xState[2] else 'O' if oState[2] else 2
    three='X' if xState[3] else 'O' if oState[3] else 3
    four='X' if xState[4] else 'O' if oState[4] else 4
    five='X' if xState[5] else 'O' if oState[5] else 5
    six='X' if xState[6] else 'O' if oState[6] else 6
    seven='X' if xState[7] else 'O' if oState[7] else 7
    eight='X' if xState[8] else 'O' if oState[8] else 8
    print(f"  {zero}  |  {one}  |  {two}")
    print(f"-----|-----|-----")
    print(f"  {three}  |  {four}  |  {five}")
    print(f"-----|-----|-----")
    print(f"  {six}  |  {seven}  |  {eight}")

def sum(a,b,c):
    return a+b+c

def checkWin(state):
    win=[[0,3,6],[1,4,7],[2,5,8],[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6]]
    for i in win:
        if sum(state[i[0]],state[i[1]],state[i[2]])==3:
            return 0
    return 1

def checkInput(x):
    if x not in range(9):
        print("Please enter valid position.")
        return 1

def replace():
    xState=[0,0,0,0,0,0,0,0,0]
    oState=[0,0,0,0,0,0,0,0,0]
    turn=0
    board(xState,oState)
    usedPosition=[]
    process=True
    while process:
        ip=True
        if turn==0:
            while ip==True:
                try:
                    x=int(input("X's turn: "))
                except ValueError:
                    print("Please enter valid numeric value.")
                    continue
                if checkInput(x)==1:
                    ip=False
                elif x in usedPosition:
                    print("Position already occupied. Please enter another position.")
                else:
                    usedPosition.append(x)
                    xState[x]=1
                    break
            if checkWin(xState)!=1:
                print("X won!")
                break

        else:
            while ip==True:
                try:
                    o=int(input("O's turn: "))
                except ValueError:
                    print("Please enter valid numeric value.")
                    continue
                if checkInput(o)==1:
                    ip=False
                elif o in usedPosition:
                    print("Position already occupied. Please enter another position.")
                else:
                    usedPosition.append(o)
                    oState[o]=1
                    break
            if checkWin(oState)!=1:
                print("O won!")
                break
        
        board(xState,oState)
        turn=1-turn
        if len(usedPosition)==9:
            process=False
            print("Tie!")
    print("Game Over!")

if __name__=="__main__":
    play=True
    while(play==True):
        replace()
        re=input("Do you want to replay this game?(yes/no): ")
        if re.lower()=='no':
            play=False
        if re.lower()=='yes':
            play=True
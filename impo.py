
counter = 0
seccounter = 0

def num():
    global counter
    global seccounter
    board = [
    [0,0,7,0,4,0,0,0,0],
    [0,0,0,0,0,8,0,0,6],
    [0,4,1,0,0,0,9,0,0],
    [0,0,0,0,0,0,1,7,0],
    [0,0,0,0,0,6,0,0,0],
    [0,0,8,7,0,0,2,0,0],
    [3,0,0,0,0,0,0,0,0],
    [0,0,0,1,2,0,0,0,0],
    [8,6,0,0,7,6,0,0,5]
    ]
    print(board[seccounter][counter])
    counter =counter +1
    if counter == 9:
        counter = 0
        seccounter +=1

for x in range(70):
    num()

    print(counter)
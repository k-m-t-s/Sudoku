
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
   
    

num()
def row(numrow):
    row = []
    for x in range(8):
        row.append(board[numrow][x])
    return row

def column(numcolumn):
    column =[]
    for x in range(8):
        column.append(board[x][numcolumn])
    return column

def block(numblock):
    ## 123
    ## 456
    ## 789
    if numblock == 1:
        fx, fy = 0,0
    elif numblock == 2:
        fx, fy = 3,0
    elif numblock == 3:
        fx, fy = 6,0
    elif numblock == 4:
        fx, fy = 0,3
    elif numblock == 5:
        fx, fy = 3,3
    elif numblock == 6:
        fx, fy = 6,3
    elif numblock == 1:
        fx, fy = 0,6
    elif numblock == 8:
        fx, fy = 3,6
    elif numblock == 9:
        fx, fy = 6,6   
    else:
        print("ERROR ON BLOCK")
    solid = []
    for y in range(3):
        for x in range(3):
            solid.append((board[y+fy][x+fx]))
    return solid
class go():

    x= 10
    def fun(self):
        x = 20
        print(x)
    def all(self):
        x = 25
        print(x)
        self.fun()
        print(x)

    

def possibilities(x,y):
    possibility = [
        [
            [[],[]],
            [[],[]]
        ]
    ,
                  [[[],[]],[[],[]]]]      
    z = [0,1,2,3,4,5,6,7,8,9]
    for x in range(4):
        for y in range(4):
            possibility[z][y][x] = board[y][x]
            print(possibilities[x][y][z])

lists = [
    [
        [[1],[2]],
        [[3],[4]]
    ]
    ,
    [
        [[5],[6]],
        [[7],[8]]
    ]    
]
lists2 =[]
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
for z in range(2):
    lists2.append([])
    for y in range(9):
        lists2[z].append([])
        for x in range(9):
            lists2[z][y].append([])
    
for y in range (9):
    for x in range(9):
        lists2[0][y][x] = board[y][x]
for y in range (9):
    for x in range(9):
        lists2[1][y][x] = [1,2,3,4,5,6,7,8,9]

for x in range(9):
            for y in range(9):
                if board[y][x] != 0:
                    pass
for y in range(9):
    for x in range(9):
        if board[y][x] != 0:
                for xchange in range(9):
                    pass
newboard =[]
for y in range(9):
    newboard.append([])
    for x in range(9):
        newboard[y].append([])

[[[], [], [], [], [], [], [], [], []],
 [[], [], [], [], [], [], [], [], []], 
 [[], [], [], [], [], [], [], [], []], 
 [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], [], []]]
""" 
for y in range (9):
    sth = False
    for x in range(9):
        if board[y][x] != 0:
            for xchange in range(9):
                lists2[1][0][xchange].remove(7) 
            sth = True
            break
    if sth == True:
        continue
newboard =[]
for y in range(9):
    for x inr
for y in range (9):
    for x in range(9):
        if board[y][x] != 0:
            for xchange in range(9):
                if lists2[1][y][xchange] != board[y][x]:

                    

for y in range (9):
            for x in range(9):
                if board[y][x] != 0:
                    lists2[1][y][x] = [-1]  
"""
los = [
    [
    [[1,3,2],[3]],
    [[1],[2],[3],[4]]
    ]
   
]
x = los[0][0].__len__()
print(x)
print(los[1][0][0])
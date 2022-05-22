import numpy as np
lists2 =[]
board = [
    [0,9,4, 0,3,0, 1,0,0],
    [8,1,2, 7,0,0, 0,9,6],
    [3,0,0, 1,9,0, 0,0,0],

    [0,3,0, 9,0,4, 6,0,0],
    [0,0,8, 6,1,3, 0,4,9],
    [0,0,6, 2,0,0, 0,0,1],

    [4,0,3, 5,0,0, 0,0,8],
    [5,0,0, 0,2,0, 7,0,0],
    [0,6,0, 0,0,8, 4,1,5]
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
"""
for y in range(8):
    for x in range(8):
        if board[y][x] != 0:
                for xchange in range(9):
"""
for y in range(9):
    for x in range(9):
            if board[y][x] != 0:
                for xchange in range(9):
                    lists2[1][y][xchange].remove(board[y][x])
def block(self, numblock):
        # 123
        # 456
        # 789
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
            
x = 1
y = 0
for y in range(9):
    for x in range(9):
        if board[y][x] != 0:
            for ychange in range(9):
                if lists2[1][ychange][x].__contains__(board[y][x]):
                    lists2[1][ychange][x].remove(board[y][x])
for y in range (9):
            for x in range(9):
                if board[y][x] != 0:
                    lists2[1][y][x] = [-1]
fx, fy = -1,-1
def numblock(num):
    global fx
    global fy
    if num == 1:
        fx, fy = 0,0
    elif num == 2:
        fx, fy = 3,0
    elif num == 3:
        fx, fy = 6,0
    elif num == 4:
        fx, fy = 0,3
    elif num == 5:
        fx, fy = 3,3
    elif num == 6:
        fx, fy = 6,3
    elif num == 1:
        fx, fy = 0,6
    elif num == 8:
        fx, fy = 3,6
    elif num == 9:
        fx, fy = 6,6  
    else:
        print=("ERROR in block function") 
for blockno in range(1,10):
    numblock(blockno)
    for y in range(3):
        for x in range(3):
            for ychange in range(3):
                for xchange in range(3):
                    if lists2[1][ychange+fy][xchange+fx].__contains__(board[y+fy][x+fx]):
                        lists2[1][ychange+fy][xchange+fx].remove(board[y+fy][x+fx])

for y in range(9):
    for x in range(9):
        if lists2[1][y][x].__len__() == 1:
            if lists2[1][y][x] == [-1]:
                continue
            print(lists2[1][y][x])

[[[0, 9, 4, 0, 3, 0, 1, 0, 0], 
[8, 1, 2, 7, 0, 0, 0, 9, 6], 
[3, 0, 0, 1, 9, 0, 0, 0, 0], 
[0, 3, 0, 9, 0, 4, 6, 0, 0], 
[0, 0, 8, 6, 1, 3, 0, 4, 9], 
[0, 0, 6, 2, 0, 0, 0, 0, 1], 
[4, 0, 3, 5, 0, 0, 0, 0, 8], 
[5, 0, 0, 0, 2, 0, 7, 0, 0], 
[0, 6, 0, 0, 0, 8, 4, 1, 5]],

 [[[6, 7], [-1], [-1], [8], [-1], [2, 5, 6], [-1], [2, 5, 7, 8], [2, 7]], 
 [[-1], [-1], [-1], [-1], [4, 5], [5], [3, 5], [-1], [-1]], 
 [[-1], [5, 7], [5, 7], [-1], [-1], [2, 5, 6], [2, 5, 8], [2, 5, 7, 8], [2, 4, 7]], 
 [[1, 2, 7], [-1], [1, 5, 7], [-1], [5, 7, 8], [-1], [-1], [2, 5, 7, 8], [2, 7]], 
 [[2, 7], [2, 5, 7], [-1], [-1], [-1], [-1], [2, 5], [-1], [-1]], 
 [[7, 9], [4, 5, 7], [-1], [-1], [5, 7, 8], [5, 7], [3, 5, 8], [3, 5, 7, 8], [-1]], 
 [[-1], [2, 7], [-1], [-1], [6, 7], [1, 6, 7, 9], [2, 9], [2, 6], [-1]], 
 [[-1], [4, 8], [1, 9], [3, 4], [-1], [1, 6, 9], [-1], [3, 6], [3]], 
 [[2, 7, 9], [-1], [7, 9], [3], [7], [-1], [-1], [-1], [-1]]]]
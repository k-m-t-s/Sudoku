import numpy as np
lists2 =[]
board = [
    [0,0,0, 0,3,0, 0,9,0],
    [7,5,0, 0,2,0, 1,0,3],
    [0,0,3, 0,0,8, 0,5,6],

    [3,0,0, 0,0,0, 0,0,0],
    [5,4,6, 0,0,0, 8,3,2],
    [8,0,0, 2,0,3, 0,0,0],

    [0,7,8, 0,5,0, 0,0,0],
    [0,3,0, 0,7,6, 5,4,0],
    [4,6,5, 0,0,0, 0,7,9]
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
    elif num == 7:
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
                    """
                    print(str(lists2[1][y][x])+" "+str(y) +" "+str(x))
                    """
for blockno in range(1,10):
    numblock(blockno)
    for y in range(3):
        for x in range(3):
            if lists2[1][y+fy][x+fx].__len__() == 1 and lists2[1][y+fy][x+fx] != [-1]:
                convertinto = 0
                for r in lists2[1][y+fy][x+fx]:
                    convertinto = r
                
                for a in range(3):
                    for b in range(3):
                        if lists2[1][fy+a][fx+b].__contains__(convertinto) and lists2[1][fy+a][fx+b].__len__() != 1:
                            lists2[1][fy+a][fx+b].remove(convertinto)
for y in range(9):
    for x in range(9):
        if lists2[1][y][x].__len__() == 1 and lists2[1][y][x] != [-1]:
                convertinto = 0
                for r in lists2[1][y][x]:
                    convertinto = r
                for ychange in range(9):
                    if lists2[1][ychange][x].__contains__(convertinto) and lists2[1][ychange][x].__len__() != 1:
                        lists2[1][ychange][x].remove(convertinto)
for y in range(9):
    for x in range(9):
        if lists2[1][y][x].__len__() == 1 and lists2[1][y][x] != [-1]:
                convertinto = 0
                for r in lists2[1][y][x]:
                    convertinto = r
                for xchange in range(9):
                    if lists2[1][y][xchange].__contains__(convertinto) and lists2[1][y][xchange].__len__() != 1:
                        lists2[1][y][xchange].remove(convertinto)             
                            



counter = 0
for blockno in range(1,10):
    miniboard =[]
    numblock(blockno)
    for y in range(3):
        for x in range(3):
            if lists2[1][y+fy][x+fx].__len__() != 1:
                for o in lists2[1][y+fy][x+fx]:
                    miniboard.append(o)
    for a in miniboard:
        if miniboard.count(a) == 1:
            for y in range(3):
                for x in range(3):
                        for b in lists2[1][y+fy][x+fx]:
                            if a == b:
                                continue
                            else:
                                if lists2[1][y+fy][x+fx].__contains__(a):
                                    lists2[1][y+fy][x+fx].remove(b)


for blockno in range(1,10):
    numblock(blockno)      
    singleLine=[]
    for y in range(3):
        for x in range(3):
            if lists2[1][y+fy][x+fx] != 0 and lists2[1][y+fy][x+fx].__len__() != 1:
                for q in lists2[1][y+fy][x+fx]:
                    singleLine.append(q)
    for q in singleLine:
        counter = 0
        for a in singleLine:
            if q == a:
                counter +=1
                if counter != 1:
                    singleLine.remove(q)
    counter = 0
    
    for q in singleLine:
        firstrow = 0
        secondrow = 0
        thirdrow = 0
        for y in range(3):
                for x in range(3):
                    if lists2[1][y+fy][x+fx] != 0 and lists2[1][y+fy][x+fx].__len__() != 1:
                        if lists2[1][y+fy][x+fx].__contains__(q):
                            if y == 0:
                                firstrow += 1
                            if y == 1:
                                secondrow += 1
                            if y == 2:
                                thirdrow += 1
        row_sum = firstrow + secondrow + thirdrow
        if row_sum < 4 and row_sum > 1:
            if (firstrow + secondrow) == 0:
                for x in range(3,9):
                    if lists2[1][2+fy][fx+x].__contains__(q):
                        lists2[1][2+fy][fx+x].remove(q)
            if (thirdrow + secondrow) == 0:
                for x in range(3,9):
                    if lists2[1][0+fy][fx+x].__contains__(q):
                        lists2[1][0+fy][fx+x].remove(q)
            if (firstrow + thirdrow) == 0:
                for x in range(3,9):
                    if lists2[1][1+fy][fx+x].__contains__(q):
                        lists2[1][1+fy][fx+x].remove(q)

for blockno in range(1,10):
    numblock(blockno)      
    singleLine=[]
    for y in range(3):
        for x in range(3):
            if lists2[1][y+fy][x+fx] != 0 and lists2[1][y+fy][x+fx].__len__() != 1:
                for q in lists2[1][y+fy][x+fx]:
                    singleLine.append(q)
    for q in singleLine:
        counter = 0
        for a in singleLine:
            if q == a:
                counter +=1
                if counter != 1:
                    singleLine.remove(q)
    counter = 0
    
    for q in singleLine:
        firstrow = 0
        secondrow = 0
        thirdrow = 0
        for y in range(3):
                for x in range(3):
                    if lists2[1][y+fy][x+fx] != 0 and lists2[1][y+fy][x+fx].__len__() != 1:
                        if lists2[1][y+fy][x+fx].__contains__(q):
                            if y == 0:
                                firstrow += 1
                            if y == 1:
                                secondrow += 1
                            if y == 2:
                                thirdrow += 1
        row_sum = firstrow + secondrow + thirdrow
        if row_sum < 4 and row_sum > 1:
            if (firstrow + secondrow) == 0:
                for x in range(3,9):
                    if lists2[1][2+fy][fx+x].__contains__(q):
                        lists2[1][2+fy][fx+x].remove(q)
            if (thirdrow + secondrow) == 0:
                for x in range(3,9):
                    if lists2[1][0+fy][fx+x].__contains__(q):
                        lists2[1][0+fy][fx+x].remove(q)
            if (firstrow + thirdrow) == 0:
                for x in range(3,9):
                    if lists2[1][1+fy][fx+x].__contains__(q):
                        lists2[1][1+fy][fx+x].remove(q)
                        
                         



"""
for a in range(3):
                        for b in range(3):
                            if lists2[1][a+fy][b+fx] != 0 and lists2[1][a+fy][b+fx].__len__() != 1:
                                if lists2[1][a+fy][b+fy].__contains__(q):
                                        insiderow += 1
                                        if nextrow == True:
                                            outsiderow +=1
                        nextrow = True
                    print("inside " + str(insiderow))
                    print("outside " + str(outsiderow)
            for o in tempo2:
                counter = 0 
                for z in tempo2:
                    if o == z:
                        counter +=1       
                if counter == 1:
                    for a in lists2[1][y+fy][x+fx]:
                        if a == i:
                            if lists2[1][y+fy][x+fx].__contains__(a) and not lists2[1][y+fy][x+fx].__len__() == 1:
                                lists2[1][y+fy][x+fx].remove(a)
                        
    

             

for y in range(9):
    for x in range(9):
                if lists2[1][y][x].__len__() == 1:
                    print("True"+" "+str(lists2[1][y][x]))
                else:
                    print("False")
"""


import numpy
print(lists2)


## remove the number from all other possy in box
## in a box if that is the only remaining number, change it
## check if it is value at the end, check x ,y , and board
[0,0,0, 0,3,0, 0,9,0],
[7,5,0, 0,2,0, 1,0,3],
[0,0,3, 0,0,8, 0,5,6],

[3,0,0, 0,0,0, 0,0,0],
[5,4,6, 0,0,0, 8,3,2],
[8,0,0, 2,0,3, 0,0,0],

[0,7,8, 0,5,0, 0,0,0],
[0,3,0, 0,7,6, 5,4,0],
[4,6,5, 0,0,0, 0,7,9]

[[6], [8], [1, 2, 4],       [1, 4, 5, 7], [-1], [1, 4, 5, 7],               [2, 4, 7], [-1], [4, 7]]
[[-1], [-1], [4, 9],              [6], [-1], [4, 9],                       [-1], [8], [-1]]
[[1, 2], [1, 2, 9], [-1],     [1, 4, 7], [1, 4, 9], [-1],                  [2, 4, 7], [-1], [-1]]

[[-1], [1, 2, 9], [1, 2, 7, 9],     [1, 4, 5, 7, 8], [1, 4, 6, 8, 9], [1, 4, 5, 7, 9],        [4, 6, 7, 9], [1, 6], [4, 7]]
[[-1], [-1], [-1],                    [1, 7], [1, 9], [1, 7, 9],                              [-1], [-1], [-1]]
[[-1], [1, 9], [1, 7, 9],           [-1], [1, 4, 6, 9], [-1],                                 [4, 6, 7, 9], [1, 6], [5]]

[[9], [-1], [-1],                    [3, 4], [-1], [2, 4],                                   [2, 3, 6], [2, 6], [1]]
[[1, 2], [3], [1, 2],                [9], [-1], [-1],                                      [-1], [-1], [8]]
[[-1], [6], [-1],                   [1, 3, 8], [1, 8], [1, 2],                            [2, 3], [-1], [-1]]

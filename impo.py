lists2 = [
     [
    [0,0,0, 0,3,0, 0,9,0],
    [7,5,0, 0,2,0, 1,0,3],
    [0,0,3, 0,0,8, 0,5,6],

    [3,0,0, 0,0,0, 0,0,0],
    [5,4,6, 0,0,0, 8,3,2],
    [8,0,0, 2,0,3, 0,0,0],

    [0,7,8, 0,5,0, 0,0,0],
    [0,0,0, 0,7,6, 5,4,0],
    [4,0,5, 0,0,0, 0,7,9]
    ]
    ,
    [
[[6], [8], [2], [1, 5, 7], [-1], [1, 5, 7], [4, 7], [-1], [4, 7]],
[[-1], [-1], [4], [6], [-1], [9], [-1], [8], [-1]],
[[1, 2], [2, 9], [-1], [1, 7], [4], [-1], [2, 7], [-1], [-1]],

[[-1], [1, 2, 9], [7, 9], [1, 4, 5, 7, 8], [1, 6, 8, 9], [1, 5, 7], [4, 7, 9], [1, 6], [4, 7]],
[[-1], [-1], [-1], [1, 7], [1, 9], [1, 7], [-1], [-1], [-1]],
[[-1], [1, 9], [7, 9], [-1], [1, 6, 9], [-1], [4, 7, 9], [1, 6], [5]],

[[9], [-1], [-1], [3], [-1], [4], [6], [2], [1]],
[[2], [2, 3], [1], [9], [-1], [-1], [-1], [-1], [8]],
[[-1], [6], [-1], [1, 8], [1, 8], [2], [3], [-1], [-1]],
    ]
]
print("single in block")
def block(numblock):
        # 123
        # 456
        # 789
        global fx,fy
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
        elif numblock == 7:
            fx, fy = 0,6
        elif numblock == 8:
            fx, fy = 3,6
        elif numblock == 9:
            fx, fy = 6,6   
        else:
            print("ERROR ON BLOCK")
       
if True:
        for y in range(9):
            print(lists2[1][y])
            if y == 2 or y ==5:
                print(" ")
        print(" ")
        print(" ")
        for blockno in range(1,10):
            singleLine = []
            singles = []
            block(blockno)
            for y in range(3):
                for x in range(3):
                    if lists2[1][y+fy][x+fx].__len__() != 1:
                        for o in lists2[1][y+fy][x+fx]:
                            singleLine.append(o)
                    else: 
                        for o in lists2[1][y+fy][x+fx]:
                            singles.append(o)
            for o in singleLine:
                for a in singles:
                    if o == a:
                        singleLine.remove(a)
            print(singleLine)
            for a in singleLine:
                if singleLine.count(a) == 1:
                    print(a)
                    for y in range(3):
                        for x in range(3):
                                for b in lists2[1][y+fy][x+fx]:
                                    if a == b:
                                        continue
                                    else:
                                        if lists2[1][y+fy][x+fx].__contains__(a):
                                            lists2[1][y+fy][x+fx].remove(b)
                                           

for y in range(9):
            print(lists2[1][y])
            if y == 2 or y ==5:
                print(" ")

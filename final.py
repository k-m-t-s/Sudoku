import pygame as pg

pg.init()
FONT = pg.font.Font(None,35)
FONTpossy = pg.font.Font(None,20)

black = pg.Color('black')
lightblue = pg.Color(30,125,150)
grey = pg.Color(100,100,100)
FPS = 30
window = pg.display.set_mode((500,450))
xcounter = -1
ycounter = 0
board = []
lists2 =[]

def drawingPossy(window, text,x, y, line):  
    if line == 1:    
        textsurface = FONTpossy.render(text, True, grey)
        window.blit(textsurface,(x+3,y+4))
    elif line == 2:
        textsurface = FONTpossy.render(text, True, grey)
        window.blit(textsurface,(x+3,y+18))
    elif line == 3:
        textsurface = FONTpossy.render(text, True, grey)
        window.blit(textsurface,(x+3,y+35))

class highlightbox:
    def __init__(self,x,y,w,h) -> None:
        self.recta = pg.Rect(x,y,w,h)
        
        self.activeColor = pg.Color("black")
    
    def draw(self, window):
        pg.draw.rect(window, self.activeColor,self.recta,2)

class box:
    def __init__(self,x,y,w,h,num,textcolor) -> None:
        self.recta = pg.Rect(x,y,w,h)
        self.width = 1
        self.x = x
        self.y = y 
        self.num = num
        self.active = False
        self.textcolor = textcolor
        self.activeColor = pg.Color("black")
        self.textsurface = FONT.render(self.num, True, self.textcolor)
    
    def draw(self,window):
        pg.draw.rect(window, self.activeColor,self.recta,self.width)
        window.blit(self.textsurface,(self.x+5,self.y+5))

    def inputs(self, event):
        if pg.MOUSEBUTTONDOWN == event.type:
            if self.recta.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if self.active == True:
            self.activeColor = pg.Color("red")
            self.width = 3
        else:
            self.activeColor = pg.Color("black")
            self.width = 1
        if pg.KEYDOWN == event.type:
            if self.active == True:
                if pg.K_BACKSPACE == event.key:
                    self.num = self.num[:-1]
                else:    
                    if len(self.num)>0:
                        pass
                    else:
                        self.num += event.unicode
        self.textsurface = FONT.render(self.num,True,self.textcolor)


class algorithm:
    def __init__(self) -> None:
        pass
    def block(self, numblock):
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
       
    def setpossibilities(self):
        global lists2
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
        for y in range (9):
            for x in range(9):
                if board[y][x] != 0:
                    lists2[1][y][x] = [-1]
    def checkremove(self):
        #horizontal
        for y in range(9):
            for x in range(9):
                    if not board[y][x] == 0:
                        for xchange in range(9):
                            if lists2[1][y][xchange].__contains__(board[y][x]):
                                lists2[1][y][xchange].remove(board[y][x])
        #vertical
        for y in range(9):
            for x in range(9):
                if not board[y][x] == 0:
                    for ychange in range(9):
                        if lists2[1][ychange][x].__contains__(board[y][x]):
                            lists2[1][ychange][x].remove(board[y][x])
        #block
        for blockno in range(1,10):
            self.block(blockno)
            for y in range(3):
                for x in range(3):
                    for ychange in range(3):
                        for xchange in range(3):
                            if lists2[1][ychange+fy][xchange+fx].__contains__(board[y+fy][x+fx]):
                                lists2[1][ychange+fy][xchange+fx].remove(board[y+fy][x+fx])
        #clears the single possibilities on the other place in the same block
        for blockno in range(1,10):
            self.block(blockno)
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

        # if single in block, take out other possibilities 
        
        for blockno in range(1,10):
            singleLine = []
            singles = []
            self.block(blockno)
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
            for a in singleLine:
                if singleLine.count(a) == 1:
                    for y in range(3):
                        for x in range(3):
                                for b in lists2[1][y+fy][x+fx]:
                                    if a == b:
                                        continue
                                    else:
                                        if lists2[1][y+fy][x+fx].__contains__(a):
                                            lists2[1][y+fy][x+fx].remove(b)
                                           


        ## only double in single row kicks out other shit
        
        for blockno in range(1,10):
            self.block(blockno)      
            singleLine=[]
            singles = []
            for y in range(3):
                for x in range(3):
                    if lists2[1][y+fy][x+fx].__len__() != 1:
                        for q in lists2[1][y+fy][x+fx]:
                            singleLine.append(q)

                    if lists2[1][y+fy][x+fx].__len__() == 1 and lists2[1][y+fy][x+fx] != -1:
                        for k in lists2[1][y+fy][x+fx]:
                            singles.append(k)
            
                
            for q in singleLine:
                counter = 0
                for a in singleLine:
                    if q == a:
                        counter +=1
                        if counter != 1:
                            singleLine.remove(q)

            for k in singles:
                    if singleLine.__contains__(k):
                        singleLine.remove(k)

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
                    if (firstrow + secondrow) == 0 and thirdrow ==2:
                        for x in range(9):
                            if fx == 0:
                                if x < 3:
                                    continue
                            if fx == 3:
                                if x >= 3 and x < 6:
                                    continue
                            if fx == 6:
                                if x >= 6:
                                    continue
                            if lists2[1][2+fy][x].__contains__(q):
                                lists2[1][2+fy][x].remove(q)
                                
                                        
                    if (thirdrow + secondrow) == 0 and firstrow ==2:
                        for x in range(9):
                            if fx == 0:
                                if x < 3:
                                    continue
                            if fx == 3:
                                if x >= 3 and x < 6:
                                    continue
                            if fx == 6:
                                if x >= 6:
                                    continue
                            if lists2[1][0+fy][x].__contains__(q):
                                lists2[1][0+fy][x].remove(q)
                                
                                
                                        
                    if (firstrow + thirdrow) == 0 and secondrow ==2:
                        for x in range(9):
                            if fx == 0:
                                if x < 3:
                                    continue
                            if fx == 3:
                                if x >= 3 and x < 6:
                                    continue
                            if fx == 6:
                                if x >= 6:
                                    continue
                            if lists2[1][1+fy][x].__contains__(q):
                                lists2[1][1+fy][x].remove(q)
        
        # removing douples in the y axis   
        for blockno in range(3,4):
            self.block(blockno)      
            singleLine=[]
            singles = []
            for y in range(3):
                for x in range(3):
                    if lists2[1][y+fy][x+fx].__len__() != 1:
                        for q in lists2[1][y+fy][x+fx]:
                            singleLine.append(q)

                    if lists2[1][y+fy][x+fx].__len__() == 1 and lists2[1][y+fy][x+fx] != -1:
                        for k in lists2[1][y+fy][x+fx]:
                            singles.append(k)
            
                
            for q in singleLine:
                counter = 0
                for a in singleLine:
                    if q == a:
                        counter +=1
                        if counter != 1:
                            singleLine.remove(q)

            for k in singles:
                    if singleLine.__contains__(k):
                        singleLine.remove(k)

            for q in singleLine:
                firstcolumn = 0
                secondcolumn = 0
                thirdcolumn = 0
                for y in range(3):
                    for x in range(3):
                        if lists2[1][fy+y][fx+x].__len__() != 1:
                            if lists2[1][fy+y][fx+x].__contains__(q):
                                if x == 0:
                                    firstcolumn += 1
                                        
                                if x == 1:
                                    secondcolumn += 1
                                        
                                if x == 2:
                                    thirdcolumn += 1
                    

                column_sum = firstcolumn + secondcolumn + thirdcolumn
                
                if column_sum < 4 and column_sum > 1:
                    if (firstcolumn + secondcolumn) == 0 and thirdcolumn ==2:
                        for y in range(9):
                            if fy == 0:
                                if y < 3:
                                    continue
                            if fy == 3:
                                if y >= 3 and y < 6:
                                    continue
                            if fy == 6:
                                if y >= 6:
                                    continue
                            if lists2[1][y][2+fx].__contains__(q):
                                lists2[1][y][2+fx].remove(q)
                                
                                        
                    if (thirdcolumn + secondcolumn) == 0 and firstcolumn ==2:
                        for y in range(9):
                            if fy == 0:
                                if y < 3:
                                    continue
                            if fy == 3:
                                if y >= 3 and y < 6:
                                    continue
                            if fy == 6:
                                if y >= 6:
                                    continue
                            if lists2[1][y][fx+0].__contains__(q):
                                lists2[1][y][fx+0].remove(q)
                              
                                
                                
                                        
                    if (firstcolumn + thirdcolumn) == 0 and secondcolumn ==2:
                        for y in range(9):
                            if fy == 0:
                                if y < 3:
                                    continue
                            if fy == 3:
                                if y >= 3 and y < 6:
                                    continue
                            if fy == 6:
                                if y >= 6:
                                    continue
                            if lists2[1][y][fx+1].__contains__(q):
                                lists2[1][y][fx+1].remove(q)  
                                                           
        
def num():
    global xcounter
    global ycounter
    global board
    board = [
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
    xcounter = xcounter +1
    if xcounter == 9:
        xcounter = 0
        if ycounter != 9:
            ycounter +=1
        else:
            ycounter = 1
    if str(board[ycounter][xcounter])==("0"):
        board[ycounter][xcounter] = ""
    return board[ycounter][xcounter]


def callingalgo(num):
    algo = algorithm()
    algo.setpossibilities()
    for r in range(num):
        algo.checkremove()
    counter = 0
    anotherlist = []
    global listsfinal
    listsfinal = []
    for y in range(9):
        for x in range(9):
            if lists2[1][y][x].__len__() == 1:
                if lists2[1][y][x] == [-1]:
                    continue
                counter += 1
                for s in lists2[1][y][x]:
                    a = str(s)
                anotherlist.append([x, y, a])

    for y in range(counter):
        da = box(anotherlist[y][0] * 50, anotherlist[y][1] * 50, 50, 50, anotherlist[y][2], lightblue)
        listsfinal.append(da)
    

def main():
    clock = pg.time.Clock()
    highlight_boxes = []
    boxes = []
    run = True
    for y in range(0,450,50):
        for x in range(0,450,50):
            box1 = box(x,y,50,50,str(num()), black)
            boxes.append(box1)
    
    for x in range(0,450,150):
        for y in range(0,450,150):
            box1 = highlightbox(x,y,150,150)
            highlight_boxes.append(box1)
    callingalgo(20)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            for z in boxes:
                z.inputs(event)
       
        window.fill(pg.Color("white"))
        
        for rectan in boxes:
            rectan.draw(window)

        for rectan in highlight_boxes:
            rectan.draw(window)
        for rectan in listsfinal:
            rectan.draw(window)
        """
        tempo = ""
        for y in range(9):
            for x in range(9):
                if lists2[1][y][x].__len__() != 1:
                    if lists2[1][y][x].__contains__(1):
                            for r in lists2[1][y][x]:
                                tempo += str(r)
                drawingPossy(window, tempo, x * 50, y * 50,1)


        """
        pg.display.flip()

        clock.tick(FPS)
    pg.quit()
main()

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
                    if not board[y][x] == 0 or lists2[1][y][x].__len__() == 1:
                        for xchange in range(9):
                            if lists2[1][y][xchange].__contains__(board[y][x]):
                                lists2[1][y][xchange].remove(board[y][x])
        #vertical
        for y in range(9):
            for x in range(9):
                if not board[y][x] == 0 or lists2[1][y][x].__len__() == 1:
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
        
    
def num():
    global xcounter
    global ycounter
    global board
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
    algo = algorithm()
    algo.setpossibilities()
    algo.checkremove()
    algo.checkremove()
    algo.checkremove()
    
    counter = 0
    anotherlist = []
    listsfinal = []
    for y in range(9):
        for x in range(9):
            if lists2[1][y][x].__len__() == 1:
                if lists2[1][y][x] == [-1]:
                    continue
                print(str(lists2[1][y][x])+" "+str(y) +" "+str(x))
                counter += 1
                for s in lists2[1][y][x]:
                    a = str(s)
                anotherlist.append([x, y, a])
    print(anotherlist)

    for y in range(counter):
        da = box(anotherlist[y][0] * 50, anotherlist[y][1] * 50, 50, 50, anotherlist[y][2], lightblue)
        listsfinal.append(da)




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

import pygame as pg

pg.init()
FONT = pg.font.Font(None,35)
black = pg.Color('black')
FPS = 30
window = pg.display.set_mode((450,450))
xcounter = -1
ycounter = 0
board = []

class highlightbox:
    def __init__(self,x,y,w,h) -> None:
        self.recta = pg.Rect(x,y,w,h)
        
        self.activeColor = pg.Color("black")
    
    def draw(self, window):
        pg.draw.rect(window, self.activeColor,self.recta,2)

class box:
    def __init__(self,x,y,w,h,num) -> None:
        self.recta = pg.Rect(x,y,w,h)
        self.width = 1
        self.x = x
        self.y = y 
        self.num = num
        self.active = False
        self.activeColor = pg.Color("black")
        self.textsurface = FONT.render(self.num, True, black)
    
    def draw(self, window):
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
        self.textsurface = FONT.render(self.num,True,black)


class algorithm:
    def __init__(self) -> None:
        pass
    def horizontalcheck(self):
        for x in range(9):
            pass
    def verticalcheck(self):
        pass
    def blockcheck(self):
        pass

def num():
    global xcounter
    global ycounter
    global board
    board = [
    [0,0,7,0,4,0,0,0,0],
    [0,0,0,0,0,8,0,0,6],
    [0,4,1,0,0,0,9,0,0],
    [0,0,0,0,0,0,1,7,0],
    [0,0,0,0,0,6,0,0,0],
    [0,0,8,7,0,0,2,0,0],
    [3,0,0,0,0,0,0,0,0],
    [0,0,0,1,2,0,0,0,0],
    [8,6,0,0,7,6,0,0,5],
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
    return str(board[ycounter][xcounter])

    
def main():
    clock = pg.time.Clock()
    highlight_boxes = []
    boxes = []
    run = True
    for x in range(0,450,50):
        for y in range(0,450,50):
            box1 = box(y,x,50,50,num())
            boxes.append(box1)
    
    for x in range(0,450,150):
        for y in range(0,450,150):
            box1 = highlightbox(x,y,150,150)
            highlight_boxes.append(box1)
          
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
        pg.display.flip()
        clock.tick(FPS)
    pg.quit()
main()
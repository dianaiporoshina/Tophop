import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk
import random as rand
import math as math

root = tk.Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())

loadFoot = Image.open("resource\\foot.png")
loadFootR = loadFoot.transpose(Image.FLIP_LEFT_RIGHT).rotate(-90)
loadFootL = loadFoot.rotate(-90)
loadHand = Image.open("resource\\hand.png")
loadHandR = loadHand.transpose(Image.FLIP_LEFT_RIGHT).rotate(-90)
loadHandL = loadHand.rotate(-90)


w = root.winfo_screenwidth() 
h = root.winfo_screenheight()
gapH = 15
gapW = 5
cardH = 200
cardW = 40
multRow = 1.5

numRow = int(math.log((multRow-1)*w/(cardW+gapW)+1,multRow))

realW = int((multRow-1)*w/(multRow**(numRow)-1))
gapW = realW-cardW

cardsArray = []

canvas=tk.Canvas(root, width=w, height=h)
canvas.pack()

def drawCard(x, y, hand, left, line, row, curCardW):
    if hand==1:
        if left==1:
            card = loadHandL
        else:
            card = loadHandR
    else:
        if left==1:
            card = loadFootL
        else:
            card = loadFootR
    print(curCardW)
    renderCard = ImageTk.PhotoImage(card.resize((curCardW,cardH)))
    cardsArray.append(renderCard)
    canvas.create_image(x, y, image = renderCard, tag = "line"+str(line)+" row"+str(row))

def drawRow(x, row, curCardW, curGapW):
    a=rand.randint(0,1)
    b=rand.randint(0,2)
    c=rand.randint(0,1)
    drawCard(curCardW//2+x,h//2+(b-1)*(cardH+gapH),a,c,b,row,curCardW)
    d=0
    for j in range (0,3):
        if j!=b:
            drawCard(curCardW//2 + x,h//2+(j-1)*(cardH+gapH), 1-a, 1-d,j,row,curCardW)
            d=d+1

def drawField():
    curCardW = cardW
    curGapW = gapW
    curX = 0
    for i in range(0, numRow):
        print(curX, curCardW,curGapW)
        drawRow(curX,i,curCardW,curGapW)
        curX = curX+curGapW+curCardW
        curGapW = int(curGapW*multRow)
        curCardW = int(curCardW*multRow)

def updateGapH(delta):
    top = canvas.find_withtag("line0")
    for card in top:
        canvas.move(card, 0, delta)
    bottom = canvas.find_withtag("line2")
    for card in bottom:
        canvas.move(card, 0, -delta)

def updateGapW(delta):
    for i in range(0,numRow):
        curRow = canvas.find_withtag("row"+str(i))
        for card in curRow:
            canvas.move(card, delta*i, 0)

drawField()

root.bind('<q>',lambda e: updateGapH(-1))
root.bind('<a>',lambda e: updateGapH(1))
root.bind('<w>',lambda e: updateGapW(-1))
root.bind('<s>',lambda e: updateGapW(1))

root.mainloop()

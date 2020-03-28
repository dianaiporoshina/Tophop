import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk
import random as rand

root = tk.Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())

loadFoot = Image.open("resource\\foot.png")
renderFootR = ImageTk.PhotoImage(loadFoot.transpose(Image.FLIP_LEFT_RIGHT).rotate(-90))
renderFootL = ImageTk.PhotoImage(loadFoot.rotate(-90))
loadHand = Image.open("resource\\hand.png")
renderHandR = ImageTk.PhotoImage(loadHand.transpose(Image.FLIP_LEFT_RIGHT).rotate(-90))
renderHandL = ImageTk.PhotoImage(loadHand.rotate(-90))

w = root.winfo_screenwidth() 
h = root.winfo_screenheight()
gapH = 15
gapW = 10
numRow = w//(200+gapW)


canvas=tk.Canvas(root, width=w, height=h)
canvas.pack()

def drawCard(x, y, hand, left, line, row):
    if hand==1:
        if left==1:
            card = renderHandL
        else:
            card = renderHandR
    else:
        if left==1:
            card = renderFootL
        else:
            card = renderFootR
    canvas.create_image(x, y, image = card, tag = "line"+str(line)+" row"+str(row))
    #print("line"+str(line)+" row"+str(row))

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

for i in range (0,numRow):
    a=rand.randint(0,1)
    b=rand.randint(0,2)
    c=rand.randint(0,1)
    drawCard(100+i*(200+gapW),h//2+(b-1)*(200+gapH),a,c,b,i)
    d=0
    for j in range (0,3):
        if j!=b:
            drawCard(100 + i * (200+gapW),h//2+(j-1)*(200+gapH), 1-a, 1-d,j,i)
            d=d+1

root.bind('<q>',lambda e: updateGapH(-1))
root.bind('<a>',lambda e: updateGapH(1))
root.bind('<w>',lambda e: updateGapW(-1))
root.bind('<s>',lambda e: updateGapW(1))

root.mainloop()

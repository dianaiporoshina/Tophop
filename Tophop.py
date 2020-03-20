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

canvas=tk.Canvas(root, width=w, height=h)
canvas.pack()

def drawCard(x, y, hand, left):
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
    canvas.create_image(x,y,image=card)
for q in range(0,5):/
    for i in range (0,5):
        a=rand.randint(0,1)
        b=rand.randint(0,2)
        c=rand.randint(0,1)

       drawCard(100+i*200,100+b*200,a,c)
       d=0
       for j in range (0,3):
            if j!=b:
                drawCard(100 + i * 200, 100 + j * 200, 1-a, 1-d)
                d=d+1
time.sleep(60)
#    image=canvas.create_image(100+i*200, 100, image=renderFootL)
#    image=canvas.create_image(100+i*200, 300, image=renderFootR)
#    image=canvas.create_image(100+i*200, 500, image=renderHandR)
#    image=canvas.create_image(100+i*200, 700, image=renderHandL)


root.mainloop()

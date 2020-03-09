import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk

root = tk.Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())

loadFoot = Image.open("resource\\foot.png")
renderFootR = ImageTk.PhotoImage(loadFoot.transpose(Image.FLIP_LEFT_RIGHT).rotate(-90))
renderFootL = ImageTk.PhotoImage(loadFoot.rotate(-90))
loadHand = Image.open("resource\\hand.png")
renderHandR = ImageTk.PhotoImage(loadHand.transpose(Image.FLIP_LEFT_RIGHT).rotate(-90))
renderHandL = ImageTk.PhotoImage(loadHand.rotate(-90))

canvas=tk.Canvas(root, width=1000, height=1200)
canvas.pack()
for i in range (0,5):
    image=canvas.create_image(100+i*200, 100, image=renderFootL)
    image=canvas.create_image(100+i*200, 300, image=renderFootR)
    image=canvas.create_image(100+i*200, 500, image=renderHandR)
    image=canvas.create_image(100+i*200, 700, image=renderHandL)


root.mainloop()
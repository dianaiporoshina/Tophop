import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk

root = tk.Tk()
root.attributes('-fullscreen', True)
root.bind('<Escape>',lambda e: root.destroy())

loadFoot = Image.open("resource\\foot.png")
renderFoot = ImageTk.PhotoImage(loadFoot.transpose(Image.FLIP_LEFT_RIGHT).rotate(-90))
loadHand = Image.open("resource\\hand.png")
renderHand = ImageTk.PhotoImage(loadHand.resize((100,100)))

canvas=tk.Canvas(root, width=1000, height=1000)
canvas.pack()

image=canvas.create_image(100, 100, image=renderFoot)
image=canvas.create_image(300, 100, image=renderHand)

root.mainloop()
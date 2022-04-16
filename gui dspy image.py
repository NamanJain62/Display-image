from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.geometry("400x500")
#photo = PhotoImage(file="anaconda_PNG15.png")
#root.title("my gui with harry")
#label = Label(image = photo)
#label.pack()


#for jpg imgage
image = Image.open("1.jpeg")
photo =ImageTk.PhotoImage(image)
label=Label(image=photo)
label.pack()
root.mainloop()

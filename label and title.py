from tkinter import *

root=Tk()
root.geometry("400x500")
root.title("Naman jain")

# important label option
#text-add the text
#bd- background
#fg - forground
#font -  sets the font
#padx - x padding
#pady - y padding
#relief - border styling -SUNKEN, RAISED, GROOVE, RIDGE

title_label= Label(text="Time of India",bg="blue", fg="white",padx=0,pady=0, font=("Time new roman",20,"bold"),borderwidth=4)
title_label1= Label(text="12/10/2022",bg="red", fg="white", font=("Time new roman",14,"bold"))
title_label2= Label(text='''hjklnikrthrtnhnrhnrtlhnrtn \n nhlnrhrt jn nlhnh lntniknh \n t nnr rtlk hn nhrt l nlhnrkh n lhlkt''',bg="red", fg="white", font=("Time new roman",14,"bold"))
#important pack option
# anchor=nw
#side = top, bottom, left, right
#fill
#
title_label.pack(side=TOP,fill=X)
title_label1.pack(anchor='ne',side=TOP)
title_label2.pack(side=BOTTOM,fill=Y)
root.mainloop()

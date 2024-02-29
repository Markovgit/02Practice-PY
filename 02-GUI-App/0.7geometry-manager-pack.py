from tkinter import *
window=Tk()

frame_a = Frame(master=window,width=150,height=150,bg="red")
frame_a.pack(fill=BOTH,side=LEFT,expand=True)
frame_b = Frame(master=window,width=100,height=100,bg="pink")
frame_b.pack(fill=BOTH,side=LEFT,expand=True)
frame_c = Frame(master=window,width=50,height=50,bg="green")
frame_c.pack(fill=BOTH,side=LEFT,expand=True)


#ovako dobijamo responsive




window.mainloop()
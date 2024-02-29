from tkinter import*
window = Tk()
frame = Frame(master=window,width=200,height=200)
frame.pack()

label_a = Label(master=frame,text="Im at (0,0)",bg="green",fg="yellow")
#pozicionira 
label_a.place(x=0,y=0)

label_b = Label(master=frame,text="Im at (50,50)",bg="red",fg="yellow")
#pozicionira 
label_b.place(x=50,y=50)

label_c = Label(master=frame,text="Im at (100,100)",bg="black",fg="yellow")
#pozicionira 
label_c.place(x=100,y=100)


# sa place ne dobijamo responsive


window.mainloop()
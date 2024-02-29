from tkinter import *
window = Tk()
def greetings_message ():
    greetings_a = Label(text="what are you doing",font="Arial 20 ",fg="white",bg="pink")
    greetings_a.pack()
    greetings_b = Label(text="why are you doing",font="Arial 20 ",fg="white",bg="green")
    greetings_b.pack()
    greetings_c = Label(text="how are you doing",font="Arial 20 ",fg="white",bg="blue")
    greetings_c.pack()
btn = Button(text="Click on ME",font="Arial 20",fg="white",bg="red",command=greetings_message)
btn.pack()



window.mainloop()
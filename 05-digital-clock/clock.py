from tkinter import *
from time import strftime
root = Tk()
root.title("Digital-Clock-App")
#funkcija koja pokrece sat na ekranu 
def time():
    TimeFormat = strftime(" %H:%M:%S")
    clock.config(text=TimeFormat)
    clock.after(1000,time)
#izgled i velicina sata
clock = Label(root,font="Arial 100  bold",pady=30,bg="#FFC742",fg='black')
clock.pack()

time()
mainloop()
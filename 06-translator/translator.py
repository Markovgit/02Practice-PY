# 1 import potrebne module 
from tkinter import *
from translate import Translator

# 2 create display window
 
#2.1 create instancu tkinter okvira ili prozora 
Screen =Tk()
Screen.title("Translator App")
Screen.geometry("450x350")
#Screen.resizable(0,0)
Screen.config(bg="lightblue")


# 3 definisi meni sa opcijama(widget) koji bira jezik u ovoj aplikaciji 
# 3.1 za imput widget 
InputLanguageChoice = StringVar()
InputLanguageChoice.set("English")  #  jezik po default-u
LanguageChoices = OptionMenu(Screen,InputLanguageChoice,"Serbian","English", "French","German") #.pack() mozda treba staviti 
LanguageChoices.config(bg="green",fg="white")
LanguageChoices["menu"].config(bg= "pink")
LanguageChoices.grid(row=2,column=2,ipadx=15)

# 3.2 output wiget
OutputLanguageChoice = StringVar()
OutputLanguageChoice.set("Choose")  #  jezik po default-u
LanguageChoices = OptionMenu(Screen,OutputLanguageChoice,"Serbian","English", "French","German") #.pack() mozda treba staviti 
LanguageChoices.config(bg="green",fg="white")
LanguageChoices["menu"].config(bg= "pink")
LanguageChoices.grid(row=2,column=4,ipadx=15)

# 4 create input i output text (widget)
# input 
Label(Screen,text="Enter text ").grid(row=3,column=1)
TextVar = StringVar()
Textbox = Entry(Screen,textvariable=TextVar).grid(row=3,column=2,ipadx=15,ipady=20) 

#output
Label(Screen,text="Enter text ").grid(row=3,column=3)
OutputVar = StringVar()
Textbox = Entry(Screen,textvariable = OutputVar).grid(row=3,column=4,ipadx=15,ipady=20) 


# definisi funkciju

def Translate():
    translator = Translator(from_lang = InputLanguageChoice.get(),to_lang = OutputLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

# create translate dugme 
# dugme koje pokrece prevod 
B = Button(Screen,text="Click me to Translate",command=Translate,relief=GROOVE).grid(row=4,column=3)


Screen.mainloop()




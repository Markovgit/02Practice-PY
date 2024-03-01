#first of all you  must install pyspeedtest  module by using pip command 


import pyspeedtest
from tkinter import *
# create the window 
#create an object from the Tk class

speedTest = Tk()
speedTest.configure(bg="lightblue")
speedTest.geometry("750x350")
speedTest.resizable(0,0)
speedTest.title("INTERNET  SPEED TESTER")

ping_Speed = StringVar()
down_Speed = StringVar()

#create text and link entry widget 
heading_text = Label(speedTest,text="Welcome to tje Internet Speed Tester ",font="Times New Roman 16 bold",fg='black', bg= 'light blue')    
web_url = Label(speedTest,text="Enter web URL ",font="Times New Roman 14 bold", bg="blue")
ping_result = Label(speedTest,text="Ping result is: ",font="Times New Roman 14 bold",fg="white", bg="blue")
download_result = Label(speedTest,text="Download result is: ",font="Times New Roman 14 bold",fg="white", bg="blue")

#set position for widgets 
heading_text.grid(row=0,column=1,pady=20)
web_url.grid(row=1,column=0,pady=10)
ping_result.grid(row=3,column=0,pady=10)
download_result.grid(row=4,column=0,padx=10,pady=10)



result1 = Label(speedTest,text=" ",textvariable=ping_Speed,font="Times New Roman 18 italic",bg="black")
result1.grid(row=3,column=1)
result2 = Label(speedTest,text=" ",textvariable=ping_Speed,font="Times New Roman 18 italic",bg="black")
result2.grid(row=4,column=1)

#link entry box
url_entry = Entry(speedTest,width=25,font= "Times New Roman 16 italic")
url_entry.grid(row=1, column=1)
              
#create function        
def speed_test():
    internet = pyspeedtest.SpeedTest(url_entry.get())
    ping_Speed.set(internet.ping())
    down_Speed.set(internet.download())
    
    
    #button
    btn = Button(speedTest,text="Check Internet Speed",font="Times New Roman 18 italic",bg="black",border=5,command=speed_test)
    btn.grid(row=2,column=1,pady=10)
         
              

speedTest.mainloop()




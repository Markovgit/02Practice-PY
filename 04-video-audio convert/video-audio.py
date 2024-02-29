import moviepy.editor as mp
from tkinter import *
from tkinter import filedialog
#  kreiramo funkciju koja konvertuje video u audio fajl
def convert():
    videoClip = mp.VideoFileClip(fname)
    #Zadajemo ime novom audio fajlu i formatu .mp3
    videoClip.audio.write_audiofile("Converted video.mp3")
    messageToGenerate.set("Audio file is generated successfully")
    
# funkcija koja radi upload video fajla
def upload():
    #upload fajla 
    filename = filedialog.askopenfilename(filetypes =[('Mp4 Files', '*.mp4'),('WMV Files', '*.wmv'),('ogg files','*.ogg')])
    
    #poruka koja se prijazuje kada je fajl upload-ovan
    messageForUpload.set("File Uploaded:"+filename)
    #declaring global variable
    global fname
    # prebacivanje  vrednosti iz varijable filename u fname
    fname=filename

# izgled  prozora
root = Tk()
#visina sirina prozora
root.geometry("700x250")
#setting project/window bacground color
root["bg"] = "black"
#naslov projekta
root.title("Video to audio converting app done by Marko")
# kreiranje varijable za poruke 
global messageForUpload
global messageToGenerate
messageForUpload = StringVar()
messageToGenerate = StringVar()
#Label for uploading message 
Label(root,text="hello",textvar=messageForUpload,font="Arial 14",fg="#fff",bg="green").place(x=100,y=40)
#button za upload fajla
Button(root,text="Upload Video",command=upload,font="Arial 14 bold",fg="#fff",bg="green").place(x=100,y=70)
#button for convert video fajla u audio
Button(root,text="Convert Video",command=convert,font="Arial 14 bold",fg="#fff",bg="green").place(x=350,y=70)

#Label for Converting message 
Label(root,text="hello",textvar=messageToGenerate,font="Arial 14",fg="#fff",bg="green").place(x=100,y=120)





root.mainloop()
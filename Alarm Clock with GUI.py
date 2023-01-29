from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import time
import datetime
import threading
from pygame import mixer

root = Tk()
root.title("Alarm")
root.geometry("800x450")
mixer.init()

def th():
    t1 = threading.Thread(target=a, args=())
    t1.start()

def a():
    a = hr.get()
    if a == "":
        msg = messagebox.showerror('Invalid data', 'Please enter valid time')
    else:
        Alarmtime = a
        CurrentTime = time.strftime("%H:%M:%S")

        while Alarmtime != CurrentTime:
            CurrentTime = time.strftime("%H:%M:%S")

        if Alarmtime == CurrentTime:
            mixer.music.load('tone.mp3')
            mixer.music.play()
            msg = messagebox.showinfo('It is time', f'{amsg.get()}')
            if msg == 'ok':
                mixer.music.stop()

header = Frame(root)
header.place(x=5, y=5)

head = Label(root, text="ALARM CLOCK", fg="blue", font=(
    'Times New Roman', 25, 'bold', 'underline'))
head.pack(fill=X)

panel = Frame(root)
panel.place(x=5, y=70)

img = Image.open("page.png")
img = img.resize((400, 350))
my = ImageTk.PhotoImage(img)
label = Label(image=my)
label.pack(side=RIGHT)

atime = Label(panel, text="Alarm Time \n(Hour:Min:Sec)",
              font=('Times New Roman', 18))
atime.grid(row=0, column=1, padx=10, pady=5)

hr = Entry(panel, font=('Times New Roman', 20), width=7)
hr.grid(row=0, column=2, padx=10, pady=5)

amessage = Label(panel, text="Message", font=('Times New Roman', 20))
amessage.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

amsg = Entry(panel, font=('Times New Roman', 15), width=25)
amsg.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

start = Button(panel, text="Set Alarm", bg="yellow", fg="blue",
               font=('Times New Roman', 20, 'bold'), command=th)
start.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

root.mainloop()

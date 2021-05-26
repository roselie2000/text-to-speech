import pyttsx3
import tkinter
from tkinter import END,scrolledtext

def text_to_speech():

    engine = pyttsx3.init()
    saying = ent.get('1.0',END)
    engine.say(saying)
    engine.runAndWait()
    ent.delete('1.0', END)


root = tkinter.Tk()
root.title("Text to Speech")
root.geometry('300x300')
root.resizable(0,0)
root.iconbitmap("C:/Users/User/speakericon.ico")
root.config(bg="#fabc3d")
my_img = tkinter.PhotoImage(file="C:/Users/User/speaker.png")
lab = tkinter.Label(root, text="Enter your text here", bg="#fabc3d", fg="#c94353",  font=("Times",20, "bold"))
lab.pack(padx=10, pady=(10,0), anchor='w')
ent = tkinter.scrolledtext.ScrolledText(root, borderwidth=2,  width=50, height=5)
ent.pack(padx=10, pady=(10,0))
btn = tkinter.Button(root, image=my_img, bg="#fabc3d", command=text_to_speech).pack(padx=5, pady=7)
btn1 = tkinter.Button(root, text="Quit", width=10, bg='#d8d86c', fg="#c94353",  font=("Times",15, "bold"), command=root.destroy)
btn1.pack(padx=5, pady=7, ipadx=5)

root.mainloop()
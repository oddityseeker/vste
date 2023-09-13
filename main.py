from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog
from datetime import datetime
import time

st = 300000

STime = time.time()
saved = time.time()

window = Tk()
window.title("simple text editor")
window.geometry('400x250')

def openq():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            txt.delete("1.0", END)
            txt.insert("1.0", text)
def prim():
    st = int(spin.get()) * 1000
    print(st)
    save()
    window.after(st, prim)
def repeated():
    STime = time.time() - saved
    lbl.configure(text=STime)
    window.after(1000, repeated)

def save():
    global saved
    saved = time.time()
    s111 = 'qwe'+str(int(saved//1)) + '.txt'
    print(s111)
    text1 = txt.get("1.0", END)
    with open(s111, "w") as file:
        file.write(text1)
        file.close()


tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='прочее')
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='файл')
tab_control.pack(expand=1, fill='both')

window.after(0, repeated)

txt = scrolledtext.ScrolledText(tab2, width=110, height=30, wrap="word")
txt.grid(column=0, row=0)

lbl = Label(tab2, text=STime)
lbl.grid(column=1, row=1)

sbtn = Button(tab1, text="открыть", command=openq)
sbtn.grid(column=1, row=2)

sbtn = Button(tab1, text="сохранить", command=save)
sbtn.grid(column=1, row=0)

spin = Spinbox(tab1, from_=30, to=100, width=5)
spin.grid(column=1, row=1)

btn1 = Button(tab1, text="применить", command=prim)
btn1.grid(column=2, row=1)


window.mainloop()
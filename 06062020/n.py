from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import subprocess as sp
 
r = Tk()
r.title('Text Workerer')
file_name = ""
 
def file_open():
    try:
        global file_name
        file_name = fd.askopenfilename()
        splt = file_name.split("/")
        sc = ["xxd", "-g1", file_name]
        t = sp.run(sc, stdout = sp.PIPE)
        text.delete('1.0', 'end')
        text.insert('1.0', t.stdout)

    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Такой файл не считывается!")
 
 
def file_save():
    global file_name
    str = text.get(1.0, END)
    arg = ['xxd', '-r', '-g1', '-',  file_name]
    sp.run(arg, input = str.encode("UTF-8"), stdout = sp.PIPE)
    messagebox.showinfo("Сообщение", "Ваш файл {0}, был удачно сохранён!".format(file_name))
 
 
f_top = Frame(r)
f_bot = Frame(r)
 
f_top.pack()
f_bot.pack(expand=1, fill=BOTH)

b_save = Button(f_top, text="Save", padx=3, command=file_save)
b_save.pack(side=RIGHT, padx=2)
 
b_open = Button(f_top, text="Open", padx=3, command=file_open)
b_open.pack(side=RIGHT, padx=2)
 
scroll_y = Scrollbar(f_bot, orient=VERTICAL)
scroll_y.pack(side=RIGHT, fill=Y)
 
scroll_x = Scrollbar(f_bot, orient=HORIZONTAL)
scroll_x.pack(side=BOTTOM, fill=X, anchor=W)
 
text = Text(f_bot, width=80, height=20, wrap=NONE, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
text.pack(expand=1, fill=BOTH)
 
scroll_y.config(command=text.yview)
scroll_x.config(command=text.xview)
 
r.mainloop()

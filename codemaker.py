from tkinter import filedialog
from tkinter import Tk, Menu
from tkinter import Label, Button, Frame, END
from tkinter import NW, X, LEFT, StringVar, Entry
from tkinter import Scrollbar, RIGHT, Y, Text, E, BOTTOM
import requests


root = Tk()
global path
path = False


def dark_mode():
    root.configure(background='#4d4d4d')
    my_txt.config(background='#2e2e2e', foreground="#ccfcff")
    status_bar.config(background='#4d4d4d', foreground="#ccfcff")
    txt_scroll.config(background='#2e2e2e')
    my_menu.config(background='#2e2e2e', foreground="#ccfcff")
    edit_menu.config(background='#2e2e2e', foreground="#ccfcff")
    file_menu.config(background='#2e2e2e', foreground="#ccfcff")
    theme_menu.config(background='#2e2e2e', foreground="#ccfcff")
    my_frm_format.config(background='#2e2e2e')


def light_mode():
    root.configure(background='white')
    my_txt.config(background='white', foreground="black")
    status_bar.config(background='white', foreground="black")
    txt_scroll.config(background='white')
    my_menu.config(background='white', foreground="black")
    edit_menu.config(background='white', foreground="black")
    file_menu.config(background='white', foreground="black")
    theme_menu.config(background='white', foreground="black")
    my_frm_format.config(background='#f7f7f7')


def open_file():
    my_txt.delete("1.0", END)
    file = filedialog.askopenfilename(initialdir="C:/", filetypes=(('Text Files', '*.txt'), ('HTML Files', '*.html'),
                                                                   ('Python Files', '*.py'),('All Files', '*.*')),
                                      title="Open file")
    name = file
    status_bar.config(text='Opened        ')

    root.title(f'{name} - Scribble Editor')
    global path
    if file:
        global path
        path = file


    file = open(file, "r")
    stuff = file.read()
    my_txt.insert(END, stuff)
    file.close()


def save_as():
    global path
    file = filedialog.asksaveasfilename(initialdir="C:/", filetypes = (('Text Files', '*.txt'), ('HTML Files', '*.html'),
                                                                       ('Python Files', '*.py'),('All Files', '*.*')))
    name = file
    path=file
    status_bar.config(text='Saved        ')
    # name = name.replace("C:/scribble","")
    root.title(f'{name} - Scribble Editor')
    file = open(file,'w')
    data=my_txt.get(1.0,END)
    file.write(data)
    file.close()


def save():
    global path
    if path:
        file = open(path, 'w')
        file.write(my_txt.get(1.0, END))
        name = file
        status_bar.config(text='Saved        ')
        # name = name.replace("C:/scribble","")
        root.title(f'{name} - Scribble Editor')
        file.close()
    else:
        save_as()


def get_code():
    if (sitename.get() == "") or (sitename.get() == "https://www."):
        my_txt.insert(END, "Please enter correct website link for eg : https://www.sitename.com/ \nOr\ncheck Your Internet Connection")

    else:
        url = sitename.get()
        a = requests.get(url)
        code = a.content
        my_txt.insert(END, code)

def reset():
    my_txt.delete(1.0, END)



# window configuration
root.title("Code Generator")
root.iconbitmap('cg.ico')

sitename = StringVar()

#root.geometry("1366x768")
root.configure(background='white')
app_width = 1366
app_height = 768

win_width = root.winfo_screenwidth()
win_height = root.winfo_screenheight()

x = (win_width / 2) - (app_width / 2)
y = (win_height / 2) - (app_height / 2)

root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

my_frm_format = Frame(root, background="#f7f7f7")
my_frm_format.pack(anchor=NW, fill=X)


lab = Label(my_frm_format, text="Enter Website link (eg : https://www.example.com/):", font=("Consolas", 15)).pack(side=LEFT, padx=5)
ent = Entry(my_frm_format,width=35, borderwidth=1, textvariable=sitename, font=("Consolas", 13))
ent.insert(0, 'https://www.')
ent.pack(side=LEFT, padx=5, pady=5, ipady=5)

gen_cod = Button(my_frm_format, text="Generate Code", font=("Consolas", 15), borderwidth=1,width=15, height=1, background="grey", foreground="White", command=get_code)
gen_cod.pack(side=LEFT, padx=5)

Re_set = Button(my_frm_format, text="Clear", borderwidth=1, font=("Consolas", 15),width=15, height=1, background="grey", foreground="White", command=reset)
Re_set.pack(side=LEFT,padx=5)


# frame initialization
my_frm = Frame(root)
my_frm.pack(pady=5)


# scroll bar
txt_scroll = Scrollbar(my_frm)
txt_scroll.pack(side=RIGHT, fill=Y)



# text area
my_txt = Text(my_frm, width=150, height=29, font=('Consolas', 16), selectbackground="#ff564a",
              selectforeground="white", undo=True, yscrollcommand=txt_scroll.set, borderwidth="0")
my_txt.pack()

# menu initialization
my_menu = Menu(root)
root.config(menu=my_menu)

# file menu
file_menu = Menu(my_menu, tearoff=False, font=('Consolas', 11))
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open               Ctr+O",command=open_file)
file_menu.add_command(label="Save               Ctr+S", command=save)
file_menu.add_command(label="Save As      Ctr+Shift+S", command=save_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# edit menu
edit_menu = Menu(my_menu, tearoff=False, font=('Consolas', 11))
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut",accelerator="Ctrl+X",command=lambda: my_txt.focus_get().event_generate('<<Cut>>'))
edit_menu.add_command(label="Copy ",accelerator="Ctrl+C",command=lambda: my_txt.focus_get().event_generate('<<Copy>>'))
edit_menu.add_command(label="Paste" ,accelerator="Ctrl+V",command=lambda: my_txt.focus_get().event_generate('<<Paste>>'))
edit_menu.add_separator()
edit_menu.add_command(label="Undo    Ctr+Z", command=my_txt.edit_undo)
edit_menu.add_command(label="Redo    Ctr+Y", command=my_txt.edit_redo)



# themes
theme_menu = Menu(my_menu, tearoff=False, font=('Consolas', 11))
my_menu.add_cascade(label="Theme", menu=theme_menu)
theme_menu.add_command(label="Dark Mode", command=dark_mode)
theme_menu.add_command(label="Light Mode", command=light_mode)

# status bar
status_bar = Label(root, text='Ready         ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

# config scroll bar
txt_scroll.config(command=my_txt.yview)

root.mainloop()

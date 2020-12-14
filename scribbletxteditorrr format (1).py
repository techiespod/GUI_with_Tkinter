
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import Tk, Menu
from tkinter import colorchooser
from tkinter import ttk
from tkinter import Label, Button, Frame, END, IntVar
from tkinter import NW, X, PhotoImage, LEFT, StringVar
from tkinter import Scrollbar, RIGHT, Y, Text, E, BOTTOM
from fpdf import FPDF
import os
import pyttsx3

def load_editor():

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
        export_menu.config(background='#2e2e2e', foreground="#ccfcff")
        file_menu.config(background='#2e2e2e', foreground="#ccfcff")
        theme_menu.config(background='#2e2e2e', foreground="#ccfcff")

    def light_mode():
        root.configure(background='white')
        my_txt.config(background='white', foreground="black")
        status_bar.config(background='white', foreground="black")
        txt_scroll.config(background='white')
        my_menu.config(background='white', foreground="black")
        edit_menu.config(background='white', foreground="black")
        export_menu.config(background='white', foreground="black")
        file_menu.config(background='white', foreground="black")
        theme_menu.config(background='white', foreground="black")


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
        file.write(my_txt.get(1.0, END))
        file.close()
        
    def pdf():
        #root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='yes.png'))
        user_name=os.getlogin()
        if path==False:
            USER_INP = simpledialog.askstring(title="EXPORT To PDF",
                                  prompt="Enter File name of PDF:")

            #root.iconbitmap("icon1.ico")
            pdf = FPDF() 
            pdf.add_page() 
            pdf.set_font("Arial", size = 15) 
            f = my_txt.get(1.0,END)
            pdf.cell(200, 10, txt = f, ln = 1, align = 'L') 
            s="C:/Users/"+str(user_name)+"/Desktop/"+ str(USER_INP)+ ".pdf"
            my_txt.insert(END,pdf.output(s))
            status_bar.config(text='Pdf created at '+s)
            
        else:
            USER_INP = simpledialog.askstring(title="EXPORT To PDF",
                                  prompt="Enter File name of PDF:")
            pdf = FPDF() 
            pdf.add_page() 
            pdf.set_font("Arial", size = 15) 
            f = open(path, "r") 
            for x in f: 
                pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
            s="C:/Users/"+str(user_name)+"/Desktop/"+ str(USER_INP)+ ".pdf"
            my_txt.insert(END,pdf.output(s))
            status_bar.config(text='Pdf created at '+s)
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

    def choose_color():
        color_code = colorchooser.askcolor(title="Choose color")
        my_txt.config(foreground=color_code[1])

    def say_out():

        engin = pyttsx3.init()
        voices = engin.getProperty('voices')
        engin.setProperty('voice', voices[1].id)
        engin.setProperty('rate', 175)
        engin.say(my_txt.get(1.0, END))
        engin.runAndWait()

    def end_task():
        pass


    # window configuration
    root.title("Scribble Editor")
    root.iconbitmap('icon1.ico')

    #root.geometry("1366x768")
    root.configure(background='white')
    app_width = 1366
    app_height = 768


    win_width = root.winfo_screenwidth()
    win_height = root.winfo_screenheight()

    x = (win_width / 2) - (app_width / 2)
    y = (win_height / 2) - (app_height / 2)

    root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

    my_frm_format = Frame(root)
    my_frm_format.pack(anchor=NW, fill=X)

    photo = PhotoImage(file=r"clipart891338.png")
    photo1 = photo.subsample(1, 1)

    photo2 = PhotoImage(file=r"59377.png")
    photo3 = photo2.subsample(1, 1)

    photo4 = PhotoImage(file=r"under.png")
    photo5 = photo4.subsample(1, 1)

    ttk.Label(my_frm_format, text="Font :", font=("Consolas", 10)).pack(side=LEFT, padx=5)
    n_font_style = StringVar()
    n_font_size = IntVar()
    Font_Select = ttk.Combobox(my_frm_format, width=20, textvariable=n_font_style, state="readonly")

    # Adding combobox drop down list
    Font_Select['values'] = (' Times New Roman',
                              ' Arial',
                              ' Arial Black',
                              ' Helvatica',
                              ' Ink Free',
                              ' Courier New',
                              ' Lucida Console',
                              ' Impact',
                              ' Segoe Print',
                              ' Yu Gothic UI',
                              ' Comic Sans MS',
                              ' Calibri',
                             )

    Font_Select.pack(side=LEFT, padx=5)
    Font_Select.current()
    a = Font_Select.get()

    Font_Size = ttk.Combobox(my_frm_format, width=2, textvariable=n_font_size)

    # Adding combobox drop down list
    Font_Size['values'] = (9,10,11,12,14,16,18,20,22,24,26,28,36,48,72)

    Font_Size.pack(side=LEFT, padx=5)
    Font_Size.current()

    bold = Button(my_frm_format, borderwidth=0,image=photo1)
    bold.pack(side=LEFT, padx=5)

    italics = Button(my_frm_format, borderwidth=0, image=photo3)
    italics.pack(side=LEFT,padx=5)

    underline = Button(my_frm_format, borderwidth=0, image=photo5)
    underline.pack(side=LEFT, padx=5)

    color_piker = Button(my_frm_format, borderwidth=1, text="Text Colour ▼", command=choose_color)
    color_piker.pack(side=LEFT, padx=5)

    say = Button(my_frm_format, borderwidth=1, text="Speak Out Loud ", command=say_out)
    say.pack(side=LEFT, padx=5)

    end_say = Button(my_frm_format, borderwidth=1, text="||", command=end_task)
    end_say.pack(side=LEFT, padx=5)

    # frame initialization
    my_frm = Frame(root)
    my_frm.pack(pady=5)


    # scroll bar
    txt_scroll = Scrollbar(my_frm)
    txt_scroll.pack(side=RIGHT, fill=Y)



    # text area
    my_txt = Text(my_frm, width=150, height=30, font=('Consolas', 16), selectbackground="#ff564a",
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

    # export menu
    export_menu = Menu(my_menu, tearoff=False, font=('Consolas', 11))
    my_menu.add_cascade(label="Export", menu=export_menu)
    export_menu.add_command(label="Export As PDF",command=pdf)


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
load_editor()
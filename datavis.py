import gc
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import ttk
from PIL import ImageGrab
from tkinter import filedialog
import numpy as np
import random
from turtle import TurtleScreen, RawTurtle
import time
import webbrowser
from tkinter import messagebox
from math import *


class work:
    def __init__(self, m):

        # single line graph
        self.x = StringVar()
        self.y = StringVar()
        self.xname = StringVar()
        self.yname = StringVar()

        # double line graph
        self.x_double_1 = StringVar()
        self.y_double_1 = StringVar()
        self.x_double_2 = StringVar()
        self.y_double_2 = StringVar()
        self.x_doublename_real = StringVar()
        self.y_doublename_real = StringVar()
        self.x_doublename = StringVar()
        self.y_doublename = StringVar()

        # single bar graph
        self.x1 = StringVar()
        self.y1 = StringVar()
        self.x1_name = StringVar()
        self.y1_name = StringVar()

        # double bar graph
        self.x_bar_ = StringVar()
        self.y_bar_ = StringVar()
        self.x_bar_name = StringVar()
        self.y_bar_name = StringVar()
        self.x_bar_name_axix = StringVar()
        self.y_bar_name_axix = StringVar()

        # histogram raw data
        self.x_bar_hist = StringVar()
        self.y_bar_hist = StringVar()
        self.x_bar_hist_name = StringVar()
        self.y_bar_hist_name = StringVar()

        # histogram frequency
        self.x_bar_hist_f = StringVar()
        self.y_bar_hist_f = StringVar()
        self.x_bar_hist_name_f = StringVar()
        self.y_bar_hist_name_f = StringVar()

        # scattered single
        self.x_scattered_s = StringVar()
        self.y_scattered_s = StringVar()
        self.x_scattered_name_s = StringVar()
        self.y_scattered_name_s = StringVar()

        # scattered double
        self.x_scattered_d1 = StringVar()
        self.y_scattered_d1 = StringVar()
        self.x_scattered_d2 = StringVar()
        self.y_scattered_d2 = StringVar()
        self.x_scattered_name_d1 = StringVar()
        self.y_scattered_name_d1 = StringVar()
        self.x_scattered_name_d2 = StringVar()
        self.y_scattered_name_d2 = StringVar()

        # scattered 3D
        self.x_scattered_3d = StringVar()
        self.y_scattered_3d = StringVar()
        self.z_scattered_3d = StringVar()
        self.x_scattered_name_3d = StringVar()
        self.y_scattered_name_3d = StringVar()
        self.z_scattered_name_3d = StringVar()

        # pie chart
        self.pie_lable = StringVar()
        self.pie_data = StringVar()

        # calculator
        self.sc_variable = StringVar()

        self.m = m

    def canvasdemo(self):

        # self.m.config(bg="#ffffff")
        self.m.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.canvas = Canvas(self.m, width=1010, height=700, highlightbackground="#cfff70", highlightcolor="green",
                             highlightthickness=1, bg="#a2a3a2")
        self.canvas.grid(row=0, rowspan=20, padx=20, pady=20)
        self.root = TurtleScreen(self.canvas)
        turtle = RawTurtle(self.root, visible=False)
        self.root.bgcolor("#a2a3a2")
        turtle.color('#58CDAC')
        turtle.pensize(4)
        turtle.shape('arrow')
        turtle.speed(9)
        turtle.hideturtle()
        turtle.fillcolor("#58CDAC")
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(-150, -150)
        turtle.pendown()
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(160)
        turtle.forward(200)
        turtle.right(50)
        turtle.forward(150)
        turtle.left(40)
        turtle.forward(182)
        turtle.end_fill()

        turtle = RawTurtle(self.root, visible=False)
        # root1 = turtle.Turtle()
        turtle.color('#7ACA8C')
        turtle.pensize(4)
        turtle.shape('arrow')
        turtle.speed(9)
        turtle.hideturtle()
        turtle.fillcolor("#7ACA8C")
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(-150, -150)
        turtle.pendown()
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(250)
        turtle.left(150)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(90)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(40)
        turtle.forward(75)
        turtle.left(40)
        turtle.forward(59)
        turtle.end_fill()

        turtle = RawTurtle(self.root, visible=False)
        # root2 = turtle.Turtle()
        turtle.color('#2BB79E')
        turtle.pensize(4)
        turtle.shape('arrow')
        turtle.speed(9)
        turtle.hideturtle()
        turtle.fillcolor("#2BB79E")
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(-150, -150)
        turtle.pendown()
        turtle.forward(300)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(100)
        turtle.forward(90)
        turtle.right(60)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(150)
        turtle.right(90)
        turtle.forward(47)
        turtle.left(110)
        turtle.forward(70)
        turtle.end_fill()

        turtle.color("Black")
        style = ('Arial', 30, 'bold')
        turtle.penup()
        turtle.setposition(1, -200)
        turtle.hideturtle()
        turtle.write('Data Visualizer', font=style, align='center')

        style = ('Arial', 15, 'bold')

        turtle.setposition(1, -230)
        turtle.write('TechieSpod', font=style, align='center')

        style = ('Arial', 10)
        turtle.setposition(1, -260)
        turtle.write('Joy & Khushal', font=style, align='center')

        # ---------------------main tab line-----------------------------
        self.my_notebook = ttk.Notebook(self.m, height=700)
        self.my_notebook.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=0)

        self.my_frm = Frame(self.my_notebook, width=150, height=31.3, background="#e3fff6")
        self.my_frm.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20)
        self.my_notebook.add(self.my_frm, text="Line Graph")

        self.my_frm1 = Frame(self.my_notebook, width=150, height=31.3, background="#e3fff6")
        self.my_frm1.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20)
        self.my_notebook.add(self.my_frm1, text="Bar Graph")

        self.my_frm2 = Frame(self.my_notebook, width=150, height=31.3, background="#e3fff6")
        self.my_frm2.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20)
        self.my_notebook.add(self.my_frm2, text="Histogram")

        self.my_frm3 = Frame(self.my_notebook, width=150, height=31.3, background="#e3fff6")
        self.my_frm3.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20)
        self.my_notebook.add(self.my_frm3, text="Scattered")

        self.my_frmpie = Frame(self.my_notebook, width=150, height=31.3, background="#e3fff6")
        self.my_frmpie.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20)
        self.my_notebook.add(self.my_frmpie, text="Pie Chart")

        self.my_cal = Frame(self.my_notebook, width=150, height=31.3, background="#e3fff6")
        self.my_cal.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20)
        self.my_notebook.add(self.my_cal, text="Calculator")

        self.screen = Entry(self.my_cal, textvariable=self.sc_variable, font='lucida 20 bold', fg='black', bg='white', borderwidth=1, width=30)
        self.screen.grid(row=0, column=0, columnspan=6, pady=20,ipady=20)

        self.b1 = Button(self.my_cal, text='7', font='lucida 15 bold',   fg='#c7ffed', bg='grey',width=5)
        self.b1.grid(row=1, column=0)
        self.b2 = Button(self.my_cal, text='8', font='lucida 15 bold',  fg='#c7ffed', bg='grey',width=5)
        self.b2.grid(row=1, column=1)
        self.b3 = Button(self.my_cal, text='9', font='lucida 15 bold',  fg='#c7ffed', bg='grey', width=5)
        self.b3.grid(row=1, column=2)
        self.b4 = Button(self.my_cal, text='*', font='lucida 15 bold', fg='#c7ffed', bg='grey', width=5)
        self.b4.grid(row=1, column=3)
        self.b5 = Button(self.my_cal, text='sin', font='lucida 15 bold',  fg='#c7ffed', bg='grey',
                    width=5)
        self.b5.grid(row=1, column=4)
        self.b6 = Button(self.my_cal, text='(', font='lucida 15 bold',  fg='#c7ffed', bg='grey', width=5)
        self.b6.grid(row=1, column=5)

        self.b1.bind('<Button-1>', self.getvals)
        self.b2.bind('<Button-1>', self.getvals)
        self.b3.bind('<Button-1>', self.getvals)
        self.b4.bind('<Button-1>', self.getvals)
        self.b5.bind('<Button-1>', self.getvals)
        self.b6.bind('<Button-1>', self.getvals)
        """buttons = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6]
        count = 0
        for l in range(6):
            buttons[count].grid(row=1, column=l)
            count += 1"""


        self.b7 = Button(self.my_cal, text='4', font='lucida 15 bold',   fg='#c7ffed', bg='grey',width=5)
        self.b7.grid(row=2, column=0)
        self.b8 = Button(self.my_cal, text='5', font='lucida 15 bold',   fg='#c7ffed', bg='grey',width=5 )
        self.b8.grid(row=2, column=1)
        self.b9 = Button(self.my_cal, text='6', font='lucida 15 bold',  fg='#c7ffed', bg='grey',width=5 )
        self.b9.grid(row=2, column=2)
        self.b10 = Button(self.my_cal, text='-', font='lucida 15 bold',   fg='#c7ffed', bg='grey',width=5 )
        self.b10.grid(row=2, column=3)
        self.b11 = Button(self.my_cal, text='cos', font='lucida 15 bold',   fg='#c7ffed', bg='grey',width=5)
        self.b11.grid(row=2, column=4)
        self.b12 = Button(self.my_cal, text=')', font='lucida 15 bold',   fg='#c7ffed', bg='grey',width=5)
        self.b12.grid(row=2, column=5)
        self.b7.bind('<Button-1>', self.getvals)
        self.b8.bind('<Button-1>', self.getvals)
        self.b9.bind('<Button-1>', self.getvals)
        self.b10.bind('<Button-1>', self.getvals)
        self.b11.bind('<Button-1>', self.getvals)
        self.b12.bind('<Button-1>', self.getvals)
        """buttons = [b1, b2, b3, b4, b5, b6]
        count = 0
        for i in range(6):
            buttons[count].grid(row=2, column=i)
            count += 1
        self.f = Frame(self.m)"""


        self.b13 = Button(self.my_cal, text='1', font='lucida 15 bold',   fg='#c7ffed', bg='grey', width=5)
        self.b13.grid(row=3, column=0)
        self.b14 = Button(self.my_cal, text='2', font='lucida 15 bold',   fg='#c7ffed', bg='grey', width=5)
        self.b14.grid(row=3, column=1)
        self.b15 = Button(self.my_cal, text='3', font='lucida 15 bold',   fg='#c7ffed', bg='grey', width=5)
        self.b15.grid(row=3, column=2)
        self.b16 = Button(self.my_cal, text='+', font='lucida 15 bold',   fg='#c7ffed', bg='grey', width=5)
        self.b16.grid(row=3, column=3)
        self.b17 = Button(self.my_cal, text='tan', font='lucida 15 bold',   fg='#c7ffed', bg='grey',
                    width=5)
        self.b17.grid(row=3, column=4)
        self.b18 = Button(self.my_cal, text='%', font='lucida 15 bold',   fg='#c7ffed', bg='grey', width=5)
        self.b18.grid(row=3, column=5)
        self.b13.bind('<Button-1>', self.getvals)
        self.b14.bind('<Button-1>', self.getvals)
        self.b15.bind('<Button-1>', self.getvals)
        self.b16.bind('<Button-1>', self.getvals)
        self.b17.bind('<Button-1>', self.getvals)
        self.b18.bind('<Button-1>', self.getvals)


        self.b19 = Button(self.my_cal, text='.', font='lucida 15 bold',   fg='#c7ffed', bg='grey', width=5)
        self.b19.grid(row=4, column=0)
        self.b20 = Button(self.my_cal, text='0', font='lucida 15 bold',   fg='#c7ffed', bg='grey', width=5)
        self.b20.grid(row=4, column=1)
        self.b21 = Button(self.my_cal, text='sinh', font='lucida 15 bold',   fg='#c7ffed', bg='grey',
                    width=5)
        self.b21.grid(row=4, column=2)
        self.b22 = Button(self.my_cal, text='cosh', font='lucida 15 bold',   fg='#c7ffed', bg='grey',
                    width=5)
        self.b22.grid(row=4, column=3)
        self.b23 = Button(self.my_cal, text='tanh', font='lucida 15 bold',   fg='#c7ffed', bg='grey',
                    width=5)
        self.b23.grid(row=4, column=4)
        self.b24 = Button(self.my_cal, text='pi', font='lucida 15 bold',  fg='#c7ffed', bg='grey',
                    width=5)
        self.b24.grid(row=4, column=5)
        self.b19.bind('<Button-1>', self.getvals)
        self.b20.bind('<Button-1>', self.getvals)
        self.b21.bind('<Button-1>', self.getvals)
        self.b22.bind('<Button-1>', self.getvals)
        self.b23.bind('<Button-1>', self.getvals)
        self.b24.bind('<Button-1>', self.getvals)



        self.b25 = Button(self.my_cal, text='log10', font='lucida 15 bold',   fg='#c7ffed', bg='grey',
                    width=5)
        self.b25.grid(row=5, column=0)
        self.b26 = Button(self.my_cal, text='exp', font='lucida 15 bold',   fg='#c7ffed', bg='grey',
                    width=5)
        self.b26.grid(row=5, column=1)
        self.b27 = Button(self.my_cal, text='/', font='lucida 15 bold',   fg='#c7ffed', bg='grey', width=5)
        self.b27.grid(row=5, column=2)
        self.b28 = Button(self.my_cal, text='Clr', font='lucida 15 bold',   fg='#c7ffed', bg='grey',
                    width=5)
        self.b28.grid(row=5, column=3)
        self.b29 = Button(self.my_cal, text='log', font='lucida 15 bold',   fg='#c7ffed', bg='grey',
                    width=5)
        self.b29.grid(row=5, column=4)
        self.b30 = Button(self.my_cal, text='=', font='lucida 15 bold',   fg='#c7ffed', bg='grey', width=5)
        self.b30.grid(row=5, column=5)
        self.b25.bind('<Button-1>', self.getvals)
        self.b26.bind('<Button-1>', self.getvals)
        self.b27.bind('<Button-1>', self.getvals)
        self.b28.bind('<Button-1>', self.getvals)
        self.b29.bind('<Button-1>', self.getvals)
        self.b30.bind('<Button-1>', self.getvals)

        self.status_var = StringVar()
        self.status_var.set('Ready..')

        # ---------------------line graph tab-----------------------------
        self.my_notebook1 = ttk.Notebook(self.my_frm, height=700)
        self.my_notebook1.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=20)

        self.my_frm_sub = Frame(self.my_notebook1, width=150, height=31.3, background="#e3fff6")
        self.my_frm_sub.grid()
        self.my_notebook1.add(self.my_frm_sub, text="Single Line Graphs")

        self.my_frm_sub_1 = Frame(self.my_notebook1, width=150, height=31.3, background="#e3fff6")
        self.my_frm_sub_1.grid()
        self.my_notebook1.add(self.my_frm_sub_1, text="Double Line Graphs")
        # ---------------------main tab bar-----------------------------

        self.my_notebook2 = ttk.Notebook(self.my_frm1, height=700)
        self.my_notebook2.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=20)

        self.my_frm_sub_bar1 = Frame(self.my_notebook2, width=150, height=31.3, background="#e3fff6")
        self.my_frm_sub_bar1.grid()
        self.my_notebook2.add(self.my_frm_sub_bar1, text="Single Bar Graphs")

        self.my_frm_sub_bar2 = Frame(self.my_notebook2, width=150, height=31.3, background="#e3fff6")
        self.my_frm_sub_bar2.grid()
        self.my_notebook2.add(self.my_frm_sub_bar2, text="Double Bar Graphs")

        # ------------------------------------Histogram--------------------------------------

        self.my_notebook3 = ttk.Notebook(self.my_frm2, height=700)
        self.my_notebook3.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=20)

        self.my_frm_sub_bar3 = Frame(self.my_notebook3, width=150, height=31.3, background="#e3fff6")
        self.my_frm_sub_bar3.grid()
        self.my_notebook3.add(self.my_frm_sub_bar3, text="Histogram (raw data)")

        self.my_frm_sub_bar4 = Frame(self.my_notebook3, width=150, height=31.3, background="#e3fff6")
        self.my_frm_sub_bar4.grid()
        self.my_notebook3.add(self.my_frm_sub_bar4, text="Histogram (frequency)")

        # ------------------------------------Scattered--------------------------------------

        self.my_notebook4 = ttk.Notebook(self.my_frm3, height=700)
        self.my_notebook4.grid(row=0, column=1, columnspan=2, sticky="nsew", padx=20)

        self.my_frm_sub_scattered_s = Frame(self.my_notebook4, width=150, height=31.3, background="#e3fff6")
        self.my_frm_sub_scattered_s.grid()
        self.my_notebook4.add(self.my_frm_sub_scattered_s, text="Single Scattering")

        self.my_frm_sub_scattered_d = Frame(self.my_notebook4, width=150, height=31.3, background="#e3fff6")
        self.my_frm_sub_scattered_d.grid()
        self.my_notebook4.add(self.my_frm_sub_scattered_d, text="Double Scattering")

        self.my_frm_sub_scattered_3d = Frame(self.my_notebook4, width=150, height=31.3, background="#e3fff6")
        self.my_frm_sub_scattered_3d.grid()
        self.my_notebook4.add(self.my_frm_sub_scattered_3d, text="3D Scattering")

        """my_frm1 = Frame(my_notebook, width=150, height=31.3, background="#e6ffe6", borderwidth=0)
        my_frm1.grid()
        my_notebook.add(my_frm1, text="Single Bar Graph")"""
        # -------------------------------Menu-----------------------------------
        my_menu = Menu(self.m)
        self.m.config(menu=my_menu)
        self.new = 1
        self.url = "https://www.techiespod.com/contact"

        file_menu = Menu(my_menu, tearoff=False, font=('Consolas', 11))
        my_menu.add_cascade(label="File", menu=file_menu)
        
        file_menu.add_command(label="Save", command=self.save_as_png)
        """file_menu.add_command(label="Save As")"""
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)


        # Theme menu
        theme_menu = Menu(my_menu, tearoff=False, font=('Consolas', 11))
        my_menu.add_cascade(label="Theme", menu=theme_menu)
        theme_menu.add_command(label="Dark Theme", command=self.dark)
        theme_menu.add_command(label="Default Theme", command=self.default)

        # Cal menu
        cal_menu = Menu(my_menu, tearoff=False, font=('Consolas', 11))
        my_menu.add_cascade(label="Calculation", menu=cal_menu)
        cal_menu.add_command(label="Open Calculator", command=self.show)

        # Help menu
        help_menu = Menu(my_menu, tearoff=False, font=('Consolas', 11))
        my_menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Contact Us", command=self.openweb)

        # -------------------------------Side Pannel single graph (line)-----------------------------------

        self.title = Label(self.my_frm_sub, text="Single Line Graph :)", font=('Consolas', 20), background="#e3fff6")
        self.title.grid(row=0, column=1, columnspan=2, pady=20)

        self.ip_X = Label(self.my_frm_sub, text="X-Coordinate : ", background="#e3fff6")
        self.ip_X.grid(row=1, column=1, padx=20, pady=10)

        self.ip_X_ent = Entry(self.my_frm_sub, width=30, textvariable=self.x)
        self.ip_X_ent.grid(row=1, column=2, pady=10, padx=20)

        self.ip_Y = Label(self.my_frm_sub, text="Y-Coordinate : ", background="#e3fff6")
        self.ip_Y.grid(row=2, column=1, pady=10, padx=20)

        self.ip_Y_ent = Entry(self.my_frm_sub, width=30, textvariable=self.y)
        self.ip_Y_ent.grid(row=2, column=2, pady=10, padx=20)

        self.lbl_x = Label(self.my_frm_sub, text="X-Coordinate Name : ", background="#e3fff6")
        self.lbl_x.grid(row=3, column=1, pady=10, padx=20)

        self.lbl_x_ent = Entry(self.my_frm_sub, textvariable=self.xname)
        self.lbl_x_ent.grid(row=3, column=2, pady=10, padx=20)

        self.lbl_y = Label(self.my_frm_sub, text="Y-Coordinate Name : ", background="#e3fff6")
        self.lbl_y.grid(row=4, column=1, pady=10, padx=20)

        self.lbl_y_ent = Entry(self.my_frm_sub, textvariable=self.yname)
        self.lbl_y_ent.grid(row=4, column=2, pady=10, padx=20)

        self.gen_graph = Button(self.my_frm_sub, text="Generate Graph", width=15,
                                command=self.Generate_Graph_singleline)
        self.gen_graph.grid(row=5, column=1, pady=10, padx=20)

        self.reset = Button(self.my_frm_sub, text="Reset", width=15, command=self.reset_it)
        self.reset.grid(row=5, column=2, pady=10, padx=20)

        # -------------------------------Side Pannel double graph (line)-----------------------------------

        self.title_ = Label(self.my_frm_sub_1, text="Double Line Graph :)", font=('Consolas', 20), background="#e3fff6")
        self.title_.grid(row=0, column=1, columnspan=2, pady=20)

        self.ip_1X_ = Label(self.my_frm_sub_1, text="X1-Coordinate : ", background="#e3fff6")
        self.ip_1X_.grid(row=1, column=1, padx=20, pady=10)

        self.ip_1X_ent_ = Entry(self.my_frm_sub_1, width=30, textvariable=self.x_double_1)
        self.ip_1X_ent_.grid(row=1, column=2, pady=10, padx=20)

        self.ip_1Y_ = Label(self.my_frm_sub_1, text="Y1-Coordinate : ", background="#e3fff6")
        self.ip_1Y_.grid(row=2, column=1, pady=10, padx=20)

        self.ip_1Y_ent_ = Entry(self.my_frm_sub_1, width=30, textvariable=self.y_double_1)
        self.ip_1Y_ent_.grid(row=2, column=2, pady=10, padx=20)

        self.ip_2X_ = Label(self.my_frm_sub_1, text="X2-Coordinate : ", background="#e3fff6")
        self.ip_2X_.grid(row=3, column=1, padx=20, pady=10)

        self.ip_2X_ent_ = Entry(self.my_frm_sub_1, width=30, textvariable=self.x_double_2)
        self.ip_2X_ent_.grid(row=3, column=2, pady=10, padx=20)

        self.ip_2Y_ = Label(self.my_frm_sub_1, text="Y2-Coordinate : ", background="#e3fff6")
        self.ip_2Y_.grid(row=4, column=1, pady=10, padx=20)

        self.ip_2Y_ent_ = Entry(self.my_frm_sub_1, width=30, textvariable=self.y_double_2)
        self.ip_2Y_ent_.grid(row=4, column=2, pady=10, padx=20)

        self.lbl_2x_ = Label(self.my_frm_sub_1, text="X-Coordinate Name : ", background="#e3fff6")
        self.lbl_2x_.grid(row=5, column=1, pady=20, padx=20)

        self.lbl_2x_ent_ = Entry(self.my_frm_sub_1, textvariable=self.x_doublename)
        self.lbl_2x_ent_.grid(row=5, column=2, pady=20, padx=20)

        self.lbl_2y_ = Label(self.my_frm_sub_1, text="Y-Coordinate Name : ", background="#e3fff6")
        self.lbl_2y_.grid(row=6, column=1, pady=20, padx=20)

        self.lbl_2y_ent_ = Entry(self.my_frm_sub_1, textvariable=self.y_doublename)
        self.lbl_2y_ent_.grid(row=6, column=2, pady=20, padx=20)

        self.lbl_2x_leg_ = Label(self.my_frm_sub_1, text="1st ledgend : ", background="#e3fff6")
        self.lbl_2x_leg_.grid(row=7, column=1, pady=20, padx=20)

        self.lbl_2x_ent_leg_ = Entry(self.my_frm_sub_1, textvariable=self.x_doublename_real)
        self.lbl_2x_ent_leg_.grid(row=7, column=2, pady=20, padx=20)

        self.lbl_2y_leg_ = Label(self.my_frm_sub_1, text="2st ledgend : ", background="#e3fff6")
        self.lbl_2y_leg_.grid(row=8, column=1, pady=20, padx=20)

        self.lbl_2y_ent_leg_ = Entry(self.my_frm_sub_1, textvariable=self.y_doublename_real)
        self.lbl_2y_ent_leg_.grid(row=8, column=2, pady=20, padx=20)

        self.gen_graph_ = Button(self.my_frm_sub_1, text="Generate Graph", width=15,
                                 command=self.Generate_Graph_doubleline)
        self.gen_graph_.grid(row=9, column=1, pady=20, padx=20)

        self.reset_ = Button(self.my_frm_sub_1, text="Reset", width=15, command=self.reset_it)
        self.reset_.grid(row=9, column=2, pady=20, padx=20)

        # -------------------------------------Bar Single Graph--------------------------------------------
        self.title1 = Label(self.my_frm_sub_bar1, text="Single Line Bar Graph :)", font=('Consolas', 20),
                            background="#e3fff6")
        self.title1.grid(row=0, column=1, columnspan=2, pady=20)

        self.ip_X1 = Label(self.my_frm_sub_bar1, text="X-Coordinate : ", background="#e3fff6")
        self.ip_X1.grid(row=1, column=1, pady=20, padx=20)

        self.ip_X_ent1 = Entry(self.my_frm_sub_bar1, width=30, textvariable=self.x1)
        self.ip_X_ent1.grid(row=1, column=2, pady=20, padx=20)

        self.ip_Y1 = Label(self.my_frm_sub_bar1, text="Y-Coordinate : ", background="#e3fff6")
        self.ip_Y1.grid(row=2, column=1, pady=20, padx=20)

        self.ip_Y_ent1 = Entry(self.my_frm_sub_bar1, width=30, textvariable=self.y1)
        self.ip_Y_ent1.grid(row=2, column=2, pady=20, padx=20)

        self.lbl_x1 = Label(self.my_frm_sub_bar1, text="X-Coordinate Name : ", background="#e3fff6")
        self.lbl_x1.grid(row=3, column=1, pady=20, padx=20)

        self.lbl_x_ent1 = Entry(self.my_frm_sub_bar1, width=30, textvariable=self.x1_name)
        self.lbl_x_ent1.grid(row=3, column=2, pady=20, padx=20)

        self.lbl_y1 = Label(self.my_frm_sub_bar1, text="Y-Coordinate Name : ", background="#e3fff6")
        self.lbl_y1.grid(row=4, column=1, pady=20, padx=20)

        self.lbl_y_ent1 = Entry(self.my_frm_sub_bar1, width=30, textvariable=self.y1_name)
        self.lbl_y_ent1.grid(row=4, column=2, pady=20, padx=20)

        self.gen_graph1 = Button(self.my_frm_sub_bar1, text="Generate Graph", width=15,
                                 command=self.Generate_Graph_bar_S)
        self.gen_graph1.grid(row=5, column=1, pady=20, padx=20)

        self.reset1 = Button(self.my_frm_sub_bar1, text="Reset", width=15, command=self.reset_it)
        self.reset1.grid(row=5, column=2, pady=20, padx=20)

        # -------------------------------------Bar Double Graph--------------------------------------------
        self.title_bar_1 = Label(self.my_frm_sub_bar2, text="Double Line Bar Graph :)", font=('Consolas', 20),
                                 background="#e3fff6")
        self.title_bar_1.grid(row=0, column=1, columnspan=2, pady=20)

        self.ip_bar_X1 = Label(self.my_frm_sub_bar2, text="X-Coordinate : ", background="#e3fff6")
        self.ip_bar_X1.grid(row=1, column=1, pady=20, padx=20)

        self.ip_X_bar_ent1 = Entry(self.my_frm_sub_bar2, width=30, textvariable=self.x_bar_)
        self.ip_X_bar_ent1.grid(row=1, column=2, pady=20, padx=20)

        self.ip_bar_Y1 = Label(self.my_frm_sub_bar2, text="Y-Coordinate : ", background="#e3fff6")
        self.ip_bar_Y1.grid(row=2, column=1, pady=20, padx=20)

        self.ip_Y_bar_ent1 = Entry(self.my_frm_sub_bar2, width=30, textvariable=self.y_bar_)
        self.ip_Y_bar_ent1.grid(row=2, column=2, pady=20, padx=20)

        self.lbl_bar_x1 = Label(self.my_frm_sub_bar2, text="1st Ledgend : ", background="#e3fff6")
        self.lbl_bar_x1.grid(row=3, column=1, pady=20, padx=20)

        self.lbl_x_bar_ent1 = Entry(self.my_frm_sub_bar2, textvariable=self.x_bar_name)
        self.lbl_x_bar_ent1.grid(row=3, column=2, pady=20, padx=20)

        self.lbl_bar_y1 = Label(self.my_frm_sub_bar2, text="2st Ledgend : ", background="#e3fff6")
        self.lbl_bar_y1.grid(row=4, column=1, pady=20, padx=20)

        self.lbl_y_bar_ent1 = Entry(self.my_frm_sub_bar2, textvariable=self.y_bar_name)
        self.lbl_y_bar_ent1.grid(row=4, column=2, pady=20, padx=20)

        self.lbl_bar_x1_axix = Label(self.my_frm_sub_bar2, text="X-Coordinate Name : ", background="#e3fff6")
        self.lbl_bar_x1_axix.grid(row=5, column=1, pady=20, padx=20)

        self.lbl_x_bar_ent1_axix = Entry(self.my_frm_sub_bar2, textvariable=self.x_bar_name_axix)
        self.lbl_x_bar_ent1_axix.grid(row=5, column=2, pady=20, padx=20)

        self.lbl_bar_y1_axix = Label(self.my_frm_sub_bar2, text="Y-Coordinate Name : ", background="#e3fff6")
        self.lbl_bar_y1_axix.grid(row=6, column=1, pady=20, padx=20)

        self.lbl_y_bar_ent1_axix = Entry(self.my_frm_sub_bar2, textvariable=self.y_bar_name_axix)
        self.lbl_y_bar_ent1_axix.grid(row=6, column=2, pady=20, padx=20)

        self.gen_graph_bar_ = Button(self.my_frm_sub_bar2, text="Generate Graph", width=15,
                                     command=self.Generate_Graph_bar_D)
        self.gen_graph_bar_.grid(row=7, column=1, pady=20, padx=20)

        self.reset_bar_ = Button(self.my_frm_sub_bar2, text="Reset", width=15, command=self.reset_it)
        self.reset_bar_.grid(row=7, column=2, pady=20, padx=20)

        # -------------------------------------Histogram (Raw Data)--------------------------------------------
        self.title_bar_2 = Label(self.my_frm_sub_bar3, text="Histogram (Raw Data) :)", font=('Consolas', 20),
                                 background="#e3fff6")
        self.title_bar_2.grid(row=0, column=1, columnspan=2, pady=20)

        self.ip_bar_X2 = Label(self.my_frm_sub_bar3, text="Raw Data (Y-Axis) : ", background="#e3fff6")
        self.ip_bar_X2.grid(row=1, column=1, pady=20, padx=20)

        self.ip_X_bar_ent2 = Entry(self.my_frm_sub_bar3, width=30, textvariable=self.x_bar_hist)
        self.ip_X_bar_ent2.grid(row=1, column=2, pady=20, padx=20)

        self.ip_bar_Y2 = Label(self.my_frm_sub_bar3, text="Interval (X-Axis) : ", background="#e3fff6")
        self.ip_bar_Y2.grid(row=2, column=1, pady=20, padx=20)

        self.ip_Y_bar_ent2 = Entry(self.my_frm_sub_bar3, width=30, textvariable=self.y_bar_hist)
        self.ip_Y_bar_ent2.grid(row=2, column=2, pady=20, padx=20)

        self.lbl_bar_x2 = Label(self.my_frm_sub_bar3, text="X-Coordinate Name : ", background="#e3fff6")
        self.lbl_bar_x2.grid(row=3, column=1, pady=20, padx=20)

        self.lbl_x_bar_ent2 = Entry(self.my_frm_sub_bar3, textvariable=self.x_bar_hist_name)
        self.lbl_x_bar_ent2.grid(row=3, column=2, pady=20, padx=20)

        self.lbl_bar_y2 = Label(self.my_frm_sub_bar3, text="Y-Coordinate Name : ", background="#e3fff6")
        self.lbl_bar_y2.grid(row=4, column=1, pady=20, padx=20)

        self.lbl_y_bar_ent2 = Entry(self.my_frm_sub_bar3, textvariable=self.y_bar_hist_name)
        self.lbl_y_bar_ent2.grid(row=4, column=2, pady=20, padx=20)

        self.gen_graph_bar_2 = Button(self.my_frm_sub_bar3, text="Generate Graph", width=15,
                                      command=self.Generate_Graph_bar_Hist)
        self.gen_graph_bar_2.grid(row=5, column=1, pady=20, padx=20)

        self.reset_bar_2 = Button(self.my_frm_sub_bar3, text="Reset", width=15, command=self.reset_it)
        self.reset_bar_2.grid(row=5, column=2, pady=20, padx=20)

        # -------------------------------------Histogram (Frequency)--------------------------------------------
        self.title_bar_2_f = Label(self.my_frm_sub_bar4, text="Histogram (Frequency) :)", font=('Consolas', 20),
                                   background="#e3fff6")
        self.title_bar_2_f.grid(row=0, column=1, columnspan=2, pady=20)

        self.ip_bar_X2_f = Label(self.my_frm_sub_bar4, text="Raw Data (Y-Axis) : ", background="#e3fff6")
        self.ip_bar_X2_f.grid(row=1, column=1, pady=20, padx=20)

        self.ip_X_bar_ent2_f = Entry(self.my_frm_sub_bar4, width=30, textvariable=self.x_bar_hist_f)
        self.ip_X_bar_ent2_f.grid(row=1, column=2, pady=20, padx=20)

        self.ip_bar_Y2_f = Label(self.my_frm_sub_bar4, text="Interval (X-Axis) : ", background="#e3fff6")
        self.ip_bar_Y2_f.grid(row=2, column=1, pady=20, padx=20)

        self.ip_Y_bar_ent2_f = Entry(self.my_frm_sub_bar4, width=30, textvariable=self.y_bar_hist_f)
        self.ip_Y_bar_ent2_f.grid(row=2, column=2, pady=20, padx=20)

        self.lbl_bar_x2_f = Label(self.my_frm_sub_bar4, text="X-Coordinate Name : ", background="#e3fff6")
        self.lbl_bar_x2_f.grid(row=3, column=1, pady=20, padx=20)

        self.lbl_x_bar_ent2_f = Entry(self.my_frm_sub_bar4, textvariable=self.x_bar_hist_name_f)
        self.lbl_x_bar_ent2_f.grid(row=3, column=2, pady=20, padx=20)

        self.lbl_bar_y2_f = Label(self.my_frm_sub_bar4, text="Y-Coordinate Name : ", background="#e3fff6")
        self.lbl_bar_y2_f.grid(row=4, column=1, pady=20, padx=20)

        self.lbl_y_bar_ent2_f = Entry(self.my_frm_sub_bar4, textvariable=self.y_bar_hist_name_f)
        self.lbl_y_bar_ent2_f.grid(row=4, column=2, pady=20, padx=20)

        self.gen_graph_bar_2_f = Button(self.my_frm_sub_bar4, text="Generate Graph", width=15,
                                        command=self.Generate_Graph_bar_Hist_frequency)
        self.gen_graph_bar_2_f.grid(row=5, column=1, pady=20, padx=20)

        self.reset_bar_2_f = Button(self.my_frm_sub_bar4, text="Reset", width=15, command=self.reset_it)
        self.reset_bar_2_f.grid(row=5, column=2, pady=20, padx=20)

        # -------------------------------Scattering Single-----------------------------------

        self.title_scattering_s = Label(self.my_frm_sub_scattered_s, text="Single Scattering :)", font=('Consolas', 20),
                                        background="#e3fff6")
        self.title_scattering_s.grid(row=0, column=1, columnspan=2, pady=20)

        self.ip_X_scattering_s = Label(self.my_frm_sub_scattered_s, text="X-Coordinate : ", background="#e3fff6")
        self.ip_X_scattering_s.grid(row=1, column=1, padx=20, pady=10)

        self.ip_X_ent_scattering_s = Entry(self.my_frm_sub_scattered_s, width=30, textvariable=self.x_scattered_s)
        self.ip_X_ent_scattering_s.grid(row=1, column=2, pady=10, padx=20)

        self.ip_Y_scattering_s = Label(self.my_frm_sub_scattered_s, text="Y-Coordinate : ", background="#e3fff6")
        self.ip_Y_scattering_s.grid(row=2, column=1, pady=10, padx=20)

        self.ip_Y_ent_scattering_s = Entry(self.my_frm_sub_scattered_s, width=30, textvariable=self.y_scattered_s)
        self.ip_Y_ent_scattering_s.grid(row=2, column=2, pady=10, padx=20)

        self.lbl_x_scattering_s = Label(self.my_frm_sub_scattered_s, text="X-Coordinate Name : ", background="#e3fff6")
        self.lbl_x_scattering_s.grid(row=3, column=1, pady=10, padx=20)

        self.lbl_x_ent_scattering_s = Entry(self.my_frm_sub_scattered_s, textvariable=self.x_scattered_name_s)
        self.lbl_x_ent_scattering_s.grid(row=3, column=2, pady=10, padx=20)

        self.lbl_y_scattering_s = Label(self.my_frm_sub_scattered_s, text="Y-Coordinate Name : ", background="#e3fff6")
        self.lbl_y_scattering_s.grid(row=4, column=1, pady=10, padx=20)

        self.lbl_y_ent_scattering_s = Entry(self.my_frm_sub_scattered_s, textvariable=self.y_scattered_name_s)
        self.lbl_y_ent_scattering_s.grid(row=4, column=2, pady=10, padx=20)

        self.gen_graph_scattering_s = Button(self.my_frm_sub_scattered_s, text="Generate Graph", width=15,
                                             command=self.Generate_Graph_scattered_s)
        self.gen_graph_scattering_s.grid(row=5, column=1, pady=10, padx=20)

        self.reset_scattering_s = Button(self.my_frm_sub_scattered_s, text="Reset", width=15, command=self.reset_it)
        self.reset_scattering_s.grid(row=5, column=2, pady=10, padx=20)

        # -------------------------------Scattering 3D-----------------------------------

        self.title_scattering_3d = Label(self.my_frm_sub_scattered_3d, text="Single Scattering :)",
                                         font=('Consolas', 20),
                                         background="#e3fff6")
        self.title_scattering_3d.grid(row=0, column=1, columnspan=2, pady=20)

        self.ip_X_scattering_3d = Label(self.my_frm_sub_scattered_3d, text="X-Coordinate : ", background="#e3fff6")
        self.ip_X_scattering_3d.grid(row=1, column=1, padx=20, pady=10)

        self.ip_X_ent_scattering_3d = Entry(self.my_frm_sub_scattered_3d, width=30, textvariable=self.x_scattered_3d)
        self.ip_X_ent_scattering_3d.grid(row=1, column=2, pady=10, padx=20)

        self.ip_Y_scattering_3d = Label(self.my_frm_sub_scattered_3d, text="Y-Coordinate : ", background="#e3fff6")
        self.ip_Y_scattering_3d.grid(row=2, column=1, pady=10, padx=20)

        self.ip_Y_ent_scattering_3d = Entry(self.my_frm_sub_scattered_3d, width=30, textvariable=self.y_scattered_3d)
        self.ip_Y_ent_scattering_3d.grid(row=2, column=2, pady=10, padx=20)

        self.ip_Z_scattering_3d = Label(self.my_frm_sub_scattered_3d, text="Z-Coordinate : ", background="#e3fff6")
        self.ip_Z_scattering_3d.grid(row=3, column=1, pady=10, padx=20)

        self.ip_Z_ent_scattering_3d = Entry(self.my_frm_sub_scattered_3d, width=30, textvariable=self.z_scattered_3d)
        self.ip_Z_ent_scattering_3d.grid(row=3, column=2, pady=10, padx=20)

        self.lbl_x_scattering_3d = Label(self.my_frm_sub_scattered_3d, text="X-Coordinate Name : ",
                                         background="#e3fff6")
        self.lbl_x_scattering_3d.grid(row=4, column=1, pady=10, padx=20)

        self.lbl_x_ent_scattering_3d = Entry(self.my_frm_sub_scattered_3d, textvariable=self.x_scattered_name_3d)
        self.lbl_x_ent_scattering_3d.grid(row=4, column=2, pady=10, padx=20)

        self.lbl_y_scattering_3d = Label(self.my_frm_sub_scattered_3d, text="Y-Coordinate Name : ",
                                         background="#e3fff6")
        self.lbl_y_scattering_3d.grid(row=5, column=1, pady=10, padx=20)

        self.lbl_y_ent_scattering_3d = Entry(self.my_frm_sub_scattered_3d, textvariable=self.y_scattered_name_3d)
        self.lbl_y_ent_scattering_3d.grid(row=5, column=2, pady=10, padx=20)

        self.lbl_z_scattering_3d = Label(self.my_frm_sub_scattered_3d, text="Z-Coordinate Name : ",
                                         background="#e3fff6")
        self.lbl_z_scattering_3d.grid(row=6, column=1, pady=10, padx=20)

        self.lbl_z_ent_scattering_3d = Entry(self.my_frm_sub_scattered_3d, textvariable=self.z_scattered_name_3d)
        self.lbl_z_ent_scattering_3d.grid(row=6, column=2, pady=10, padx=20)

        self.gen_graph_scattering_3d = Button(self.my_frm_sub_scattered_3d, text="Generate Graph", width=15,
                                              command=self.Generate_Graph_scattered_3d)
        self.gen_graph_scattering_3d.grid(row=7, column=1, pady=10, padx=20)

        self.reset_scattering_3d = Button(self.my_frm_sub_scattered_3d, text="Reset", width=15, command=self.reset_it)
        self.reset_scattering_3d.grid(row=7, column=2, pady=10, padx=20)

        # -------------------------------Scattered Double-----------------------------------

        self.title_scattering_d = Label(self.my_frm_sub_scattered_d, text="Double Scattering :)", font=('Consolas', 20),
                                        background="#e3fff6")
        self.title_scattering_d.grid(row=0, column=1, columnspan=2, pady=20)

        self.ip_1X_scattering_d = Label(self.my_frm_sub_scattered_d, text="X1-Coordinate : ", background="#e3fff6")
        self.ip_1X_scattering_d.grid(row=1, column=1, padx=20, pady=10)

        self.ip_1X_ent_scattering_d = Entry(self.my_frm_sub_scattered_d, width=30, textvariable=self.x_scattered_d1)
        self.ip_1X_ent_scattering_d.grid(row=1, column=2, pady=10, padx=20)

        self.ip_1Y_scattering_d = Label(self.my_frm_sub_scattered_d, text="Y1-Coordinate : ", background="#e3fff6")
        self.ip_1Y_scattering_d.grid(row=2, column=1, pady=10, padx=20)

        self.ip_1Y_ent_scattering_d = Entry(self.my_frm_sub_scattered_d, width=30, textvariable=self.y_scattered_d1)
        self.ip_1Y_ent_scattering_d.grid(row=2, column=2, pady=10, padx=20)

        self.ip_2X_scattering_d = Label(self.my_frm_sub_scattered_d, text="X2-Coordinate : ", background="#e3fff6")
        self.ip_2X_scattering_d.grid(row=3, column=1, padx=20, pady=10)

        self.ip_2X_ent_scattering_d = Entry(self.my_frm_sub_scattered_d, width=30, textvariable=self.x_scattered_d2)
        self.ip_2X_ent_scattering_d.grid(row=3, column=2, pady=10, padx=20)

        self.ip_2Y_scattering_d = Label(self.my_frm_sub_scattered_d, text="Y2-Coordinate : ", background="#e3fff6")
        self.ip_2Y_scattering_d.grid(row=4, column=1, pady=10, padx=20)

        self.ip_2Y_ent_scattering_d = Entry(self.my_frm_sub_scattered_d, width=30, textvariable=self.y_scattered_d2)
        self.ip_2Y_ent_scattering_d.grid(row=4, column=2, pady=10, padx=20)

        self.lbl_2x_scattering_d = Label(self.my_frm_sub_scattered_d, text="X-Coordinate Name : ", background="#e3fff6")
        self.lbl_2x_scattering_d.grid(row=5, column=1, pady=20, padx=20)

        self.lbl_2x_ent_scattering_d = Entry(self.my_frm_sub_scattered_d, textvariable=self.x_scattered_name_d1)
        self.lbl_2x_ent_scattering_d.grid(row=5, column=2, pady=20, padx=20)

        self.lbl_2y_scattering_d = Label(self.my_frm_sub_scattered_d, text="Y-Coordinate Name : ", background="#e3fff6")
        self.lbl_2y_scattering_d.grid(row=6, column=1, pady=20, padx=20)

        self.lbl_2y_ent_scattering_d = Entry(self.my_frm_sub_scattered_d, textvariable=self.y_scattered_name_d1)
        self.lbl_2y_ent_scattering_d.grid(row=6, column=2, pady=20, padx=20)

        self.lbl_2x_scattering_d_leg = Label(self.my_frm_sub_scattered_d, text="1st Ledgend : ", background="#e3fff6")
        self.lbl_2x_scattering_d_leg.grid(row=7, column=1, pady=20, padx=20)

        self.lbl_2x_ent_scattering_d_leg = Entry(self.my_frm_sub_scattered_d, textvariable=self.x_scattered_name_d2)
        self.lbl_2x_ent_scattering_d_leg.grid(row=7, column=2, pady=20, padx=20)

        self.lbl_2y_scattering_d_leg = Label(self.my_frm_sub_scattered_d, text="2st Ledgend : ", background="#e3fff6")
        self.lbl_2y_scattering_d_leg.grid(row=8, column=1, pady=20, padx=20)

        self.lbl_2y_ent_scattering_d = Entry(self.my_frm_sub_scattered_d, textvariable=self.y_scattered_name_d2)
        self.lbl_2y_ent_scattering_d.grid(row=8, column=2, pady=20, padx=20)

        self.gen_graph_scattering_d = Button(self.my_frm_sub_scattered_d, text="Generate Graph", width=15,
                                             command=self.Generate_Graph_scattered_d)
        self.gen_graph_scattering_d.grid(row=9, column=1, pady=20, padx=20)

        self.reset_scattering_d = Button(self.my_frm_sub_scattered_d, text="Reset", width=15, command=self.reset_it)
        self.reset_scattering_d.grid(row=9, column=2, pady=20, padx=20)

        # -------------------------------------Pie Chart--------------------------------------------
        self.title_bar_2_ = Label(self.my_frmpie, text="Pie Chart :)", font=('Consolas', 20),
                                  background="#e3fff6")
        self.title_bar_2_.grid(row=0, column=1, columnspan=2, pady=20)

        self.ip_bar_X2_ = Label(self.my_frmpie, text="Chart Label : ", background="#e3fff6")
        self.ip_bar_X2_.grid(row=1, column=1, pady=20, padx=20)

        self.ip_X_bar_ent2_ = Entry(self.my_frmpie, width=30, textvariable=self.pie_lable)
        self.ip_X_bar_ent2_.grid(row=1, column=2, pady=20, padx=20)

        self.ip_bar_Y2_ = Label(self.my_frmpie, text="Chart Data : ", background="#e3fff6")
        self.ip_bar_Y2_.grid(row=2, column=1, pady=20, padx=20)

        self.ip_Y_bar_ent2_ = Entry(self.my_frmpie, width=30, textvariable=self.pie_data)
        self.ip_Y_bar_ent2_.grid(row=2, column=2, pady=20, padx=20)

        self.gen_graph_bar_2 = Button(self.my_frmpie, text="Generate Graph", width=15,
                                      command=self.Generate_Graph_pie_chart)
        self.gen_graph_bar_2.grid(row=5, column=1, pady=20, padx=20)

        self.reset_bar_2 = Button(self.my_frmpie, text="Reset", width=15, command=self.reset_it)
        self.reset_bar_2.grid(row=5, column=2, pady=20, padx=20)

    def show(self):
        """self.my_cal = Frame(self.my_notebook, width=150, height=31.3, background="#e3fff6")
        self.my_cal.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=20)
        self.my_notebook.add(self.my_cal, text="Calculator")"""
        messagebox.showinfo("Information", "Calculator tab is in side pannel")

    def openweb(self):
        webbrowser.open(self.url, new=self.new)

    def reset_it(self):
        self.canvas.destroy()

        self.canvas_again()

    def canvas_again(self):
        self.canvas = Canvas(self.m, width=1010, height=700, highlightbackground="green", highlightcolor="green",
                             highlightthickness=1, bg="#a2a3a2")
        self.canvas.grid(row=0, rowspan=20, padx=20, pady=20)


    def Generate_Graph_singleline(self):
        self.reset_it()
        # self.canvas.delete("all")
        if (self.x.get() == "") or (self.y.get() == ""):

            self.oops1 = PhotoImage(file='oops.png')
            self.canvas.create_image(500, 400, image=self.oops1)

        else:
            self.canvas.delete("all")
            self.X = self.x.get()
            self.Y = self.y.get()
            fig = Figure(figsize=(6, 6), dpi=90)
            plot1 = fig.add_subplot(111)
            self.XX = list(self.X.split(","))
            self.YY = list(self.Y.split(","))
            for i in range(0, len(self.XX)):
                self.XX[i] = float(self.XX[i])

            for i in range(0, len(self.YY)):
                self.YY[i] = float(self.YY[i])

            plot1.plot(self.XX, self.YY)
            plot1.set_xlabel(self.xname.get())
            plot1.set_ylabel(self.yname.get())
            plot1.set_title("www.techiespod.com")

            canvas = FigureCanvasTkAgg(fig, master=self.canvas)
            canvas.draw()
            canvas.get_tk_widget().pack(padx=250, pady=81)
            # grid(padx=250, pady=125)
            toolbar = NavigationToolbar2Tk(canvas, self.m)
            toolbar.update()
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
            self.canvas.delete("all")

    def Generate_Graph_doubleline(self):
        self.reset_it()
        # self.canvas.delete("all")
        if (self.x_double_1.get() == "") or (self.y_double_1.get() == "") or (self.x_double_2.get() == "") or (
                self.y_double_2.get() == ""):

            self.oops1 = PhotoImage(file='oops.png')
            self.canvas.create_image(500, 400, image=self.oops1)

        else:
            self.canvas.delete("all")
            self.X_1 = self.x_double_1.get()
            self.Y_1 = self.y_double_1.get()

            self.X_2 = self.x_double_2.get()
            self.Y_2 = self.y_double_2.get()

            fig = Figure(figsize=(6, 6), dpi=90)
            plot1 = fig.add_subplot(111)

            self.XX_1 = list(self.X_1.split(","))
            self.YY_1 = list(self.Y_1.split(","))
            self.XX_2 = list(self.X_2.split(","))
            self.YY_2 = list(self.Y_2.split(","))

            for i in range(0, len(self.XX_1)):
                self.XX_1[i] = float(self.XX_1[i])

            for i in range(0, len(self.YY_1)):
                self.YY_1[i] = float(self.YY_1[i])

            for i in range(0, len(self.XX_2)):
                self.XX_2[i] = float(self.XX_2[i])

            for i in range(0, len(self.YY_2)):
                self.YY_2[i] = float(self.YY_2[i])


            plot1.plot(self.XX_1, self.YY_1)
            plot1.plot(self.XX_2, self.YY_2)
            plot1.set_xlabel(self.x_doublename.get())
            plot1.set_ylabel(self.y_doublename.get())
            plot1.legend(labels=[self.x_doublename_real.get(), self.y_doublename_real.get()])
            plot1.set_title("www.techiespod.com")
            canvas = FigureCanvasTkAgg(fig, master=self.canvas)
            canvas.draw()
            canvas.get_tk_widget().grid(padx=250, pady=81)
            toolbar = NavigationToolbar2Tk(canvas, self.m)
            toolbar.update()
            canvas.get_tk_widget().grid()
            self.canvas.delete("all")

    def Generate_Graph_bar_S(self):

        self.reset_it()
        if (self.x1.get() == "") or (self.y1.get() == ""):
            self.oops1 = PhotoImage(file='oops.png')
            self.canvas.create_image(500, 400, image=self.oops1)

        else:
            self.canvas.delete("all")
            self.X1 = self.x1.get()
            self.Y1 = self.y1.get()
            fig = Figure(figsize=(6, 6), dpi=90)
            plot2 = fig.add_subplot(111)
            self.XX1 = list(self.X1.split(","))
            self.YY1 = list(self.Y1.split(","))
            for i in range(0, len(self.XX1)):
                self.XX1[i] = float(self.XX1[i])

            for i in range(0, len(self.YY1)):
                self.YY1[i] = float(self.YY1[i])

            plot2.bar(self.XX1, self.YY1)
            plot2.set_xlabel(self.x1_name.get())
            plot2.set_ylabel(self.y1_name.get())
            canvas = FigureCanvasTkAgg(fig, master=self.canvas)
            canvas.draw()
            canvas.get_tk_widget().grid(padx=250, pady=81)
            toolbar = NavigationToolbar2Tk(canvas, self.m)
            toolbar.update()
            canvas.get_tk_widget().grid()

    def Generate_Graph_bar_D(self):
        self.reset_it()
        self.canvas.delete("all")
        if (self.x_bar_.get() == "") or (self.y_bar_.get() == ""):
            self.oops1 = PhotoImage(file='oops.png')
            self.canvas.create_image(500, 400, image=self.oops1)
        else:
            self.canvas.delete("all")
            self.X1_bar_ = self.x_bar_.get()
            self.Y1_bar_ = self.y_bar_.get()
            fig = Figure(figsize=(6, 6), dpi=90)
            plot2 = fig.add_subplot(111)
            width = 0.35

            self.XX1_bar_ = list(self.X1_bar_.split(","))
            self.YY1_bar_ = list(self.Y1_bar_.split(","))
            for i in range(0, len(self.XX1_bar_)):
                self.XX1_bar_[i] = float(self.XX1_bar_[i])

            for i in range(0, len(self.YY1_bar_)):
                self.YY1_bar_[i] = float(self.YY1_bar_[i])

            N = int()
            a = len(self.XX1_bar_)
            print(a)
            N = a
            ind = np.arange(N)

            plot2.bar(ind, self.XX1_bar_, width)
            plot2.bar(ind, self.YY1_bar_, width, bottom=self.XX1_bar_)
            plot2.legend(labels=[self.x_bar_name.get(), self.y_bar_name.get()])
            plot2.set_xlabel(self.x_bar_name_axix.get())
            plot2.set_ylabel(self.y_bar_name_axix.get())
            canvas = FigureCanvasTkAgg(fig, master=self.canvas)
            canvas.draw()
            canvas.get_tk_widget().grid(padx=250, pady=81)
            toolbar = NavigationToolbar2Tk(canvas, self.m)
            toolbar.update()
            canvas.get_tk_widget().grid()

    def Generate_Graph_bar_Hist(self):
        self.reset_it()
        self.canvas.delete("all")
        if (self.x_bar_hist.get() == "") or (self.y_bar_hist.get() == ""):
            self.oops1 = PhotoImage(file='oops.png')
            self.canvas.create_image(500, 400, image=self.oops1)
        else:
            self.canvas.delete("all")
            self.X = self.x_bar_hist.get()
            self.Y = self.y_bar_hist.get()
            fig = Figure(figsize=(6, 6), dpi=90)
            plt = fig.add_subplot(111)
            self.XX = list(self.X.split(","))
            self.YY = list(self.Y.split(","))
            for i in range(0, len(self.XX)):
                self.XX[i] = float(self.XX[i])

            for i in range(0, len(self.YY)):
                self.YY[i] = float(self.YY[i])
            print(self.XX)
            print(self.YY)

            bins = self.YY
            plt.hist(self.XX, bins, color='green')
            plt.set_xlabel(self.x_bar_hist_name.get())
            plt.set_ylabel(self.y_bar_hist_name.get())
            plt.set_title("www.techiespod.com")
            canvas = FigureCanvasTkAgg(fig, master=self.canvas)
            canvas.draw()
            canvas.get_tk_widget().grid(padx=250, pady=81)
            toolbar = NavigationToolbar2Tk(canvas, self.m)
            toolbar.update()
            canvas.get_tk_widget().grid()
            self.canvas.delete("all")

    def Generate_Graph_bar_Hist_frequency(self):
        self.reset_it()
        self.canvas.delete("all")
        if (self.x_bar_hist_f.get() == "") or (self.y_bar_hist_f.get() == ""):
             self.oops1 = PhotoImage(file='oops.png')
             self.canvas.create_image(500, 400, image=self.oops1)

        else:
            self.canvas.delete("all")
            self.X = self.x_bar_hist_f.get()
            self.Y = self.y_bar_hist_f.get()
            fig = Figure(figsize=(6, 6), dpi=90)
            plt = fig.add_subplot(111)
            self.XX = list(self.X.split(","))
            self.YY = list(self.Y.split(","))
            for i in range(0, len(self.XX)):
                self.XX[i] = float(self.XX[i])

            for i in range(0, len(self.YY)):
                self.YY[i] = float(self.YY[i])
            self.i = 0
            self.randomlist = []
            for j in self.XX:
                for k in range(0, j):
                    self.n = random.randint(self.YY[self.i], self.YY[self.i + 1] - 1)
                    self.randomlist.append(self.n)
                self.i = self.i + 1
            print(self.randomlist)
            print(self.XX)
            print(self.YY)

            bins = self.YY

            plt.hist(self.randomlist, bins, color='green')
            plt.set_xlabel(self.x_bar_hist_name_f.get())
            plt.set_ylabel(self.y_bar_hist_name_f.get())
            plt.set_title("www.techiespod.com")
            canvas = FigureCanvasTkAgg(fig, master=self.canvas)
            canvas.draw()
            canvas.get_tk_widget().grid(padx=250, pady=81)
            toolbar = NavigationToolbar2Tk(canvas, self.m)
            toolbar.update()
            canvas.get_tk_widget().grid()
            self.canvas.delete("all")

    def Generate_Graph_scattered_s(self):
        self.reset_it()
        # self.canvas.delete("all")
        if (self.x_scattered_s.get() == "") or (self.y_scattered_s.get() == ""):
            self.oops1 = PhotoImage(file='oops.png')
            self.canvas.create_image(500, 400, image=self.oops1)

        else:
            self.canvas.delete("all")
            self.X = self.x_scattered_s.get()
            self.Y = self.y_scattered_s.get()
            fig = Figure(figsize=(6, 6), dpi=90)
            plot1 = fig.add_subplot(111)
            self.XX = list(self.X.split(","))
            self.YY = list(self.Y.split(","))
            for i in range(0, len(self.XX)):
                self.XX[i] = float(self.XX[i])

            for i in range(0, len(self.YY)):
                self.YY[i] = float(self.YY[i])
            plot1.scatter(self.XX, self.YY)
            plot1.set_xlabel(self.x_scattered_name_s.get())
            plot1.set_ylabel(self.y_scattered_name_s.get())
            plot1.set_title("www.techiespod.com")
            canvas = FigureCanvasTkAgg(fig, master=self.canvas)
            canvas.draw()
            canvas.get_tk_widget().pack(padx=250, pady=81)
            toolbar = NavigationToolbar2Tk(canvas, self.m)
            toolbar.update()
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
            self.canvas.delete("all")

    def Generate_Graph_scattered_d(self):
        self.reset_it()
        if (self.x_scattered_d1.get() == "") or (self.y_scattered_d1.get() == "") or (
                self.x_scattered_d2.get() == "") or (
                self.y_scattered_d2.get() == ""):
            self.oops1 = PhotoImage(file='oops.png')
            self.canvas.create_image(500, 400, image=self.oops1)

        else:
            self.canvas.delete("all")
            self.X_1 = self.x_scattered_d1.get()
            self.Y_1 = self.y_scattered_d1.get()

            self.X_2 = self.x_scattered_d2.get()
            self.Y_2 = self.y_scattered_d2.get()

            fig = Figure(figsize=(6, 6), dpi=90)
            plot1 = fig.add_subplot(111)

            self.XX_1 = list(self.X_1.split(","))
            self.YY_1 = list(self.Y_1.split(","))
            self.XX_2 = list(self.X_2.split(","))
            self.YY_2 = list(self.Y_2.split(","))

            for i in range(0, len(self.XX_1)):
                self.XX_1[i] = float(self.XX_1[i])

            for i in range(0, len(self.YY_1)):
                self.YY_1[i] = float(self.YY_1[i])

            for i in range(0, len(self.XX_2)):
                self.XX_2[i] = float(self.XX_2[i])

            for i in range(0, len(self.YY_2)):
                self.YY_2[i] = float(self.YY_2[i])
            plot1.scatter(self.XX_1, self.YY_1)
            plot1.scatter(self.XX_2, self.YY_2)
            plot1.set_xlabel(self.x_scattered_name_d1.get())
            plot1.set_ylabel(self.y_scattered_name_d1.get())
            plot1.legend(labels=[self.x_scattered_name_d2.get(), self.y_scattered_name_d2.get()])
            plot1.set_title("www.techiespod.com")
            canvas = FigureCanvasTkAgg(fig, master=self.canvas)
            canvas.draw()
            canvas.get_tk_widget().grid(padx=250, pady=81)
            toolbar = NavigationToolbar2Tk(canvas, self.m)
            toolbar.update()
            canvas.get_tk_widget().grid()
            self.canvas.delete("all")

    def Generate_Graph_scattered_3d(self):
        self.reset_it()
        if (self.x_scattered_3d.get() == "") or (self.y_scattered_3d.get() == "") or (self.z_scattered_3d.get() == ""):
            self.oops1 = PhotoImage(file='oops.png')
            self.canvas.create_image(500, 400, image=self.oops1)

        else:
            self.canvas.delete("all")
            self.X = self.x_scattered_3d.get()
            self.Y = self.y_scattered_3d.get()
            self.Z = self.z_scattered_3d.get()
            fig = Figure(figsize=(6, 6), dpi=90)
            plot1 = fig.add_subplot(111, projection="3d")
            self.XX = list(self.X.split(","))
            self.YY = list(self.Y.split(","))
            self.ZZ = list(self.Z.split(","))
            for i in range(0, len(self.XX)):
                self.XX[i] = float(self.XX[i])

            for i in range(0, len(self.YY)):
                self.YY[i] = float(self.YY[i])

            for i in range(0, len(self.ZZ)):
                self.ZZ[i] = float(self.ZZ[i])

            plot1.scatter3D(self.XX, self.YY, self.ZZ, color="green")

            plot1.set_xlabel(self.x_scattered_name_3d.get())
            plot1.set_ylabel(self.y_scattered_name_3d.get())
            plot1.set_zlabel(self.z_scattered_name_3d.get())
            plot1.set_title("www.techiespod.com")
            canvas = FigureCanvasTkAgg(fig, master=self.canvas)
            canvas.draw()
            canvas.get_tk_widget().pack(padx=250, pady=81)
            toolbar = NavigationToolbar2Tk(canvas, self.m)
            toolbar.update()
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
            self.canvas.delete("all")

    def Generate_Graph_pie_chart(self):
        self.reset_it()
        if (self.pie_lable.get() == "") or (self.pie_data.get() == ""):
            self.oops1 = PhotoImage(file='oops.png')
            self.canvas.create_image(500, 400, image=self.oops1)
        else:
            self.canvas.delete("all")
            self.X = self.pie_lable.get()
            self.Y = self.pie_data.get()
            fig = Figure(figsize=(6, 6), dpi=90)
            plot1 = fig.add_subplot(111)
            self.XX = list(self.X.split(","))
            self.YY = list(self.Y.split(","))

            for i in range(0, len(self.YY)):
                self.YY[i] = float(self.YY[i])
            self.length_exp = len(self.YY)
            self.length_exp_list = '0.1 ' * self.length_exp
            self.c = list(self.length_exp_list.split())
            print(self.c)
            print(len(self.c))
            for i in range(0, len(self.c)):
                self.c[i] = float(self.c[i])
            print(self.c)
            print(self.YY)
            plot1.axis('equal')
            length_exp = len(self.YY)
            length_exp_list = [0.1 * length_exp]
            print(length_exp)
            plot1.pie(self.YY, labels=self.XX, startangle=90, shadow=True, explode=self.c, autopct='%1.2f%%')
            # plot1.plot(self.XX, self.YY)
            plot1.set_title("www.techiespod.com")
            canvas = FigureCanvasTkAgg(fig, master=self.canvas)
            canvas.draw()
            canvas.get_tk_widget().pack(padx=250, pady=81)
            toolbar = NavigationToolbar2Tk(canvas, self.m)
            toolbar.update()
            canvas.get_tk_widget().pack(side=TOP, fill=BOTH)
            self.canvas.delete("all")

    def save_as_png(self):
        self.file = filedialog.asksaveasfilename(initialdir="C:/",
                                                 filetypes=(('PNG File', '.PNG'), ('PNG File', '.PNG')))
        self.file = self.file + ".PNG"
        ImageGrab.grab().crop((346, 220, 980, 860)).save(self.file)

    def dark(self):
        self.m.config(bg="#616161")
        self.canvas.config(bg="#a2a3a2")
        self.my_frm.config(bg="#454545")
        self.my_frm1.config(bg="#454545")
        self.my_frm2.config(bg="#454545")
        self.my_frm3.config(bg="#454545")
        self.my_frmpie.config(bg="#454545")
        self.my_cal.config(bg="#454545")
        # self.my_notebook.config(bg="red")
        # pie
        self.title_bar_2_.config(bg="#454545", fg="white")
        self.ip_bar_X2_.config(bg="#454545", fg="white")
        self.ip_X_bar_ent2_.config(bg="#ebebeb", fg="black")
        self.ip_Y_bar_ent2_.config(bg="#ebebeb", fg="black")
        self.ip_bar_Y2_.config(bg="#454545", fg="white")

        # scattered 3d
        self.my_frm_sub_scattered_3d.config(bg="#454545")
        self.title_scattering_3d.config(bg="#454545", fg="white")
        self.ip_X_ent_scattering_3d.config(bg="#ebebeb", fg="black")
        self.ip_X_scattering_3d.config(bg="#454545", fg="white")
        self.ip_Y_scattering_3d.config(bg="#454545", fg="white")
        self.ip_Y_ent_scattering_3d.config(bg="#ebebeb", fg="black")
        self.ip_Z_scattering_3d.config(bg="#454545", fg="white")
        self.ip_Z_ent_scattering_3d.config(bg="#ebebeb", fg="black")
        self.lbl_x_scattering_3d.config(bg="#454545", fg="white")
        self.lbl_x_ent_scattering_3d.config(bg="#ebebeb", fg="black")
        self.lbl_y_scattering_3d.config(bg="#454545", fg="white")
        self.lbl_y_ent_scattering_3d.config(bg="#ebebeb", fg="black")
        self.lbl_z_scattering_3d.config(bg="#454545", fg="white")
        self.lbl_z_ent_scattering_3d.config(bg="#ebebeb", fg="black")

        # scattered double
        self.my_frm_sub_scattered_d.config(bg="#454545")
        self.title_scattering_d.config(bg="#454545", fg="white")
        self.ip_1X_ent_scattering_d.config(bg="#ebebeb", fg="black")
        self.ip_1X_scattering_d.config(bg="#454545", fg="white")
        self.ip_1Y_scattering_d.config(bg="#454545", fg="white")
        self.ip_1Y_ent_scattering_d.config(bg="#ebebeb", fg="black")
        self.ip_2X_ent_scattering_d.config(bg="#ebebeb", fg="black")
        self.ip_2X_scattering_d.config(bg="#454545", fg="white")
        self.ip_2Y_scattering_d.config(bg="#454545", fg="white")
        self.ip_2Y_ent_scattering_d.config(bg="#ebebeb", fg="black")
        self.lbl_2x_ent_scattering_d.config(bg="#ebebeb", fg="black")
        self.lbl_2y_ent_scattering_d.config(bg="#ebebeb", fg="black")
        self.lbl_2x_ent_scattering_d_leg.config(bg="#ebebeb", fg="black")
        self.lbl_2y_scattering_d_leg.config(bg="#454545", fg="white")
        self.lbl_2x_scattering_d_leg.config(bg="#454545", fg="white")
        self.lbl_2x_scattering_d.config(bg="#454545", fg="white")
        self.lbl_2y_scattering_d.config(bg="#454545", fg="white")

        # scattered single
        self.my_frm_sub_scattered_s.config(bg="#454545")
        self.title_scattering_s.config(bg="#454545", fg="white")
        self.ip_X_scattering_s.config(bg="#454545", fg="white")
        self.ip_Y_scattering_s.config(bg="#454545", fg="white")
        self.ip_Y_ent_scattering_s.config(bg="#ebebeb", fg="black")
        self.ip_X_ent_scattering_s.config(bg="#ebebeb", fg="black")
        self.lbl_x_scattering_s.config(bg="#454545", fg="white")
        self.lbl_y_scattering_s.config(bg="#454545", fg="white")

        # Histogram frequency
        self.title_bar_2_f.config(bg="#454545", fg="white")
        self.ip_bar_X2_f.config(bg="#454545", fg="white")
        self.my_frm_sub_bar4.config(bg="#454545")
        self.ip_bar_Y2_f.config(bg="#454545", fg="white")
        self.ip_X_bar_ent2_f.config(bg="#ebebeb", fg="black")
        self.ip_Y_bar_ent2_f.config(bg="#ebebeb", fg="black")
        self.lbl_bar_x2_f.config(bg="#454545", fg="white")
        self.lbl_bar_y2_f.config(bg="#454545", fg="white")

        # Histogram Raw Input
        self.title_bar_2.config(bg="#454545", fg="white")
        self.ip_bar_X2.config(bg="#454545", fg="white")
        self.my_frm_sub_bar3.config(bg="#454545")
        self.ip_bar_Y2.config(bg="#454545", fg="white")
        self.ip_X_bar_ent2.config(bg="#ebebeb", fg="black")
        self.ip_Y_bar_ent2.config(bg="#ebebeb", fg="black")
        self.lbl_bar_x2.config(bg="#454545", fg="white")
        self.lbl_bar_y2.config(bg="#454545", fg="white")

        # Bar Graph (Stacked)
        self.title_bar_1.config(bg="#454545", fg="white")
        self.my_frm_sub_bar2.config(bg="#454545")
        self.ip_bar_X1.config(bg="#454545", fg="white")
        self.ip_X_bar_ent2.config(bg="#ebebeb", fg="black")
        self.ip_bar_Y1.config(bg="#454545", fg="white")
        self.ip_Y_bar_ent2.config(bg="#ebebeb", fg="black")
        self.lbl_bar_x1.config(bg="#454545", fg="white")
        self.lbl_bar_y1.config(bg="#454545", fg="white")
        self.lbl_bar_x1_axix.config(bg="#454545", fg="white")
        self.lbl_bar_y1_axix.config(bg="#454545", fg="white")

        # Bar Graph (Normal)
        self.title1.config(bg="#454545", fg="white")
        self.my_frm_sub_bar1.config(bg="#454545")
        self.ip_X1.config(bg="#454545", fg="white")
        self.ip_Y1.config(bg="#454545", fg="white")
        self.ip_X_ent1.config(bg="#ebebeb", fg="#454545")
        self.ip_Y_ent1.config(bg="#ebebeb", fg="#454545")
        self.lbl_x1.config(bg="#454545", fg="white")
        self.lbl_y1.config(bg="#454545", fg="white")

        # line Graph (Double Line)
        self.title_.config(bg="#454545", fg="white")
        self.my_frm_sub_1.config(bg="#454545")
        self.ip_1X_.config(bg="#454545", fg="white")
        self.ip_1Y_.config(bg="#454545", fg="white")
        self.ip_1Y_ent_.config(bg="#ebebeb", fg="#454545")
        self.ip_1X_ent_.config(bg="#ebebeb", fg="#454545")
        self.ip_2X_.config(bg="#454545", fg="white")
        self.ip_2Y_.config(bg="#454545", fg="white")
        self.lbl_2x_.config(bg="#454545", fg="white")
        self.lbl_2y_.config(bg="#454545", fg="white")
        self.lbl_2x_leg_.config(bg="#454545", fg="white")
        self.lbl_2y_leg_.config(bg="#454545", fg="white")

        # line Graph (Single Line)
        self.my_frm_sub.config(bg="#454545")
        self.title.config(bg="#454545", fg="white")
        self.ip_X.config(bg="#454545", fg="white")
        self.ip_X_ent.config(bg="#ebebeb", fg="#454545")
        self.ip_Y.config(bg="#454545", fg="white")
        self.ip_Y_ent.config(bg="#ebebeb", fg="#454545")
        self.lbl_x.config(bg="#454545", fg="white")
        self.lbl_y.config(bg="#454545", fg="white")

    def default(self):
        self.m.config(bg="#ffffff")
        self.canvas.config(bg="#a2a3a2")
        self.my_frm.config(bg="#e3fff6")
        self.my_frm1.config(bg="#e3fff6")
        self.my_frm2.config(bg="#e3fff6")
        self.my_frm3.config(bg="#e3fff6")
        self.my_frmpie.config(bg="#e3fff6")
        self.my_cal.config(bg="#e3fff6")
        # pie
        self.title_bar_2_.config(bg="#e3fff6", fg="black")
        self.ip_bar_X2_.config(bg="#e3fff6", fg="black")
        self.ip_X_bar_ent2_.config(bg="white", fg="black")
        self.ip_Y_bar_ent2_.config(bg="white", fg="black")
        self.ip_bar_Y2_.config(bg="#e3fff6", fg="black")

        # scattered 3d
        self.my_frm_sub_scattered_3d.config(bg="#e3fff6")
        self.title_scattering_3d.config(bg="#e3fff6", fg="black")
        self.ip_X_ent_scattering_3d.config(bg="white", fg="black")
        self.ip_X_scattering_3d.config(bg="#e3fff6", fg="black")
        self.ip_Y_scattering_3d.config(bg="#e3fff6", fg="black")
        self.ip_Y_ent_scattering_3d.config(bg="white", fg="black")
        self.ip_Z_scattering_3d.config(bg="#e3fff6", fg="black")
        self.ip_Z_ent_scattering_3d.config(bg="white", fg="black")
        self.lbl_x_scattering_3d.config(bg="#e3fff6", fg="black")
        self.lbl_x_ent_scattering_3d.config(bg="white", fg="black")
        self.lbl_y_scattering_3d.config(bg="#e3fff6", fg="black")
        self.lbl_y_ent_scattering_3d.config(bg="white", fg="black")
        self.lbl_z_scattering_3d.config(bg="#e3fff6", fg="black")
        self.lbl_z_ent_scattering_3d.config(bg="white", fg="black")

        # scattered double
        self.my_frm_sub_scattered_d.config(bg="#e3fff6")
        self.title_scattering_d.config(bg="#e3fff6", fg="black")
        self.ip_1X_ent_scattering_d.config(bg="white", fg="black")
        self.ip_1X_scattering_d.config(bg="#e3fff6", fg="black")
        self.ip_1Y_scattering_d.config(bg="#e3fff6", fg="black")
        self.ip_1Y_ent_scattering_d.config(bg="white", fg="black")
        self.ip_2X_ent_scattering_d.config(bg="white", fg="black")
        self.ip_2X_scattering_d.config(bg="#e3fff6", fg="black")
        self.ip_2Y_scattering_d.config(bg="#e3fff6", fg="black")
        self.ip_2Y_ent_scattering_d.config(bg="white", fg="black")
        self.lbl_2x_ent_scattering_d.config(bg="white", fg="black")
        self.lbl_2y_ent_scattering_d.config(bg="white", fg="black")
        self.lbl_2x_ent_scattering_d_leg.config(bg="white", fg="black")
        self.lbl_2y_scattering_d_leg.config(bg="#e3fff6", fg="black")
        self.lbl_2x_scattering_d_leg.config(bg="#e3fff6", fg="black")
        self.lbl_2x_scattering_d.config(bg="#e3fff6", fg="black")
        self.lbl_2y_scattering_d.config(bg="#e3fff6", fg="black")

        # scattered single
        self.my_frm_sub_scattered_s.config(bg="#e3fff6")
        self.title_scattering_s.config(bg="#e3fff6", fg="black")
        self.ip_X_scattering_s.config(bg="#e3fff6", fg="black")
        self.ip_Y_scattering_s.config(bg="#e3fff6", fg="black")
        self.ip_Y_ent_scattering_s.config(bg="white", fg="black")
        self.ip_X_ent_scattering_s.config(bg="white", fg="black")
        self.lbl_x_scattering_s.config(bg="#e3fff6", fg="black")
        self.lbl_y_scattering_s.config(bg="#e3fff6", fg="black")

        # Histogram frequency
        self.title_bar_2_f.config(bg="#e3fff6", fg="black")
        self.ip_bar_X2_f.config(bg="#e3fff6", fg="black")
        self.my_frm_sub_bar4.config(bg="#e3fff6")
        self.ip_bar_Y2_f.config(bg="#e3fff6", fg="black")
        self.ip_X_bar_ent2_f.config(bg="white", fg="black")
        self.ip_Y_bar_ent2_f.config(bg="white", fg="black")
        self.lbl_bar_x2_f.config(bg="#e3fff6", fg="black")
        self.lbl_bar_y2_f.config(bg="#e3fff6", fg="black")

        # Histogram Raw Input
        self.title_bar_2.config(bg="#e3fff6", fg="black")
        self.ip_bar_X2.config(bg="#e3fff6", fg="black")
        self.my_frm_sub_bar3.config(bg="#e3fff6")
        self.ip_bar_Y2.config(bg="#e3fff6", fg="black")
        self.ip_X_bar_ent2.config(bg="white", fg="black")
        self.ip_Y_bar_ent2.config(bg="white", fg="black")
        self.lbl_bar_x2.config(bg="#e3fff6", fg="black")
        self.lbl_bar_y2.config(bg="#e3fff6", fg="black")

        # Bar Graph (Stacked)
        self.title_bar_1.config(bg="#e3fff6", fg="black")
        self.my_frm_sub_bar2.config(bg="#e3fff6")
        self.ip_bar_X1.config(bg="#e3fff6", fg="black")
        self.ip_X_bar_ent2.config(bg="white", fg="black")
        self.ip_bar_Y1.config(bg="#e3fff6", fg="black")
        self.ip_Y_bar_ent2.config(bg="white", fg="black")
        self.lbl_bar_x1.config(bg="#e3fff6", fg="black")
        self.lbl_bar_y1.config(bg="#e3fff6", fg="black")
        self.lbl_bar_x1_axix.config(bg="#e3fff6", fg="black")
        self.lbl_bar_y1_axix.config(bg="#e3fff6", fg="black")

        # Bar Graph (Normal)
        self.title1.config(bg="#e3fff6", fg="black")
        self.my_frm_sub_bar1.config(bg="#e3fff6")
        self.ip_X1.config(bg="#e3fff6", fg="black")
        self.ip_Y1.config(bg="#e3fff6", fg="black")
        self.ip_X_ent1.config(bg="white", fg="black")
        self.ip_Y_ent1.config(bg="white", fg="black")
        self.lbl_x1.config(bg="#e3fff6", fg="black")
        self.lbl_y1.config(bg="#e3fff6", fg="black")

        # line Graph (Double Line)
        self.title_.config(bg="#e3fff6", fg="black")
        self.my_frm_sub_1.config(bg="#e3fff6")
        self.ip_1X_.config(bg="#e3fff6", fg="black")
        self.ip_1Y_.config(bg="#e3fff6", fg="black")
        self.ip_1Y_ent_.config(bg="white", fg="black")
        self.ip_1X_ent_.config(bg="white", fg="black")
        self.ip_2X_.config(bg="#e3fff6", fg="black")
        self.ip_2Y_.config(bg="#e3fff6", fg="black")
        self.lbl_2x_.config(bg="#e3fff6", fg="black")
        self.lbl_2y_.config(bg="#e3fff6", fg="black")
        self.lbl_2x_leg_.config(bg="#e3fff6", fg="black")
        self.lbl_2y_leg_.config(bg="#e3fff6", fg="black")

        # line Graph (Single Line)
        self.my_frm_sub.config(bg="#e3fff6")
        self.title.config(bg="#e3fff6", fg="black")
        self.ip_X.config(bg="#e3fff6", fg="black")
        self.ip_X_ent.config(bg="white", fg="black")
        self.ip_Y.config(bg="#e3fff6", fg="black")
        self.ip_Y_ent.config(bg="white", fg="black")
        self.lbl_x.config(bg="#e3fff6", fg="black")
        self.lbl_y.config(bg="#e3fff6", fg="black")

    def on_closing(self):
        if messagebox.askyesno("Exit", "Do you want to save your file before leaving ? "):
            self.save_as_png()
        else:
            self.m.destroy()

    def getvals(self,event):
        value = event.widget.cget('text')
        if value == 'Clr':
            self.sc_variable.set('')
        elif value == '=':
            try:
                self.sc_variable.set(eval(self.screen.get()))
                self.screen.update()
            except Exception as e:
                self.sc_variable.set('Error - Wait for 3 sec')
                self.screen.update()
                self.status_var.set('Preparing...')
                self.screen.update()
                time.sleep(3)
                self.sc_variable.set('')
                self.screen.update()
                self.status_var.set('Ready..')
                self.screen.update()

        else:
            self.sc_variable.set(f'{self.sc_variable.get()}{value}')

i = 0

def create_cycle():
    x = {}
    x[i + 1] = x


collected = gc.collect()

for i in range(10):
    create_cycle()

collected = gc.collect()




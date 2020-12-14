from datavis import *
from tkinter import *
from turtle import TurtleScreen, RawTurtle


master = Tk()
#master.attributes('-alpha',0.5)
master.iconbitmap("icon.ico")
app_width = 450
app_height = 450

win_width = master.winfo_screenwidth()
win_height = master.winfo_screenheight()



x = (win_width / 2) - (app_width / 2)
y = (win_height / 2) - (app_height / 2)

master.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

master.overrideredirect(True)
master.after(2000, lambda: master.destroy())
WIDTH, HEIGHT = 450, 450
canvas = Canvas(master, width=WIDTH, height=HEIGHT, bg="green")
canvas.pack(ipadx=30)
root = TurtleScreen(canvas)
turtle = RawTurtle(root, visible=False)
root.bgcolor("white")


turtle.color('#F09F13')
turtle.pensize(4)
turtle.speed(15)
turtle.hideturtle()

turtle.penup()
turtle.setposition(70, 90)
turtle.pendown()
turtle.fillcolor("#F09F13")
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.hideturtle()

turtle.color('#fe7d96')
turtle.pensize(4)
turtle.speed(15)
turtle.hideturtle()
turtle.penup()
turtle.setposition(15,-20)
turtle.hideturtle()
turtle.pendown()
turtle.fillcolor("#fe7d96")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.hideturtle()

turtle.color('orange')
turtle.pensize(4)
turtle.speed(15)
turtle.penup()
turtle.setposition(-69, 70)
turtle.pendown()
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()
turtle.hideturtle()

style = ('Arial', 30, 'bold')
turtle.color('Black')
turtle.speed(10)
turtle.penup()
turtle.setposition(0, -80)
turtle.hideturtle()
turtle.write('TechieSpod', font=style, align='center')
turtle.speed(10)
turtle.penup()
turtle.setposition(0, -100)
turtle.hideturtle()
style = ('Arial', 10)
turtle.write("Explore, Try & Invent", font=style, align='center')
turtle.speed(10)
turtle.penup()
turtle.setposition(0, -120)
turtle.hideturtle()
turtle.write("_________________________________", font=style, align='center')

turtle.hideturtle()

master.mainloop()
root = Tk()
root.title("Demo Class Matplotlib")
root.geometry("1536x800")
root.config(bg="#ffffff")
root.iconbitmap("icon.ico")
a = work(root)
b = work.canvasdemo(a)
root.mainloop()

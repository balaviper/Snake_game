import turtle
import time
import random

sc = turtle.Screen()
sc.title("viper game")
sc.bgcolor("black")
sc.setup(width=700, height=700)
sc.tracer(0)

hd = turtle.Turtle()
hd.speed(0)
hd.shape("circle")
hd.color("white")
hd.penup()
hd.goto(0, 0)
hd.direction = "stop"

ft = turtle.Turtle()
ft.speed(0)
ft.shape("triangle")
ft.color("red")
ft.penup()
ft.goto(0, 120)

def game_over():
    wt = turtle.Turtle()
    wt.speed(0)
    wt.shape("square")
    wt.color("white")
    wt.penup()
    wt.hideturtle()
    wt.goto(0, 0)
    wt.write("GAME OVER", align="center", font=("Ariel", 28, "normal"))


l=[]

def up():
    hd.direction = "up"

def down():
        hd.direction = "down"

def right():
    hd.direction = "right"

def left():
    hd.direction = "left"

def moves():
    if hd.direction == "up":
        y = hd.ycor()
        hd.sety(y + 20)

    if hd.direction == "down":
        y = hd.ycor()
        hd.sety(y - 20)

    if hd.direction == "left":
        x = hd.xcor()
        hd.setx(x - 20)

    if hd.direction == "right":
        x = hd.xcor()
        hd.setx(x + 20)



sc.listen()
sc.onkeypress(up, "w")
sc.onkeypress(down, "s")
sc.onkeypress(right, "d")
sc.onkeypress(left, "a")


while True:
    sc.update()

    if hd.xcor() > 340 or hd.xcor() < -340 or hd.ycor() > 340 or hd.ycor() < -330:
        time.sleep(1)
        hd.direction = "stop"
        game_over()
        time.sleep(10)




    if hd.distance(ft) < 20:
        a = random.randint(-320, 320)
        b = random.randint(-320, 320)
        ft.goto(a, b)



        bd = turtle.Turtle()
        bd.speed(0)
        bd.shape("circle")
        bd.color("white")
        bd.penup()
        l.append(bd)


    for i in range(len(l)-1, 0, -1):
        a = l[i-1].xcor()
        b = l[i-1].ycor()
        l[i].goto(a, b)

    if len(l) > 0:
        a = hd.xcor()
        b = hd.ycor()
        l[0].goto(a, b)


    moves()


    for i in l:
        if i.distance(hd) < 20:
            time.sleep(1)
            hd.direction = "stop"
            game_over()
            time.sleep(10)

    time.sleep(0.1)


sc.mainloop()

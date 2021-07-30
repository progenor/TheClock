import time
import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=700)
wn.title("Clock by progenor")
wn.tracer(0)

#drawing
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

#hand
hd = turtle.Turtle()
hd.hideturtle()
hd.speed(0)
hd.pensize(3)

#digital
di = turtle.Turtle()
di.hideturtle()
di.speed(0)
di.goto(0, 260)




def draw_clock(pen):

    #Clock face
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("red")
    pen.pendown()
    pen.circle(210)

    #draw lines
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

def draw_hand(pen, h, m, s):
    # draw oramutato xd
    pen.penup()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # draw perc xd
    pen.penup()
    pen.goto(0, 0)
    pen.color("green")
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)

    # draw masodperc xd
    pen.penup()
    pen.goto(0, 0)
    pen.color("blue")
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(120)

def dig(h, m, s, di):
    di.clear()
    di.color("red")
    di.write("{}:{}:{}".format(h, m, s), align="center", font=("Courier", 22, "normal"))



run = True

draw_clock(pen)

while run:

    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))



    draw_hand(hd, h, m, s)
    dig(h, m, s, di)

    wn.update()
    time.sleep(1)
    hd.clear()



wn.mainloop()

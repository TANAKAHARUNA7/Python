import turtle

# 画面の設定
screen = turtle.Screen()
screen.bgcolor("white")

# タートルの設定
t = turtle.Turtle()
t.speed(1)
t.color("red")
t.pensize(3)

def draw_heart():
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()
    
draw_heart()    
turtle.done()
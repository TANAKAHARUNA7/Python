import random
import turtle

# 
screen = turtle.Screen()
screen.title("Turtle 키보드 이벤트 처리 예제")

width = screen.window_width()//2
height = screen.window_height()//2

print("윈도우 가롵세로" , width, height)

screen = turtle.Screen()

def move_foward():
    t.forward(100)

    x, y = t.position()
    
    if x >= width or x <= width or :
        t.right(180)
    elif x >= width:
        t.right(180)











screen.setup(width=1720, height=1080)

boundary_left = -860
boundary_right = 860
boundary_top = 540
boundary_bottom = -540

t = turtle.Turtle()

def move_turtle(x, y):
    if boundary_left < x < boundary_right and boundary_bottom < y < boundary_top:
        t.goto(x, y)

def move_up():
    x, y = t.position()
    move_turtle(x, y + 10)

def move_down():
    x, y = t.position()
    move_turtle(x, y - 10)

def move_left():
    x, y = t.position()
    move_turtle(x - 10, y)

def move_right():
    x, y = t.position()
    move_turtle(x + 10, y)
    
# i를 누르면 색깔 빨간색 -> 또는 

def inverse_color():
    current_color = t.pencolor()
    
    if  current_color == "red":
        t.pencolor("blak")
    else:
        t.pencolor("red")  
        
        
def chenge_color():
    print("색깔 선택")
    print("1. 파란색")
    print("2. 검정색")    
    print("3. 노란색")    

# 1~3 이외 값 입력 시 재임력 -> 언제까지?? 1~3 값이 입력 될때 까지
    

    while not (1 <= input_value <= 3) :
        input_value = int(input("숫자 입력"))
        if input_value == 1:
            t.pencolor("blue")
        elif input_value == 2:
            t.pencolor("black")
        elif input_value == 3:
            t.pencolor("yellow")
            
            
            

def move_forward():
    t.forward(100)
    
    x, y = t.position()
    print(x, y)
    
    
def move_backward():
    t.backward(100)    
    
def turn_left():
    t.left(15)    

def turn_right():
    t.right(15)

def change_color_to_black():
    t.color("black")

def change_color_to_red():
    t.color("red")

def move_random():
    colors = ["red", "green", "blue", "yellow", "purple", "orange"]
    t.pencolor(random.choice(colors))
    
    
    
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")    
screen.onkey(turn_left, "Left")    
screen.onkey(turn_right, "Right") 
screen.onkey(move_random, "c")
screen.onkey(change_color_to_black,"b")
screen.onkey(change_color_to_red,"r")
screen.onkey(chenge_color,"p")

screen.mainloop()
  
    
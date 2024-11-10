import turtle

# 画面の作成
screen = turtle.Screen()
screen.setup(width=800, height=600)  # 画面の大きさを設定

# 境界を設定
boundary_left = -400
boundary_right = 400
boundary_top = 300
boundary_bottom = -300

# タートルの作成
t = turtle.Turtle()

# 移動制限を確認する関数
def move_turtle(x, y):
    if boundary_left < x < boundary_right and boundary_bottom < y < boundary_top:
        t.goto(x, y)

# 矢印キーでタートルを動かす関数
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

# キーボードのバインディング
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# ウィンドウをクリックで閉じる
screen.exitonclick()

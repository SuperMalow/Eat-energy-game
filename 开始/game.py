import turtle as t
import random
import time

#游戏登录 文字介绍
def loging():
    log = t.Turtle()
    log.color('blue')
    log.hideturtle()
    log.penup()
    log.goto(0, 50)
    log.write("机器人回家遭到陨石攻击", align='center', font=("Comic Sans MS", 40, "normal"))
    time.sleep(1)
    log.goto(0, 0)
    log.write("落在一个废弃的空间站", align='center', font=("Comic Sans MS", 40, "normal"))
    time.sleep(1)
    log.goto(0, -50)
    log.write("它目前的能量不足以回家", align='center', font=("Comic Sans MS", 40, "normal"))
    time.sleep(1)
    log.goto(0, -100)
    log.write("你能帮它回家吗？", align='center', font=("Comic Sans MS", 40, "normal"))
    time.sleep(2)
    log.clear()
    log.home()
    log.color('red')
    log.write("Game start", align='center', font=("Comic Sans MS", 80, "normal"))
    log.color('blue')
    log.goto(0, -60)
    log.write("方向键↑↓←→来控制小机器运动", align='center', font=("Comic Sans MS", 30, "normal"))
    time.sleep(4)
    log.clear()
    log.home()
    log.write("Are you ready ?", align='center', font=("Comic Sans MS", 50, "normal"))
    time.sleep(1)
    log.clear()
    log.write("3", align='center', font=("Comic Sans MS", 80, "normal"))
    time.sleep(1)
    log.clear()
    log.write("2", align='center', font=("Comic Sans MS", 80, "normal"))
    time.sleep(1)
    log.clear()
    log.write("1", align='center', font=("Comic Sans MS", 80, "normal"))
    time.sleep(1)
    log.clear()

loging()

#游戏屏幕
class pingmu:
    t.register_shape("hook.gif")
    t.register_shape("max01.gif")
    t.register_shape("stone.gif")
    t.register_shape("oil02.gif")
    t.register_shape("oil04.gif")
    t.register_shape("bat.gif")
    t.register_shape("boom.gif")
    def run(self):
        p = t.Screen()
        p.setup(500, 800)

start = pingmu()
start.run()
s = t.Screen()
s.tracer(False)

#调用游戏人物

robot = t.Turtle()
robot.shape('hook.gif')
robot.w = 50
robot.h = 50
robot.v = 10
robot.penup()
robot.goto(0, -400+robot.h)


#监听按键/持续按键 控制人物的移动 人物的速度 限制小机器的运动
def robot_left():
    if robot.xcor() > -250:
        robot.setx(robot.xcor()-10)
def robot_right():
    if robot.xcor() < 250:
        robot.setx(robot.xcor()+10)
def robot_up():
    if robot.ycor() < 400:
        robot.sety(robot.ycor()+10)
def robot_down():
    if robot.ycor() > -400:
        robot.sety(robot.ycor()-10)
s.onkey(robot_left, 'Left')
s.onkey(robot_right, 'Right')
s.onkey(robot_up, 'Up')
s.onkey(robot_down, 'Down')
s.onkeypress(robot_left, 'Left')
s.onkeypress(robot_right, 'Right')
s.onkeypress(robot_up, 'Up')
s.onkeypress(robot_down, 'Down')
s.listen()


#控制物品的掉落
things = []
for i in range(20):
    thing = t.Turtle()
    thing.v = random.random()*1     #这里是下落速度
    if random.random() >0.95:
        thing.shape('max01.gif')
        thing.name = 'max01'
        thing.w = 32
        thing.h = 32        #积分15
    elif random.random() >=0.88:
        thing.shape('bat.gif')
        thing.name = 'bat'
        thing.w = 48
        thing.h = 32        #积分10
    elif random.random() >=0.70:
        thing.shape('stone.gif')
        thing.name = 'stone'
        thing.w = 32
        thing.h = 32        #积分-20
    elif random.random() >=0.52:
        thing.shape('oil04.gif')
        thing.name = 'oil04'
        thing.w = 25
        thing.h = 25        #积分2
    else:
        thing.shape('oil02.gif')
        thing.name = 'oil02'
        thing.w = 32
        thing.h = 32        #积分2
    thing.penup()
    thing.goto(random.randint(-250, 250), random.randint(200, 400)+50)
    things.append(thing)
s.update()

#分数
score = 0
scores = t.Turtle()
scores.penup()
scores.hideturtle()
scores.color('black')
scores.goto(-250+30, 400-30)
scores.write(f'当前能量{score}', align='left', font=('Comic Sans MS',20))

#控制游戏难度
start_time = time.time()


#游戏是否结束
flag = 1
while flag:
    #控制游戏难度
    time_speed = time.time() - start_time  
    for thing in things:
        thing.sety(thing.ycor() - thing.v*(1+time_speed/6))
        #判断是否遭到陨石的砸落
        x1, y1, w1, h1 = thing.xcor()-thing.w/2,thing.ycor()+thing.h/2,thing.w,thing.w
        x2, y2, w2, h2 = robot.xcor()-robot.w/2,robot.ycor()+robot.h/2,robot.w,robot.w
        if max(x1+w1,x2+w2)-min(x1,x2)<w1+w2 and max(y1+h1,y2+h2)-min(y1,y2)<h1+h2:
            if thing.name == 'oil02':
                thing.goto(random.randint(-250, 250), random.randint(300, 400)+50)
                score+=2
                scores.clear()
                scores.write(f'当前能量{score}', align='left', font=('Comic Sans MS',20))
            elif thing.name =='oil04':
                thing.goto(random.randint(-250, 250), random.randint(300, 400)+50)
                score+=2
                scores.clear()
                scores.write(f'当前能量{score}', align='left', font=('Comic Sans MS',20))
            elif thing.name =='bat':
                thing.goto(random.randint(-250, 250), random.randint(300, 400)+50)
                score+=10
                scores.clear()
                scores.write(f'当前能量{score}', align='left', font=('Comic Sans MS',20))
            elif thing.name =='max01':
                thing.goto(random.randint(-250, 250), random.randint(300, 400)+50)
                score+=15
                scores.clear()
                scores.write(f'当前能量{score}', align='left', font=('Comic Sans MS',20))
            else:
                thing.shape('boom.gif')
                flag = 0
                #游戏结束
        if thing.ycor() < -400:
            thing.goto(random.randint(-250, 250), random.randint(300, 400)+50)
    s.update()

#结束游戏
time.sleep(2)
print(score)
over = t.Turtle()
s.clear()
over.home()
over.write(f'游戏结束，总能源{score}', align='center', font=('Comic Sans MS',20))
over.goto(0, -50)
over.shape('stone.gif')
over.stamp()
s.update()

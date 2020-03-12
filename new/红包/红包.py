import turtle
import random
import os 
import time
W,H  = 1200,700
screen  = turtle.Screen()
screen.setup(W,H)
screen.bgpic("bg.gif")
screen.register_shape('hb.gif')

红包 = turtle.Turtle()
红包.shape('hb.gif')
笔 = turtle.Turtle()
笔.hideturtle()
笔.penup()
笔.goto(20,-150)
笔.write('点击我发送红包！',align='center',font=('宋体',30,'normal'))
def ask(起始位置,y):
    # 总金额 = float(input("输入红包金额>>"))
    # renshu = int(input('输入人数>>'))
    总金额 = float(turtle.numinput("红包金额",'请输入红包金额',10,0.01,1000))
    红包个数 = int(turtle.numinput("红包个数","请输入红包个数",3,1,))
    print("你的金额为:{}\n要发的人数为：{}".format(总金额,红包个数))
    笔.clear()
    笔.goto(-100,-150)
    for i in range(3):
        笔.write('正在生成红包'+'.'*i,align="left",font=('宋体',30,'normal'))
        time.sleep(1)
    笔.clear()
    红包.hideturtle()

    红包间距 = W*0.6/(红包个数-1)
    起始位置 = -红包间距 *(红包个数-1)/2
    for i in range((红包个数)):
        if i ==红包个数-1:
            当前红包金额 = round(总金额,2)
        else :    
            qiwang = 总金额/(红包个数-i)
            当前红包金额 = round(random.uniform(0.01,qiwang*2-0.01),2)
        总金额-=当前红包金额
        总金额 = round(总金额,2)
        小红包 = turtle.Turtle()
        小红包.shape('hb.gif')
        小红包.penup()
        小红包.goto(起始位置,0)
        笔.goto(起始位置-60,-150)
        笔.write(f'金额:{当前红包金额}',align="left",font=('宋体',20,'normal'))
        起始位置+=红包间距
        # print(f"第{i+1}位朋友获得{当前红包金额}元,剩余{总金额}元")
        time.sleep(0.5)

红包.onclick(ask,btn=1)

  

import time
import matplotlib.pyplot as plt
import numpy as np
import math


def pow(x, a):
    return math.pow(x, a)


def love1():
    plt.ion()
    figure, ax = plt.subplots()
    lines, = ax.plot([], [], color="red")
    ax.set_autoscaley_on(True)
    ax.grid()
    X = np.linspace(-1.8, 1.8, 1000)
    a = 1

    while True:
        # 设置函数
        y = [pow(pow(x, 2), 2 / 7) + 0.9 * pow(3.3 - x * x, 0.5) * np.sin(a * np.pi * x) for x in X]
        a = a + 0.1
        lines.set_xdata(X)
        lines.set_ydata(y)
        ax.relim()
        ax.autoscale_view()
        figure.canvas.draw()
        figure.canvas.flush_events()
        time.sleep(0.01)


def love2():
    print('\n'.join([''.join([('love'[(x - y) % len('love')] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
                x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))


def love3():
    # coding: utf-8
    import turtle
    import time

    def LittleHeart():
        for i in range(200):
            turtle.right(1)
            turtle.forward(2)

    love = 'I ♥ 瑶'
    me = '强'
    if love == '':
        love = 'I Love you'
    if me == '':
        me = 'I Love you'
    turtle.setup(width=900, height=600)
    turtle.color('red', 'pink')
    turtle.pensize(15)
    turtle.speed(1200)

    turtle.up()

    turtle.hideturtle()
    turtle.goto(0, -180)
    turtle.showturtle()
    turtle.down()
    turtle.speed(500)
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(224)
    LittleHeart()
    turtle.left(120)
    LittleHeart()
    turtle.forward(224)
    turtle.end_fill()
    turtle.pensize(12)
    turtle.up()
    turtle.hideturtle()
    turtle.goto(0, -20)
    turtle.showturtle()
    turtle.color('#CD5C5C', 'pink')
    turtle.write(love, font=('gungsuh', 50,), align="center")
    turtle.up()
    turtle.hideturtle()
    if me != '':
        turtle.color('black', 'pink')
        time.sleep(1)
    turtle.goto(180, -180)
    turtle.showturtle()
    turtle.write(me, font=(20, 25), align="center", move=True)
    window = turtle.Screen()
    window.exitonclick()


if __name__ == '__main__':
    love2()

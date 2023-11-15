"""
File: Bounding_ball.py
Name: Peggy
-------------------------
This program simulates a bouncing ball at (START_X, START_Y) that has VX as x velocity and 0 as y velocity.
Each bounce reduces y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 20
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

times = 0
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(ball_dropped)


def ball_dropped(event):
    global times
    times += 1
    vy = 0  # 每次都先從vy=0開始跳

    if times < 4:  # 只能跳三次
        if ball.x == START_X:  # ball要掉下去的條件
            while True:
                # update
                vx = VX
                vy += GRAVITY
                ball.move(vx, 0)
                ball.move(0, vy)
                # check
                if ball.y <= 0 or ball.y >= window.height:
                    vy = -vy
                    vy *= REDUCE
                if ball.x <= 0 or ball.x >= window.width:
                    break
                # pause
                pause(DELAY)
            window.remove(ball)
            window.add(ball, x=START_X, y=START_Y)


if __name__ == "__main__":
    main()

"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GOval, GRect, GLabel


FRAME_RATE = 10        # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    life = NUM_LIVES

    # total bricks
    rows = graphics.get_rows()
    cols = graphics.get_cols()
    num = rows * cols

    # Add the animation loop here!

    while True:
        vx = graphics.get_dx()
        vy = graphics.get_dy()
        if graphics.switch is True:
            while True:
                # update
                graphics.ball.move(vx, vy)
                if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y) is not None:
                    if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y) is graphics.paddle:
                        vy = -vy
                    if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y) is not graphics.paddle:
                        vy = -vy
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x, graphics.ball.y))
                        num -= 1

                elif graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                   graphics.ball.y) is not None:
                    if graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                     graphics.ball.y) is graphics.paddle:
                        vy = -vy
                    if graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                     graphics.ball.y) is not graphics.paddle:
                        vy = -vy
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                                             graphics.ball.y))
                        num -= 1
                elif graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                   graphics.ball.y + graphics.ball.height) is not None:
                    if graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                     graphics.ball.y + graphics.ball.height) is graphics.paddle:
                        vy = -vy

                    if graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                     graphics.ball.y + graphics.ball.height) is not graphics.paddle:
                        vy = -vy
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                                             graphics.ball.y + graphics.ball.height))
                        num -= 1
                elif graphics.window.get_object_at(graphics.ball.x,
                                                   graphics.ball.y + graphics.ball.height) is not None:
                    if graphics.window.get_object_at(graphics.ball.x,
                                                         graphics.ball.y + graphics.ball.height) is graphics.paddle:
                        vy = -vy
                    if graphics.window.get_object_at(graphics.ball.x,
                                                     graphics.ball.y + graphics.ball.height) is not graphics.paddle:
                        vy = -vy
                        graphics.window.remove(graphics.window.get_object_at(graphics.ball.x,
                                                                             graphics.ball.y + graphics.ball.height))
                        num -= 1

                # win
                if num == 0:
                    nn = GLabel("You Win!")
                    nn.color = "rosybrown"
                    nn.font = "-20"
                    graphics.window.add(nn, x=(graphics.window.width-nn.width)/2,
                                        y=(graphics.window.height-nn.height)/2)
                    graphics.window.remove(graphics.ball)
                    graphics.window.remove(graphics.paddle)
                    break

                # window boundary check
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    vx = -vx
                if graphics.ball.y <= 0:
                    vy = -vy

                # out window
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    life = life - 1
                    graphics.switch = False
                    if life == 0:
                        lb = GLabel("Game over!")
                        lb.color = "rosybrown"
                        lb.font = "-20"
                        graphics.window.add(lb, x=(graphics.window.width-lb.width)/2,
                                            y=(graphics.window.height-lb.height)/2)
                        graphics.window.remove(graphics.ball)
                        graphics.window.remove(graphics.paddle)
                        break
                    graphics.window.remove(graphics.ball)
                    graphics.window.add(graphics.ball, x=graphics.window.width/2, y=graphics.window.height/2)
                    break
                # pause
                pause(FRAME_RATE)
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()

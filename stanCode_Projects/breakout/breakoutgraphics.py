"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random
from campy.gui.events.timer import pause

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2, y=window_height/2)
        self.ball.filled = True
        self.window.add(self.ball)

        # Draw bricks
        for i in range(brick_cols):
            for j in range(brick_rows):
                # print(j)
                self.bricks = GRect(brick_width, brick_height)
                self.bricks.filled = True
                if j % 10 == 0 or j % 10 == 1:
                    self.bricks.fill_color = "red"
                elif j % 10 == 2 or j % 10 == 3:
                    self.bricks.fill_color = "orange"
                elif j % 10 == 4 or j % 10 == 5:
                    self.bricks.fill_color = "yellow"
                elif j % 10 == 6 or j % 10 == 7:
                    self.bricks.fill_color = "green"
                else:
                    self.bricks.fill_color = "blue"
                self.window.add(self.bricks, x=i*(brick_spacing+self.bricks.width),
                                y=brick_offset+j*(brick_spacing+self.bricks.height))

        # Initialize our mouse listeners
        onmouseclicked(self.ball_anime)
        onmousemoved(self.mouse_tracker)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.switch = False

    def ball_anime(self, mouse):
        self.switch = True
        # print("1")
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def mouse_tracker(self, mouse):
        if mouse.x < self.paddle.width/2:
            self.paddle.x = 0
        elif mouse.x > self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    @staticmethod
    def get_rows():
        return BRICK_ROWS

    @staticmethod
    def get_cols():
        return BRICK_COLS

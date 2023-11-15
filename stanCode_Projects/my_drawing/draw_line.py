"""
File: draw_line.py
Name: Peggy
-------------------------
Creates lines on an instance of GWindow class.
"""

from campy.graphics.gobjects import GOval, GLine, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the circle
SIZE = 10
# Global Variable:
window = GWindow()
# started circle
circle = GOval(SIZE, SIZE)
# current click times
times = 0
# record current times
# times_label = GLabel("Times: "+str(times))
# window.add(times_label, x=0, y=times_label.height+15)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(circle_line)


def circle_line(event):  # odd click create a circle with size radius
    global times
    times += 1
    if times % 2 == 1:  # odd click
        window.add(circle, x=event.x - SIZE / 2, y=event.y - SIZE / 2)
#        times_label.text = "Times: "+str(times)
    else:  # even click
        x1 = circle.x
        y1 = circle.y
        window.remove(circle)
        line = GLine(x1, y1, event.x, event.y)
        window.add(line)
#        times_label.text = "Times: "+str(times)


if __name__ == "__main__":
    main()

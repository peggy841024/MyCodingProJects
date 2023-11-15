"""
File: my_drawing.py
Name: Peggy
----------------------
Create a picture using GObject/ GWindow class.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLine, GLabel, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: My lucky dog

    In my childhood, my family gave me a cute stuffed Beagle dog, named "LUCKY".
    When I feel sad, I use his hand to wipe my tears, when I feel happy, I hug him and smile happily.
    Every moment in my life, I always bring him with me. (And every domestic and overseas travel XD)
    For me, he is not just a cute doll, but is a symbol of the love from my family, which made me feel secure,
    and give me peace of mind.
    This code is dedicated to my family, Lucky, and myself. <3
    """

    window = GWindow(width=480, height=440, title="My lucky dog")
    # background
    background = GRect(480, 480)
    background.filled = True
    background.fill_color = "plum"
    window.add(background)

    l_ear = GPolygon()
    l_ear.add_vertex((160, 150))
    l_ear.add_vertex((130, 170))
    l_ear.add_vertex((100, 220))
    l_ear.add_vertex((110, 250))
    l_ear.add_vertex((120, 253))
    l_ear.add_vertex((150, 230))
    l_ear.add_vertex((150, 210))
    l_ear.filled = True
    l_ear.fill_color = "saddlebrown"
    l_ear.color = "saddlebrown"
    window.add(l_ear)

    lup_face = GArc(200, 180, 110, 90, x=135, y=145)
    lup_face.filled = True
    lup_face.fill_color = "chocolate"
    lup_face.color = "chocolate"
    window.add(lup_face)

    up_face = GArc(210, 260, 50, 60, x=130, y=145)
    up_face.filled = True
    up_face.fill_color = "saddlebrown"
    up_face.color = "saddlebrown"
    window.add(up_face)

    rup_face = GArc(200, 180, 325, 90, x=135, y=145)
    rup_face.filled = True
    rup_face.fill_color = "chocolate"
    rup_face.color = "chocolate"
    window.add(rup_face)

    middle = GOval(20, 40, x=170, y=180)
    middle.filled = True
    middle.fill_color = "ivory"
    middle.color = "ivory"
    window.add(middle)

    d_face = GOval(106, 56, x=128, y=200)
    d_face.filled = True
    d_face.fill_color = "ivory"
    d_face.color = "ivory"
    window.add(d_face)

    nose = GArc(60, 60, 25, 100, x=150, y=225)
    nose.filled = True
    nose.fill_color = "black"
    nose.color = "black"
    window.add(nose)

    mouth_l = GPolygon()
    mouth_l.add_vertex((170, 240))
    mouth_l.add_vertex((163, 245))
    mouth_l.color = "black"
    window.add(mouth_l)

    mouth_l2 = GPolygon()
    mouth_l2.add_vertex((162, 245))
    mouth_l2.add_vertex((156, 240))
    mouth_l2.color = "black"
    window.add(mouth_l2)

    mouth_r = GPolygon()
    mouth_r.add_vertex((176, 240))
    mouth_r.add_vertex((183, 247))
    mouth_r.color = "black"
    window.add(mouth_r)

    mouth_r2 = GPolygon()
    mouth_r2.add_vertex((183, 247))
    mouth_r2.add_vertex((191, 243))
    mouth_r2.color = "black"
    window.add(mouth_r2)

    eye1 = GOval(12, 12, x=150, y=180)
    eye1.filled = True
    eye1.fill_color = "black"
    eye1.color = "black"
    window.add(eye1)

    eye2 = GOval(12, 12, x=205, y=184)
    eye2.filled = True
    eye2.fill_color = "black"
    eye2.color = "black"
    window.add(eye2)

    r_ear = GPolygon()
    r_ear.add_vertex((225, 170))
    r_ear.add_vertex((220, 240))
    r_ear.add_vertex((225, 260))
    r_ear.add_vertex((235, 260))
    r_ear.add_vertex((240, 250))
    r_ear.add_vertex((246, 235))
    r_ear.add_vertex((243, 210))
    r_ear.filled = True
    r_ear.fill_color = "saddlebrown"
    r_ear.color = "saddlebrown"
    window.add(r_ear)

    b1 = GPolygon()
    b1.add_vertex((170, 255))
    b1.add_vertex((174, 320))
    b1.add_vertex((240, 320))
    b1.add_vertex((310, 307))
    b1.add_vertex((310, 255))
    b1.filled = True
    b1.fill_color = "ivory"
    b1.color = "ivory"
    window.add(b1)

    feet1 = GOval(20, 50, x=175, y=300)
    feet1.filled = True
    feet1.fill_color = "ivory"
    feet1.color = "ivory"
    window.add(feet1)

    feet2 = GOval(20, 50, x=205, y=302)
    feet2.filled = True
    feet2.fill_color = "ivory"
    feet2.color = "ivory"
    window.add(feet2)

    feet3 = GOval(17, 65, x=263, y=281)
    feet3.filled = True
    feet3.fill_color = "ivory"
    feet3.color = "ivory"
    window.add(feet3)

    feet4 = GOval(20, 70, x=290, y=280)
    feet4.filled = True
    feet4.fill_color = "ivory"
    feet4.color = "ivory"
    window.add(feet4)

    spot1 = GArc(75, 60, 90, 180, x=293, y=255)
    spot1.filled = True
    spot1.fill_color = "chocolate"
    spot1.color = "chocolate"
    window.add(spot1)

    spot5 = GArc(75, 50, 130, 120, x=207, y=275)
    spot5.filled = True
    spot5.fill_color = "chocolate"
    spot5.color = "chocolate"
    window.add(spot5)

    spot2 = GPolygon()
    spot2.add_vertex((210, 255))
    spot2.add_vertex((215, 290))
    spot2.add_vertex((293, 290))
    spot2.add_vertex((303, 275))
    spot2.add_vertex((312, 255))
    spot2.filled = True
    spot2.fill_color = "saddlebrown"
    spot2.color = "saddlebrown"
    window.add(spot2)

    spot3 = GArc(43, 80, 180, 180, x=215, y=265)
    spot3.filled = True
    spot3.fill_color = "saddlebrown"
    spot3.color = "saddlebrown"
    window.add(spot3)

    spot4 = GArc(33, 50, 180, 180, x=260, y=272)
    spot4.filled = True
    spot4.fill_color = "saddlebrown"
    spot4.color = "saddlebrown"
    window.add(spot4)

    tail1 = GPolygon()
    tail1.add_vertex((313, 270))
    tail1.add_vertex((330, 240))
    tail1.add_vertex((330, 220))
    tail1.add_vertex((320, 210))
    tail1.add_vertex((318, 220))
    tail1.add_vertex((310, 260))
    tail1.filled = True
    tail1.fill_color = "saddlebrown"
    tail1.color = "saddlebrown"
    window.add(tail1)

    tail2 = GPolygon()
    tail2.add_vertex((330, 220))
    tail2.add_vertex((320, 210))
    tail2.add_vertex((318, 220))
    tail2.filled = True
    tail2.fill_color = "ivory"
    tail2.color = "ivory"
    window.add(tail2)

    label = GLabel("You deserve all the Love!", x=70, y=90)
    label.font = "Verdana-18-bold"
    window.add(label)

    heart1 = GPolygon()
    heart1.add_vertex((260, 150))
    heart1.add_vertex((270, 160))
    heart1.add_vertex((280, 150))
    heart1.add_vertex((290, 140))
    heart1.add_vertex((287, 130))
    heart1.add_vertex((284, 132))
    heart1.add_vertex((270, 136))
    heart1.add_vertex((256, 132))
    heart1.add_vertex((253, 130))
    heart1.add_vertex((250, 140))
    heart1.filled = True
    heart1.fill_color = "red"
    heart1.color = "red"
    window.add(heart1)


if __name__ == '__main__':
    main()

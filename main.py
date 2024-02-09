import turtle
boo = turtle.Turtle()
boo.shape("turtle")
boo.speed("slow")
boo.pensize(4)
boo.pu()

for i in range(2):
    boo.left(90)
    boo.forward(100)
boo.forward(250)
boo.left(90)
boo.left(90)
boo.right(90)
boo.pd()
# I
boo.forward(100)
boo.left(90)
# L
boo.pu()
boo.forward(50)
boo.left(90)
boo.forward(100)
boo.left(90)
boo.left(90)
boo.pd()
boo.forward(100)
boo.left(90)
boo.forward(65)
# O

boo.pu()
boo.forward(100)
boo.pd()
boo.fillcolor("green")
boo.begin_fill()
for i in range(5):
    boo.left(72)
    boo.forward(70)
boo.end_fill()
# V
boo.pu()
boo.forward(70)
boo.pd()
boo.fillcolor("coral")
boo.begin_fill()
boo.left(60)
boo.forward(120)
boo.pu()
boo.left(120)
boo.forward(120)
boo.pd()
boo.left(120)
boo.forward(120)

boo.end_fill()
# E
boo.left(60)
boo.pu()
boo.forward(70)
boo.left(90)
boo.pd()
boo.forward(100)
boo.right(90)
boo.forward(70)
## out
boo.right(90)
boo.right(90)
boo.forward(70)
boo.left(90)
## in
boo.forward(50)
boo.left(90)
boo.forward(70)
## out
boo.right(90)
boo.right(90)
boo.forward(70)
boo.left(90)
## in
boo.forward(50)
boo.left(90)
boo.forward(70)
# Y
boo.pu()
boo.forward(80)
boo.left(90)
boo.pd()

boo.fillcolor("blue")
boo.begin_fill()
boo.forward(50)
boo.right(45)
boo.forward(65)
boo.right(180)
boo.forward(65)

boo.right(90)
boo.forward(65)

# back
boo.right(180)
boo.forward(65)
boo.end_fill()
boo.right(45)
boo.forward(50)
boo.left(90)
# O
boo.pu()
boo.forward(135)
boo.pd()
boo.fillcolor("green")
boo.begin_fill()
for i in range(5):
    boo.left(72)
    boo.forward(70)
boo.end_fill()
# U
boo.pu()
boo.forward(20)
boo.left(90)
boo.forward(100)
boo.right(90)
boo.forward(25)
boo.pd()
boo.fillcolor("blue")
boo.begin_fill()
boo.right(90)
boo.forward(100)
boo.left(90)
boo.forward(60)
boo.left(90)
boo.forward(100)

boo.end_fill()
# boo.left(90)
# boo.pd()
# boo.forward(100)

boo.pu()
boo.forward(80)
boo.left(90)


def trace_line_hor():
    for i in range(6):
        boo.pd()
        boo.forward(20)
        boo.pu()
        boo.forward(20)
def trace_line():
    for i in range(10):
        boo.pd()
        boo.forward(20)
        boo.pu()
        boo.forward(20)

trace_line()

def love():
    boo.pd()
    boo.forward(20)
    boo.right(45)
    boo.pd()
    boo.forward(100)
    boo.right(90)
    boo.forward(50)
    boo.right(90)
    boo.forward(50)
    boo.left(90)
    boo.forward(50)
    boo.right(90)
    boo.forward(50)
    boo.right(90)
    boo.forward(100)
    boo.right(45)

boo.fillcolor("red")
boo.begin_fill()
love()
boo.end_fill()
trace_line()
for i in range(1):
    boo.pd()
    boo.forward(20)
    boo.pu()
    boo.forward(20)




boo.left(90)
trace_line_hor()
boo.left(90)
trace_line()
#######
boo.fillcolor("red")
boo.begin_fill()
love()
boo.end_fill()
trace_line()
for i in range(3):
    boo.pd()
    boo.forward(20)
    boo.pu()
    boo.forward(20)

boo.left(90)
trace_line_hor()
boo.left(90)
for i in range(2):
    boo.pd()
    boo.forward(20)
    boo.pu()
    boo.forward(20)

boo.pd()
boo.forward(20)
boo.pu()
boo.hideturtle()

my_screen = turtle.Screen()
my_screen.exitonclick()
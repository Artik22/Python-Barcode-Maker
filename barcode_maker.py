"""
barcode_maker.py
=====
This code asks the user for a barcode and checks if the barcode is valid (with upc.py). If the barcode is valid, it draws a barcode. 
"""

import turtle
import upc

t = turtle.Turtle()

wn = turtle.Screen()
wn.setup(500, 500)
wn.bgcolor('pink')

#wn.tracer(0)
#t.hideturtle()

x = -120
y = 100

#draws rectangle and fills it in
def draw_rectangle(x, y, w, h, t, color):

    t.color(color)
    t.begin_fill()
    t.up()
    t.goto(x, y)
    t.down()

    for i in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()

#opens up textbox and starts mechanism for control of the while loop
user_input = wn.textinput('Barcode Generator', 'Please enter a barcode number: ')
loop_control = upc.valid_barcode(user_input)

#Controls error message loop for wrong input
while loop_control == False:
    user_input = wn.textinput('Barcode Generator', 'Error: not valid, please enter another barcode number')
    loop_control = upc.valid_barcode(user_input)

#Generates bar widtsh
bars = upc.generate_bar_widths(user_input)

#Generates actual image of barcode
for i in range(0, len(bars)):
    num = int(bars[i])

    if i % 2 != 0:
        draw_rectangle(x, y, 2*num, 150, t, 'white')
        x += 1 + 2*num

    elif i % 2 == 0:
        draw_rectangle(x, y, 2*num, 150, t, 'black')
        x += 1 + 2*num

#wn.update()
#wn.exitonclick()
wn.mainloop()

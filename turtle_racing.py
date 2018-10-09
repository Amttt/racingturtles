# Written by Ann-Marie Thompson 10/8/2018

import turtle as t
import random as r

t.shape("turtle")
t.ht() 
t.penup()

# Initialize race track variables
x = -200
y = 200

t.setpos(x,y+10)
for step in range(16):
    t.write(step)
    t.forward(25)
t.pu()

beginning_track_pos = (x, y)
track_width = 35
track_length = 400
tracks = 5
t.setpos(beginning_track_pos)


### Draw race track with 4 run lanes
while tracks > 0:
    t.pd()
    t.forward(track_length)
    t.pu()
    t.seth(270)
    t.fd(track_width)
    beginning_track_pos = t.setpos(x, y-track_width)
    t.seth(0)
    y = y - track_width
    tracks = tracks - 1


# Initialize start positions
x = -200
y = 200

spot_list_y = []
turtle_position_list = []
i = 0

while i < 4:
    spot_list_y.append(y)
    y = y - track_width
    race_starting_spot = spot_list_y[i] - (track_width / 2)
    turtle_position_list.append(race_starting_spot)
    i = i+1
    


# Create turtle racers 
marc = t.Turtle(shape='turtle')
marc.color('green')
marc.pu()
marc.setpos(x,turtle_position_list[0])
marc.pd()
amt = t.Turtle(shape='turtle')
amt.color('blue')
amt.pu()
amt.setpos(x,turtle_position_list[1])
amt.pd()
veil = t.Turtle(shape='turtle')
veil.color('pink')
veil.pu()
veil.setpos(x,turtle_position_list[2])
veil.pd()
bert = t.Turtle(shape='turtle')
bert.color('yellow')
bert.pu()
bert.setpos(x,turtle_position_list[3])
bert.pd()


# Initialize race variables
movement = r.randint(0,4)
over = False
t.pd()


# Begin race loop
while over == False:
    marc.fd(movement)
    movement = r.randint(0,4)
    if marc.xcor() >= 200:
        t.write('MARC wins!', font=("Arial", 32, "normal"))
        over = True
    amt.fd(movement)
    movement = r.randint(0,4)
    if amt.xcor() >= 200:
        t.write('AMT wins!', font=("Arial", 32, "normal"))
        over = True
    veil.fd(movement)
    movement = r.randint(0,4)
    if veil.xcor() >= 200:
        t.write('VEIL wins!', font=("Arial", 32, "normal"))
        over = True
    bert.fd(movement)
    if bert.xcor() >= 200:
        t.write('BERT wins!', font=("Arial", 32, "normal"))
        over = True
    
    


    


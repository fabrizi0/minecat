#
# Code by Alexander Pruss and under the MIT license
#

from mineturtle import *

LENGHT = 150


def ladders(t, lenght, down=True):
    for i in range(lenght):
        if down:
            angle=90
        else:
            angle=-90
        t.go(1)
        t.down(angle)
        t.go(1)
        t.up(angle)
        if t.type() == block.BEDROCK:
            break


def bridge(t):
    for i in range(LENGHT):
        t.go(1)
        if t.type() != block.AIR:
            break

t = Turtle()
t.turtle(PIG)
t.pendelay(0.0)

t.penblock(block.BRICK_BLOCK)
t.push()

ladders(t,3,False)
t.position.y-=1

t.penblock(block.GLASS)
t.penwidth(1)
bridge(t)

t.pop()
t.push()

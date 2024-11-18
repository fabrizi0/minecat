#
# Code by Alexander Pruss and under the MIT license
#

from mineturtle import *

DEPTH = 150

def ladders(t, b = block.AIR, even=False):
    for i in range(DEPTH):
        if even:
            t.penblock(block.AIR)
            t.penup()
        t.go(1)
        t.down(90)

        if even:
            t.pendown()
            t.penblock(b)
        t.go(1)
        t.up(90)
        if t.type() == block.BEDROCK:
            break

t = Turtle()
t.turtle(PIG)
t.pendelay(0.0)

t.penblock(block.AIR)
t.push()
t.go(5)

t.penwidth(3)
ladders(t, block.AIR, False)

t.pop()
t.push()
t.go(8)

t.penwidth(1)
ladders(t, block.GLOWING_OBSIDIAN, True)

t.pop()
t.push()
t.go(2)

t.penwidth(1)
ladders(t, block.STAIRS_BIRCH, True)

t.pop()
t.push()
t.right(90)
t.go(1)
t.left(90)
t.go(3)

t.penwidth(1)
ladders(t,block.TORCH, True)

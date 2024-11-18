#
# Code by Alexander Pruss and under the MIT license
#

from mineturtle import *

DEPTH = 150

def tunnel(t, b = block.AIR,):
    t.penblock(b)
    for i in range(DEPTH):
        t.go(1)
        if t.type() == block.BEDROCK:
            break

t = Turtle()
t.turtle(PIG)
t.pendelay(0.0)

t.penblock(block.AIR)
t.push()
t.go(2)

t.penwidth(3)
tunnel(t, block.AIR)

t.pop()
t.push()
t.go(2)
t.down(90)
t.go(2)
t.up(90)

t.penwidth(1)
tunnel(t, block.GLASS)

t.pop()
t.push()
t.go(3)
t.up(90)
t.go(2)
t.down(90)

t.penwidth(1)
tunnel(t, block.GLOWING_OBSIDIAN)

t.pop()
t.push()
t.right(90)
t.go(2)
t.left(90)
t.go(3)

t.penwidth(1)
tunnel(t,block.TORCH)

#
# Code by Alexander Pruss and under the MIT license
#

from mineturtle import *

DEPTH = 150


def ladders(t, b=block.AIR, angle=-45, blockers=[block.AIR], depth=DEPTH):
    t.penblock(b)
    t.up(angle)

    for i in range(depth):
        t.go(1)
        if t.type() in blockers:
            return i


t = Turtle()
t.turtle(PIG)
t.pendelay(0.0)

rotation, _ = t.getMinecraftAngles()

if rotation < 0:
    rotation += 360
r = int((rotation + 45) / 90) % 4 * 90

t.angle(r)
angle=45

t.penblock(block.AIR)
t.push()
t.go(3)
t.up(90)
t.go(1)
t.down(90)

depth = ladders(t, block.AIR, angle=angle)


t.pop()
t.push()
t.go(3)
t.up(90)
t.go(1)
t.down(90)
t.penwidth(3)
t.post(f"air")
ladders(t, block.AIR, angle=angle, depth=depth, blockers=[])

t.pop()
t.push()
t.penwidth(1)
t.go(2)
t.up(90)
t.go(2)
t.down(90)
t.penwidth(1)
# t.lateral(90)
t.post(f"light: {depth}")
ladders(t, block.GLOWING_OBSIDIAN, angle=angle, depth=depth, blockers=[])


t.pop()
t.push()

t.go(3)
t.down(90)
t.go(2)
t.up(90)
# t.lateral(90)

t.post(f"glass")
ladders(t, block.GLASS, angle=angle)


t.pop()
t.push()
t.go(2)
t.down(90)
t.go(2)
t.up(90)
t.lateral(-90)
t.post(f"light: {depth}")
ladders(t, block.CONCRETE_BLOCK, angle=angle)

t.pop()
t.push()
t.go(2)
t.down(90)
t.go(1)
t.up(90)
t.lateral(-90)
t.post(f"rail: {depth}")
ladders(t, block.RAIL_GOLDEN, angle=angle)

t.pop()
t.push()
t.go(3)
t.down(90)
t.go(1)
t.up(90)
t.lateral(90)
t.post(f"ladder: {depth}")

b = {
    0: block.STAIRS_COBBLESTONE_1,
    90: block.STAIRS_COBBLESTONE_2,
    180: block.STAIRS_COBBLESTONE_3,
    270: block.STAIRS_COBBLESTONE_0,
}

ladders(t, b[r], angle=angle)
t.post(f"rotation: {rotation}, {r}")
t.post(f"finished")

t.pop()
t.push()
t.penwidth(3)
t.go(3)

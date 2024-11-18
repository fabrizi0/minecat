from mine import *
import random
import sys


def getHeightBelow(x, y, z):
    if isPE:
        return min(mc.getHeight(x, z), y)
    else:
        y0 = y - 255
        while y > y0:
            if mc.getBlock(x, y, z) != block.AIR.id:
                return y
            y -= 1
        return min(mc.getHeight(x, z), y)


def rectangularPrism(x1, y1, z1, x2, y2, z2, distribution, offset=Vec3(0,0,0)):
    x1 = int(round(x1 + offset.x))
    y1 = int(round(y1 + offset.y))
    z1 = int(round(z1 + offset.z + 1))
    x2 = int(round(x2 + offset.x))
    y2 = int(round(y2 + offset.y))
    z2 = int(round(z2 + offset.z + 1))
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            for z in range(min(z1, z2), max(z1, z2) + 1):
                if isinstance(distribution, Block):
                    mc.postToChat(f"Metto un blocco: {x},{y},{z}")
                    mc.setBlock(x, y, z, distribution)
                else:
                    r = random.random()
                    for p, b in distribution:
                        r -= p
                        if r < 0:
                            mc.setBlock(x, y, z, b)
                            break


# Note: the first set of coordinates must be smaller than the second
def wall(x1, y1, z1, x2, y2, z2, baseHeight, altHeight, distribution):
    x = x1
    z = z1

    while True:
        if (x - x1 + z - z1) % 2 == 0:
            height = altHeight
        else:
            height = baseHeight
        y0 = getHeightBelow(x, y1, z)
        rectangularPrism(x, y0, z, x, y1 + height, z, distribution)
        if x >= x2 and z >= z2:
            return
        if x < x2:
            x = x + 1
        if z < z2:
            z = z + 1

distribution = (
    (1, Block(block.OBSIDIAN.id, 0)),
)

mc = Minecraft()
pos = mc.player.getTilePos()
mc.postToChat(f"Siamo nella posizione: {pos}, {dir(pos)}")


LARGHEZZA=4
LUNGHEZZA=4
ALTEZZA=3


def finestre(offset):
    # finestre
    rectangularPrism(0, 1, 0, LARGHEZZA, 1, LUNGHEZZA, block.GLASS, offset=offset)
    rectangularPrism(1, 1, 1, LARGHEZZA - 1, 1, LUNGHEZZA - 1, block.AIR, offset=offset)


def porta(offset):
    mc.setBlock(
        offset.x + LARGHEZZA / 2 + 1,
        offset.y + 1,
        offset.z + 1,
        block.HARDENED_CLAY_STAINED,
    )
    mc.setBlock(
        offset.x + LARGHEZZA / 2 - 1,
        offset.y + 1,
        offset.z + 1,
        block.HARDENED_CLAY_STAINED,
    )

    mc.setBlock(
        offset.x + LARGHEZZA / 2, offset.y, offset.z + 1, block.DOOR_WOOD_BOTTOM
    )
    mc.setBlock(
        offset.x + LARGHEZZA / 2, offset.y + 1, offset.z + 1, block.DOOR_WOOD_UP
    )


def bunker(
    offset,
    pavimento=block.CONCRETE_BLOCK_GRAY,
    muri=block.HARDENED_CLAY_STAINED,
    tetto=block.SEA_LANTERN,
):

    # preparare il posto
    rectangularPrism(-1, -1, -1, LARGHEZZA + 1, ALTEZZA + 1 , LUNGHEZZA + 1, block.AIR, offset=offset)

    # Pavimento
    rectangularPrism(
        -1, -3, -1, LARGHEZZA+1, -1, LUNGHEZZA+1, pavimento, offset=offset
    )

    # muro 1 davanti
    rectangularPrism(
        0, 0, 0, LARGHEZZA, ALTEZZA, 0, muri, offset=offset
    )

    # muro 2 sinistra
    rectangularPrism(
        0, 0, 0, 0, ALTEZZA, LUNGHEZZA, muri, offset=offset
    )

    # muro 3 dietro
    rectangularPrism(
        0,
        0,
        LUNGHEZZA,
        LARGHEZZA,
        ALTEZZA,
        LUNGHEZZA,
        muri,
        offset=offset,
    )

    # muro 4 destra
    rectangularPrism(
        LARGHEZZA,
        0,
        0,
        LARGHEZZA,
        ALTEZZA,
        LUNGHEZZA,
        muri,
        offset=offset,
    )

    # tetto
    rectangularPrism(
        0,
        ALTEZZA,
        0,
        LARGHEZZA,
        ALTEZZA,
        LUNGHEZZA,
        tetto,
        offset=offset,
    )
    rectangularPrism(
        0,
        ALTEZZA+1,
        0,
        LARGHEZZA,
        ALTEZZA+1,
        LUNGHEZZA,
        muri,
        offset=offset,
    )

    finestre(pos)
    porta(pos)


bunker(pos)

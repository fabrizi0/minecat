from mine import *
import random
import sys


mc = Minecraft()
pos = mc.player.getTilePos()

def c(text):
    return text


# def sign(text1, text2="", headingAngle=180):
#     mc.setBlockWithNBT(
#         mc.player.getTilePos(), block.SIGN(text1, text2, headingAngle=headingAngle)
#     )


def sign(x, y, z, text1, text2="", headingAngle=0):
    mc.setBlockWithNBT(
        x, y, z, block.SIGN(text1, text2, headingAngle=headingAngle)
    )


RANGE=256
OPTIONS=16

mc.setBlocks(
    pos.x,
    pos.y - 1,
    pos.z,
    pos.x + RANGE + 2,
    pos.y - 1,
    pos.z + 4 + OPTIONS,
    block.CONCRETE_BLOCK,
)


for p in range(RANGE):
    for k in range(OPTIONS):
        sign(pos.x + p, pos.y, pos.z + 1, f"{p}")
        mc.setBlock(pos.x + p, pos.y , pos.z + 2 + k, Block(p, k))
        mc.setBlock(pos.x + p, pos.y -1, pos.z , block.GLOWSTONE_BLOCK)
        # mc.setBlock(pos.x + p, pos.y + k, pos.z + 1, block.SIGN(f"{k}"))



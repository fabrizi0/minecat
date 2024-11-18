from mine import *
import random
import sys


mc = Minecraft()
pos = mc.player.getTilePos()


def sign(x, y, z, text1, text2="", headingAngle=0):
    mc.setBlockWithNBT(
        x, y, z, block.SIGN(text1, text2, headingAngle=headingAngle)
    )


RANGE=16
OPTIONS=16

mc.setBlocks(
    pos.x,
    pos.y - 1,
    pos.z,
    pos.x + RANGE * 3 + 2,
    pos.y - 1,
    pos.z + 4 + OPTIONS,
    block.CONCRETE_BLOCK,
)


# for p in range(0,RANGE*3,3):
#     sign(pos.x + p, pos.y, pos.z + 1, f"{p/3}")
#     mc.setBlock(pos.x + p, pos.y -1, pos.z , block.GLOWSTONE_BLOCK)

#     for k in range(OPTIONS):
#         mc.setBlock(pos.x + p, pos.y, pos.z + 2 + k, block.BRICK_BLOCK)
#         mc.setBlock(pos.x + p, pos.y+1, pos.z + 2 + k, block.BRICK_BLOCK)
#     for k in range(OPTIONS):
#         mc.setBlock(pos.x + p + 1, pos.y, pos.z + 2 + k, Block(64, k))
#         mc.setBlock(pos.x + p + 1, pos.y + 1, pos.z + 2 + k, Block(64, k+ int(p/3)))
#         sign(pos.x + p, pos.y+2, pos.z + 2 + k, f"{int(p/3)} - {k}")


p=12
k=4
mc.setBlock(pos.x + p, pos.y, pos.z + 2 + k, block.BRICK_BLOCK)
mc.setBlock(pos.x + p, pos.y + 1, pos.z + 2 + k, block.BRICK_BLOCK)

mc.setBlock(pos.x + p + 1, pos.y, pos.z + 2 + k, Block(64, k))
mc.setBlock(pos.x + p + 1, pos.y + 1, pos.z + 2 + k, Block(64, k + p/3 ))

mc.setBlock(pos.x + p + 2, pos.y, pos.z + 2 + k, block.BRICK_BLOCK)
mc.setBlock(pos.x + p + 2, pos.y + 1, pos.z + 2 + k, block.BRICK_BLOCK)

sign(pos.x + p, pos.y + 2, pos.z + 2 + k, f"{int(k+ p/3)} - {k}")

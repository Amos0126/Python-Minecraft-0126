
from mcpi.minecraft import Minecraft
a = Minecraft.create()
while True:
    x,y,z = a.player.getTilePos()
    block1 = a.getBlock(x,y-1,z)
    block2 = a.getBlock(x+1,y-1,z)
    block3 = a.getBlock(x-1,y-1,z)
    block4 = a.getBlock(x,y-1,z+1)
    block5 = a.getBlock(x,y-1,z-1)
    if block1 == 8 or block1 == 9 or block2 == 8 or block2 == 9\
    or block3 == 8 or block3 == 9 or block4 == 8 or block4 == 9 or\
    block5 == 8 or block5 == 9:
        a.setBlock(x,y-1,z,79)
        a.setBlock(x,y-1,z+1,79)
        a.setBlock(x,y-1,z-1,79)
        a.setBlock(x-1,y-1,z,79)
        a.setBlock(x+1,y-1,z,79)
from mcpi.minecraft import Minecraft
a = Minecraft.create()

x,y,z = a.player.getTilePos()

while True:
    a.setBlock(x,y,z+1,7)
    a.setBlock(x,y,z-1,7)
    a.setBlock(x-1,y,z,7)
    a.setBlock(x+1,y,z,7)
    a.setBlock(x+1,y,z+1,7)
    a.setBlock(x-1,y,z+1,7)
    a.setBlock(x+1,y,z-1,7)
    a.setBlock(x-1,y,z-1,7)
    y = y+1

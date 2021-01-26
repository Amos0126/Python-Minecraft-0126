from mcpi.minecraft import Minecraft
a = Minecraft.create()

import random
while True:
    x,y,z = a.player.getTilePos()
    
    c = random.randrange(0,16)
    a.setBlocks(x+1000,y,z+1000,x-1000,y+1000,z-100,0)
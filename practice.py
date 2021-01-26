
from mcpi.minecraft import Minecraft
a = Minecraft.create()
import random,time
while True:
    x,y,z = a.player.getTilePos()
    
    f = random.randrange(38,40)
    c = random.randrange(0,9)
    a.setBlock(x,y,z-1,f,c)
    time.sleep(0.1)

from mcpi.minecraft import Minecraft
a = Minecraft.create()
x,y,z = a.player.getTilePos()

long = 10
big = 10
high = 10

block = 45
air = 0

a.setBlocks(x,y,z,x+long,y+big,z+high,block)
a.setBlocks(x+1,y+1,z+1,x+long-1,y+big-1,z+high-1,air)
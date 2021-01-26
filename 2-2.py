from mcpi.minecraft import Minecraft
a = Minecraft.create()

x,y,z = a.player.getTilePos()

a.setBlock(x,y,z+2,7)
a.setBlock(x,y,z-2,7)
a.setBlock(x+2,y,z,7)
a.setBlock(x-2,y,z,7)
a.setBlock(x+1,y,z+1,7)
a.setBlock(x-1,y,z+1,7)
a.setBlock(x+1,y,z-1,7)
a.setBlock(x-1,y,z-1,7)
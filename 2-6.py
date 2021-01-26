from mcpi.minecraft import Minecraft
a = Minecraft.create()

x,y,z = a.player.getTilePos()

ans = int(input('What do you want to put?'))
a.setBlock(x+1,y,z,ans)
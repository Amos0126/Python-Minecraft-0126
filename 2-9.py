from mcpi.minecraft import Minecraft
a = Minecraft.create()

x,y,z = a.player.getTilePos()
a.setSign(x,y,z+1,63,0,["Welcome","to","My City!"])
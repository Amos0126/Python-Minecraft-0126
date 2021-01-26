from mcpi.minecraft import Minecraft
a = Minecraft.create()

x,y,z = a.player.getTilePos()

try:
    ans = int(input('What do you want to put?'))
    a.setBlock(x+1,y,z,ans)
except:
    print('try agian!You can only tape number(s)')


   
    
    # a.setBlock(x+1,y,z,ans)
    #print('try agian!')
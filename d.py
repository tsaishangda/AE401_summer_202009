from mcpi.minecraft import Minecraft
mc =Minecraft.create()

x,y,z = mc.player.getTilePos()

for i in range(20):
    mc.setBlocks(x+i,y-1,z+i,x+2+i,y,z+i,1)
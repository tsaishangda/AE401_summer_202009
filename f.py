from mcpi.minecraft import Minecraft
mc =Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlocks(x,y+3,z,x+2,y+2+3,z+2,18)
mc.setBlocks(x+1,y,z+1,x+1,y+4,z+1,17)
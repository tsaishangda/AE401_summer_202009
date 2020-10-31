from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

try:
     blockId = int(input('方塊ID'))
     mc.setBlock(x,y,z,blockId)
     
except:
    mc.postToChat("???")
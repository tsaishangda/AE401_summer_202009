import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

for i in range(20):
    
    d = random.randrange(1,5)
    
    if d == 1:
        mc.setBlocks(x,y,z,x+4,y+4,z,57)
        x = x+4
        y = y+4 
    if d == 2:   
        mc.setBlocks(x,y,z,x-4,y-4,z,57)
        x = x-4
        y = y-4
    if d == 3:    
        mc.setBlocks(x,y,z,x,y,z+4,57)
        z = z+4
    if d == 4:
        mc.setBlocks(x,y,z,x,y,z-4,57)
        z = z-4
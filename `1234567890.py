
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

n = 1

for i in range(5):
    
    for j in range(n):
        mc.spawnEntity(x,y,z,50)
        
    n = n*2
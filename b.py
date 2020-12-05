from mcpi.minecraft import Minecraft
import random
import time

x,y,z = mc.player.getTilePos()

while True:
    y = y+30
    x = x+random.uniform(-20,20)
    z = z+random.uniform(-20,20)

    mc.spawnEntity(x,y,z,63)
    
    time.sleep(0.1)
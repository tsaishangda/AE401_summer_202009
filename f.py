from mcpi.minecraft import Minecraft
mc =Minecraft.create()

def plantTree(x,y,z):
    mc.setBlocks(x,y+3,z,x+2,y+2+3,z+2,18)
    mc.setBlocks(x+1,y,z+1,x+1,y+4,z+1,17)

a,b,c = mc.player.getTilePos()

for i in range(10):
    for j in range(10):
        for k in range(10):    
            plantTree(a+i*5,b+j*i,c+k*i)
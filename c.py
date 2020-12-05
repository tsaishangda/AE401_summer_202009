from mcpi.minecraft import Minecraft
mc =Minecraft.create()

while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos
        block = mc.getBlock(x,y,z)
        
        mc.createExplosion(x,y,z,666)
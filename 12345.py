# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 10:59:19 2020

@author: tsais
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getTilePos()
    
    a = mc.getBlock(x+1,y-1,z)
    b = mc.getBlock(x-1,y-1,z)
    c = mc.getBlock(x,y-1,z+1)
    d = mc.getBlock(x,y-1,z-1)
    
    if a==8 or a==9 or b==8 or b==9 or c==8 or c==9 or d==8 or d==9:
        mc.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,57)
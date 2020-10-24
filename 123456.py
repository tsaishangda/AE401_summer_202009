# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:40:11 2020

@author: tsais
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

a = 0
while a<20:
    mc.setBlocks(x+30,y-1,z,x-30,y-10,z,19)
    z+=5
    a+=1
    
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 11:28:24 2020

@author: tsais
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

l = 50
w = 50
h = 50

b = 46
a = 0
la = 169

mc.setBlocks(x,y,z,x+l,y+h,z+w,b)
mc.setBlocks(x+1,y+1,z+1,x+l-1,y+h-1,z+w-1,a)

mc.setBlocks(x,y+h,z,x+l,y+h,z+w,la)

mc.setBlocks(x+1,y+(h/2),z+1,x+l-1,y+(h/2),z+w-1,la)
mc.setBlocks(x+2,y+(h/2),z+2,x+l-2,y+(h/2),z+w-2,a)

mc.setBlocks(x+3,y+1,z,x+6,y+3,z,a)
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 11:11:34 2020

@author: tsais
"""

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

time.sleep(10)

x,y,z = mc.player.getTilePos()

mc.setBlock(x,y,z,57)
time.sleep(1)
mc.setBlock(x+1,y+1,z,57)
time.sleep(1)
mc.setBlock(x,y+2,z+1,57)
time.sleep(1)
mc.setBlock(x+1,y+3,z+1,57)


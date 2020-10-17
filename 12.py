# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:55:24 2020

@author: tsais
"""

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

time.sleep(10)

x,y,z = mc.player.getTilePos()

mc.setBlock(x,y,z,57)
time.sleep(1)
mc.setBlock(x,y+1,z,57)
time.sleep(1)
mc.setBlock(x,y+2,z,57)
time.sleep(1)
mc.setBlock(x,y+3,z,57)
time.sleep(1)
mc.setBlock(x,y+4,z,57)
time.sleep(1)
mc.setBlock(x,y+5,z,57)
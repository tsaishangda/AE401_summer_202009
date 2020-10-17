# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 11:28:24 2020

@author: tsais
"""

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

time.sleep(10)

x,y,z = mc.player.getTilePos()

mc.setBlocks(x+50,y-1,z+50,x-50,y-1,z-50,57)
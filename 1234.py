# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 10:33:25 2020

@author: tsais
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 50
y = 50
z = 50

mc.setBlocks(x,y,z,0)
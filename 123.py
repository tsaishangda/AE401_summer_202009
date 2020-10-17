# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:17:13 2020

@author: tsais
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    x,y,z = mc.player.getTilePos()
    mc.postToChat(
            "You are located on X:"+
            str(x) +
            ", Y:" +
            str(y) +
            ", Z:" +
            str(z))
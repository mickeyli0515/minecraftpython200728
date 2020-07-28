# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:01:00 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()


w = 10
h = 10
l = 10




x,y,z = mc.player.getTilePos()
mc. setBlocks(x,y,z,w+x,y+h,z+l,57)
mc. setBlocks(x+1,y+1,z+1,w+x-1,y+h-1,z+l-1,0)

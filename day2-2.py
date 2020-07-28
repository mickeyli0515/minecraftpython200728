# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:21:44 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

from mcpi.minecraft import Minecraft

color = random.randrange(0,16)
mc. setBlocks(x+5,y-1,z+5,x+5,y-1,z+5,95,color)

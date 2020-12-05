import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    mc.executeCommand("time add 10000")
    time.sleep(0.05)
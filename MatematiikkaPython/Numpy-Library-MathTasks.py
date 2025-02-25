import numpy as np
import math

#Tehtava 1
#osa a
r = 2.493
print(f"{r} Radians = {np.degrees(r)} degrees")

#osa b
r = 0.911
print(f"{r} Radians = {np.degrees(r)} degrees")

#Tehtava 2
#osa a
d = 137.7
print(f"{d} Degrees = {np.radians(d)} radians")

#osa b
d = 62.3
print(f"{d} Degrees = {np.radians(d)} radians")

#Tehtava 3
degs = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
print("---")
for i in degs:
  print(f"{i} Degrees = {np.radians(i)} radians")

#Tehtava 2.2.1: 1.
print(f"Hypotenouse of the triangle is {np.hypot(1.6, 2.3)} meters")
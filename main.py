import os
import matplotlib
import subprocess

#SETTINGS
GRAVITY = 9.81
HEIGHT_DIFF = 0 #difference between start height and stop height

v_y = float(input("Prędkość w osi Y (w m/s): "))
v_x = float(input("Prędkość w osi X (w m/s): "))
alfa = float(input("Kąt nachylenia do podłoża (w stopniach): "))

print(v_y, v_x, alfa)

import matplotlib
import utils

#SETTINGS
GRAVITY = 9.81
HEIGHT_DIFF = 0 #difference between start height and stop height
STEPS = 1000

#IMPUT PARAMETERS
v_y = float(input("Prędkość w osi Y (w m/s): "))
v_x = float(input("Prędkość w osi X (w m/s): "))

#SETTINGS FILE GENERATION
f = open('settings', 'w')
f.write(str(GRAVITY) + ' ')
f.write(str(HEIGHT_DIFF) + ' ')
f.write(str(STEPS) + ' ')
f.write(str(v_y) + ' ')
f.write(str(v_x) + ' ')
f.close()

utils.execute('kaczka_dziwaczka', 'settings')

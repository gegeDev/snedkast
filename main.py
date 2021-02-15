import matplotlib
import utils

#SETTINGS
GRAVITY = 9.81
HEIGHT_DIFF = 0 #difference between start height and stop height
STEPS = 1000
f = open('settings', 'w')
f.write(str(GRAVITY) + ' ')
f.write(str(HEIGHT_DIFF) + ' ')
f.write(str(STEPS) + ' ')
f.close()

v_y = float(input("Prędkość w osi Y (w m/s): "))
v_x = float(input("Prędkość w osi X (w m/s): "))
alfa = float(input("Kąt nachylenia do podłoża (w stopniach): "))

utils.mkdir("bins")

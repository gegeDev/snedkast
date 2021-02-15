from matplotlib import pyplot
import utils

#SETTINGS
GRAVITY = 9.81
HEIGHT_DIFF = 0 #difference between start height and stop height
STEPS = 1000

#IMPUT PARAMETERS
v_y = float(input("Prędkość w osi Y (w m/s): "))
v_x = float(input("Prędkość w osi X (w m/s): "))
name = input("Nazwa pliku z pomiarem: ")

#SETTINGS FILE GENERATION
f = open('settings', 'w')
f.write(str(GRAVITY) + ' ')
f.write(str(HEIGHT_DIFF) + ' ')
f.write(str(STEPS) + ' ')
f.write(str(v_y) + ' ')
f.write(str(v_x) + ' ')
f.close()

utils.execute(name, 'settings')

f = open('results/{}/{}.txt'.format(name, name))
x = []
y = []
for line in f:
    temp = [float(i) for i in line.split()]
    x.append(temp[1])
    y.append(temp[2])
f.close()

pyplot.plot(x, y)
pyplot.savefig('results/{}/{}.pdf'.format(name, name))

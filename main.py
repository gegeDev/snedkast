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
v = []
t = []
for line in f:
    temp = [float(i) for i in line.split()]
    t.append(temp[0])
    x.append(temp[1])
    y.append(temp[2])
    v.append(temp[3])
f.close()

fig, axs = pyplot.subplots(2)
fig.tight_layout()
axs[0].plot(x, y)
axs[0].set_title('Position chart')
axs[1].plot(t, v)
axs[1].set_title('Velocity over time')
fig.savefig('results/{}/{}.pdf'.format(name, name))

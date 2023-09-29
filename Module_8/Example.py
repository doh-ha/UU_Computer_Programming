import matplotlib.pyplot as plt  # alias
from math import pi, sin

# Data for plotting
L = 100
time = list(range(L))
print(time)
Voltage = [sin(2*pi*t/L) for t in time]

fig, ax = plt.subplots()  # create the frame of the figure
# plots the data previously calculated in time and voltage
ax.plot(time, Voltage)

# set label for both axes and a header for the whole figure
ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='Example 1')
ax.grid()  # create grid

fig.savefig("test.png")  # save figure as png file with specified filename
plt.show()  # displays the figure in a new window

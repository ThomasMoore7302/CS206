import pyrosim
import random
import matplotlib
import matplotlib.pyplot as plt
from robot import ROBOT

# Defining a simulation without a pause.
for i in range(0,10):
    sim = pyrosim.Simulator( play_paused = False , eval_time = 500 )

    robot = ROBOT( sim, random.random()*2 - 1 )

    # Running the simulation.
    sim.start()

    sim.wait_to_finish()

# Collecting the sensor data and displaying it on screen.
#sensorData = sim.get_sensor_data( sensor_id = P2 )
#print(sensorData)

# Setting up the graphs using matplotlib that collect sensorData.
# Creates the figure.
#f = plt.figure()
# Adds a drawing panel inside the figure.
#panel = f.add_subplot( 111 )
# Plots the data.
#plt.plot(sensorData)
# Sets graph limits.
#panel.set_ylim( -3, +1 )
# Shows the figure.
#plt.show()


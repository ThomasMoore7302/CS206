import pyrosim
import matplotlib
import matplotlib.pyplot as plt

# Defining a simulation without a pause.
sim = pyrosim.Simulator( play_paused = False , eval_time = 100 )


# Creating two different colored cylinders.
whiteObject = sim.send_cylinder ( x = 0 , y = 0 , z = 0.6 ,
                                  length = 1.0 , radius = 0.1 )

redObject = sim.send_cylinder ( x = 0 , y = 0.5 , z = 1.1 ,
                                length = 1.0 ,radius = 0.1 ,
                                r = 1 , g = 0 , b = 0,
                                r1 = 0 , r2 = 1 , r3 = 0 ) 

# Attaching the two cylinders using a joint.
joint = sim.send_hinge_joint( first_body_id = whiteObject ,
                              second_body_id = redObject ,
                              x = 0 , y = 0 , z = 1.1 ,
                              n1 = -1 , n2 = 0 , n3 = 0 ,
                              lo = -3.14159/2 , hi = 3.14159/2 )

# Creating touch sensors inside the cylinders.  
TO = sim.send_touch_sensor( body_id = whiteObject )

T1 = sim.send_touch_sensor( body_id = redObject ) 

# Creating a proprioceptive sensor inside the joint.
P2 = sim.send_proprioceptive_sensor( joint_id = joint )

# Creating a ray sensor inside redObject, at the tip, and at which direction.

#R3 = sim.send_ray_sensor( body_id = redObject,
#                          x = 0 , y = 1.1 , z = 1.1 ,
#                          r1 = 0 , r2 = 1 , r3 = 0 )

# and one inside redObject, at the bottom, and at which direction.
R3 = sim.send_ray_sensor( body_id = redObject,
                          x = 0 , y = .6 , z = 1.1 ,
                          r1 = 0 , r2 = -1 , r3 = -1 )

# Running the simulation.
sim.start()

sim.wait_to_finish()

# Collecting the sensor data and displaying it on screen.
sensorData = sim.get_sensor_data( sensor_id = R3 )
print(sensorData)

# Setting up the graphs using matplotlib that collect sensorData.
# Creates the figure.
f = plt.figure()
# Adds a drawing panel inside the figure.
panel = f.add_subplot( 111 )
# Plots the data.
plt.plot(sensorData)
# Sets graph limits.
panel.set_ylim( -1, +2 )
# Shows the figure.
plt.show()


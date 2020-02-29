import pyrosim
import matplotlib

class ROBOT:
    def __init__( self, sim, wts ):
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

        # Creating a ray sensor inside redObject, at the tip, and at which
        #direction.

        R3 = sim.send_ray_sensor( body_id = redObject,
                                  x = 0 , y = 1.1 , z = 1.1 ,
                                  r1 = 0 , r2 = 1 , r3 = 0 )


        # Creating a postion sensor.
        self.P4 = sim.send_position_sensor( body_id = redObject )

        # Creating sensor neurons.
        SN0 = sim.send_sensor_neuron( sensor_id = TO )
        SN1 = sim.send_sensor_neuron( sensor_id = T1 )
        SN2 = sim.send_sensor_neuron( sensor_id = P2 )
        SN3 = sim.send_sensor_neuron( sensor_id = R3 )

        # Creating a dictionary to store sensor neurons ID's
        sensorNeurons = {}
        sensorNeurons[ 0 ] = SN0
        sensorNeurons[ 1 ] = SN1
        sensorNeurons[ 2 ] = SN2
        sensorNeurons[ 3 ] = SN3
        
        # Creating motor neuron.
        MN2 = sim.send_motor_neuron( joint_id = joint ) 

        # Creating a dictionary to store motor neuron ID's.
        motorNeurons = {}
        motorNeurons[ 0 ] = MN2
        
        # Creating synapse.
        for s in sensorNeurons:
            for m in motorNeurons:
                sim.send_synapse( source_neuron_id = s ,
                                  target_neuron_id = m ,
                                  weight = wts[ s ] )
        

        

    

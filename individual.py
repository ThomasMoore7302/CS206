from __future__ import print_function
import random
import pyrosim
import math
import numpy
from robot import ROBOT

class INDIVIDUAL:
    def __init__( self, i ):
        self.ID = i
        self.genome = (numpy.random.rand(4,8) - 0.5) * 2
        self.fitness = 0

    def Start_Evaluate( self , pb ):
        # Defining a simulation without a pause.
        self.sim = pyrosim.Simulator( play_paused = False ,
                                 eval_time = 300 ,
                                 play_blind = pb )
        self.robot = ROBOT( self.sim, self.genome )
        self.sim.start()
        
    def Compute_Fitness( self ):
        self.sim.wait_to_finish()

        # Collecting the sensor data
        #x = self.sim.get_sensor_data( sensor_id = self.robot.P4 ,
        #                            svi = 0 )
        
        y = self.sim.get_sensor_data( sensor_id = self.robot.P4 ,
                                    svi = 1 )

        #z = self.sim.get_sensor_data( sensor_id = self.robot.P4 ,
        #                            svi = 2 )

        self.fitness = y[ -1 ]

        del self.sim
        
    def Mutate( self ):
        # Mutation used on children to differ them from parents for comparison.
        r = random.randint( 0 , 3 )
        c = random.randint( 0 , 7 )
    
        self.genome[ r , c ] = random.gauss( self.genome[ r , c ] ,
                                             math.fabs( self.genome[ r , c ]))
        
        if self.genome[ r , c ] > 1:
            self.genome[ r , c ] = 1
        elif self.genome[ r , c ] < -1:
            self.genome[ r , c ] = -1

        
    def Print( self ):
	    print( '[' , self.ID , self.fitness , ']' , end=' ' )
	    

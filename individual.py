import random
import pyrosim
import math
import numpy
from robot import ROBOT

class INDIVIDUAL:
    def __init__( self ):
        self.genome = numpy.random.random( 4 ) * 2 - 1
        self.fitness = 0

    def Start_Evaluate( self , pb ):
        # Defining a simulation without a pause.
        self.sim = pyrosim.Simulator( play_paused = False ,
                                 eval_time = 500 ,
                                 play_blind = pb )
        self.robot = ROBOT( self.sim, self.genome )
        self.sim.start()
        
    def Compute_Fitness( self ):
        self.sim.wait_to_finish()

        # Collecting the sensor data
        y = self.sim.get_sensor_data( sensor_id = self.robot.P4 ,
                                 svi = 1 )
        self.fitness = y[ -1 ]

    def Mutate( self ):
        # Mutation used on children to differ them from parents for comparison.
        geneToMutate = random.randint( 0 , 3 )
        self.genome[ geneToMutate ] = random.gauss( self.genome[ geneToMutate ] ,
                                                    math.fabs( self.genome[ geneToMutate ] ) )

    def Print( self ):
        print( self.genome )

from __future__ import print_function
import copy
import pickle
import pyrosim
import random
import matplotlib
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL
from population import POPULATION


pop = POPULATION(5)
pop.Evaluate()
pop.Print()


#parent = INDIVIDUAL()
#parent.Evaluate( False )

#for i in range( 0 , 100 ):
    #child = copy.deepcopy( parent )
    #child.Mutate()
    #child.Evaluate( True )
    #print( '[g:' , i , ']' ,
           #'[pw:', parent.genome , ']' , 
           #'[p:' , parent.fitness , ']' ,
           #'[c:' , child.fitness , ']' ) 
    #if ( child.fitness > parent.fitness ):
        #parent = child
        #parent.Evaluate( False )
        #f = open( 'robot.p' , 'w' )
        #pickle.dump( parent , f )
        #f.close()
        


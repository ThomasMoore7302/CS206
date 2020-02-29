from __future__ import print_function
import copy
import pickle
import pyrosim
import random
import matplotlib
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL

# Create a parent and show it
parent = INDIVIDUAL()
parent.Evaluate( False )

for i in range( 0 , 100 ):
    # Make a copy of the parent and name it child.
    child = copy.deepcopy( parent )
    # Mutate the child so it differs from the parent.
    child.Mutate()
    # Evaluate the mutation.
    child.Evaluate( True )
    print( '[g:' , i , ']' ,
           '[pw:', parent.genome , ']' , 
           '[p:' , parent.fitness , ']' ,
           '[c:' , child.fitness , ']' ) 
    # If the child is better than the parent replace the parent with the child.
    if ( child.fitness > parent.fitness ):
        parent = child
        parent.Evaluate( False )
        # Pickle the final/best result.
        f = open( 'robot.p' , 'w' )
        pickle.dump( parent , f )
        f.close()
        


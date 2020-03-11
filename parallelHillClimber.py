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


parents = POPULATION( 10 )
parents.Evaluate(True)


for g in range( 1 , 201 ):
    children = copy.deepcopy( parents ) 
    children.Mutate()
    children.Evaluate(True)
    parents.ReplaceWith( children )
    print( '\n' , g , end=' ')
    parents.Print()

parents.Evaluate(False)




        


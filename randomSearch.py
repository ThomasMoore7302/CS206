import pyrosim
import random
import matplotlib
import matplotlib.pyplot as plt
from robot import ROBOT
from individual import INDIVIDUAL


for i in range( 0, 10 ):
    individual = INDIVIDUAL()
    individual.Evaluate()
    print( individual.fitness )

    

    


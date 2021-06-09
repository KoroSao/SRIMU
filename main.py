from numpy.core.numeric import count_nonzero
from functions import *
import numpy as np
import random
import matplotlib.pyplot as plt
import time
start_time = time.time()


#Number of samples of angle combinations for which we want to determine the recoverability rate
N_SAMPLES = 10000
N_REAL = 1000

for i in range(N_SAMPLES):

    #Generates a new set of angles (3 for each IMU)
    angles = genRandomAngles()
    # print(f"Angles : {angles}")

    #Counts how many of the values generated were not saturated (dps below 2000)
    n_not_saturated = 0

    for j in range(N_REAL):

        #Generates a new set of DPS
        dps = genRandomDPS()
        #Compute rotation matrix  
        IMU1dps = matrixProductRot(np.array((np.radians(angles[0][0]), np.radians(angles[0][1]), np.radians(angles[0][2]))), dps)
        IMU2dps = matrixProductRot(np.array((np.radians(angles[1][0]), np.radians(angles[1][1]), np.radians(angles[1][2]))), dps)
        IMU3dps = matrixProductRot(np.array((np.radians(angles[2][0]), np.radians(angles[2][1]), np.radians(angles[2][2]))), dps)
        # print("=======================================================")
        # print(f"DPS in BA   : {dps}")
        # print(f"DPS in IMU1 : {IMU1dps}")
        # print(f"DPS in IMU2 : {IMU2dps}")
        # print(f"DPS in IMU3 : {IMU3dps}")
        # print("========================================================\n")

        count_IMUS = 0
        if not isSaturated(dps): 
            count_IMUS += 1
        if not isSaturated(IMU1dps): 
            count_IMUS += 1
        if not isSaturated(IMU2dps): 
            count_IMUS += 1
        if not isSaturated(IMU3dps): 
            count_IMUS += 1

        if count_IMUS >= 2:
            n_not_saturated += 1
        
    RR = n_not_saturated * 100 / N_REAL
    print(f"Recovery Rate is of : {RR} %")


v = np.array((1,0,0))
v2 = [1,0,0]


print("--- %s seconds ---" % (time.time() - start_time))


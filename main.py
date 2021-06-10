from os import write
from numpy.core.numeric import count_nonzero
from functions import *
import numpy as np
import matplotlib.pyplot as plt
import time
from pathlib import Path
start_time = time.time()



#Number of samples of angle combinations for which we want to determine the recoverability rate
N_SAMPLES = 1000
N_REAL = 100
SHOW_DPS = False
DIR=  Path().absolute()
FILE = str(DIR) + "\main.csv"



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


        if(SHOW_DPS):
            print("=======================================================")
            print(f"DPS in BA   : {dps}")
            print(f"DPS in IMU1 : {IMU1dps}")
            print(f"DPS in IMU2 : {IMU2dps}")
            print(f"DPS in IMU3 : {IMU3dps}")
            print("========================================================\n")

        #Here we count the number of channels (from the 9 channels) that are no saturated (dps < 2000)
        not_saturated_channels = countUnsaturedChannels(IMU1dps,IMU2dps,IMU3dps)
        if not_saturated_channels >=3:
            n_not_saturated +=1
        
    RR = n_not_saturated * 100 / N_REAL
    print(f"Recovery Rate is of : {RR} %")

    #95% is the threshold for a recovery rate to be acceptable
    if RR >= 95:
        anglestoprint = str(RR) + ',' + str(angles[0][0]) + ',' + str(angles[0][1]) + ',' + str(angles[0][2]) + ',' \
        + str(angles[1][0]) + ',' + str(angles[1][1]) + ',' + str(angles[1][2]) + ',' \
        + str(angles[2][0]) + ',' + str(angles[2][1]) + ',' + str(angles[2][2])
        
        writeToCSV(anglestoprint, FILE)



v = np.array((1,0,0))
v2 = [1,0,0]


print("--- %s seconds ---" % (time.time() - start_time))


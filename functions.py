import numpy as np
import random
import matplotlib.pyplot as plt
import time

UNIFORM_LOW = -4000
UNIFORM_HIGH = 4000

def genRandomAngles():
    tab = []
    for i in range(3):
        t = []
        for j in range(3):
            x = np.random.randint(0,360)
            t.append(x)
        tab.append(t)
    return tab

def genRandomDPS():
    #By definition we'll suppose M[0] = alpha, 1--> Beta, 2--> Gamma
    M = [np.random.randint(UNIFORM_LOW, UNIFORM_HIGH),np.random.randint(UNIFORM_LOW, UNIFORM_HIGH),np.random.randint(UNIFORM_LOW, UNIFORM_HIGH)]
    return M

def matrixProductRot(m, v):
    #M is a list of the 3 rotation angles to apply
    #V is a list of the 3 components to rotate
    #Generates the rotation matrix from the angles held in m table
    r = np.array(( (np.cos(m[0])*np.cos(m[1]), np.cos(m[0])*np.sin(m[1])*np.sin(m[2]) - np.sin(m[0])*np.cos(m[2]), np.cos(m[0])*np.sin(m[1])*np.cos(m[2]) + np.sin(m[0])*np.sin(m[2])),
                (np.sin(m[0])*np.cos(m[1]), np.sin(m[0])*np.sin(m[1])*np.sin(m[2]) - np.cos(m[0])*np.cos(m[2]), np.sin(m[0])*np.sin(m[1])*np.cos(m[2]) - np.cos(m[0])*np.sin(m[2])),
                (-np.sin(m[1]),  np.cos(m[1])*np.sin(m[2]), np.cos(m[1])*np.cos(m[2]) ) ))

    v_prime = np.around(r.dot(v), 3)
    return v_prime    


def countUnsaturedChannels(DPS1,DPS2,DPS3):
    n = 0
    for i in range(3):
        if abs(DPS1[i]) <= 2000:
            n += 1
    for i in range(3):
        if abs(DPS2[i]) <= 2000:
            n += 1
    for i in range(3):
        if abs(DPS3[i]) <= 2000:
            n += 1
    return n


def exist(filename):
    try:
        f = open(filename, 'r')
        f.close()
        return True
    except:
        return False

def writeToCSV(input_data, output_file):
    if exist(output_file):
        f = open(output_file,"a", encoding="utf-8")
        f.write(input_data + "\n")
        f.close()
    else:
        print("Specified file does not exist !")
import numpy as np
import random
import matplotlib.pyplot as plt
import time

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
    M = [np.random.randint(-4000.0, 4000.0),np.random.randint(-4000.0, 4000.0),np.random.randint(-4000.0, 4000.0)]
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


def isSaturated(v):
    #Returns True if the dps vector has one component greater than 2000
    for i in range(3):
       if v[i] >= 2000:
           return True
    return False
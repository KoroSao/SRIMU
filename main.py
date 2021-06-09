import numpy as np
import random
import matplotlib.pyplot as plt
import time
start_time = time.time()

#Let's generate 3 angles from a uniform law on the following range [-4000,4000]

def genRandomDPS():
    #By definition we'll suppose M[0] = alpha, 1--> Beta, 2--> Gamma
    M = [np.random.randint(-4000.0, 4000.0),np.random.randint(-4000.0, 4000.0),np.random.randint(-4000.0, 4000.0)]
    return M

m = [-np.radians(90),0,0]
v = np.array((1,0,0))

def matrixProductRot(m, v):
    #Generates the rotation matrix from the angles held in m table
    r = np.array(( (np.cos(m[0])*np.cos(m[1]), np.cos(m[0])*np.sin(m[1])*np.sin(m[2]) - np.sin(m[0])*np.cos(m[2]), np.cos(m[0])*np.sin(m[1])*np.cos(m[2]) + np.sin(m[0])*np.sin(m[2])),
                (np.sin(m[0])*np.cos(m[1]), np.sin(m[0])*np.sin(m[1])*np.sin(m[2]) - np.cos(m[0])*np.cos(m[2]), np.sin(m[0])*np.sin(m[1])*np.cos(m[2]) - np.cos(m[0])*np.sin(m[2])),
                (-np.sin(m[1]),  np.cos(m[1])*np.sin(m[2]), np.cos(m[1])*np.cos(m[2]) ) ))

    v_prime = np.around(r.dot(v), 3)
    return v_prime


def isSaturated(v):
    #Returns True if the dps vector has one component greater thean 2000
    print(v)
    for i in range(3):
       if v[i] >= 2000:
           return True
    return False


# m = matrixProductRot(m, v)

# for a in range(1):
#     for b in range(360):
#         for g in range(360):
#             angles = [a,b,g]
#             print(angles)

print(isSaturated(v))


print("--- %s seconds ---" % (time.time() - start_time))

# print(m)


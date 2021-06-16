from functions import *
import numpy as np
import plotly.express as px

N_REAL = 1000
N_ECH = 1000

angles = [[227,77,227],[140,271,52],[40,338,132]]

x = []
y = []
for i in range(N_ECH):
    y.append(i+1)

for i in range (N_ECH):
    n_not_saturated = 0
    for j in range(N_REAL):
        dps = genRandomDPS()

        IMU1dps = matrixProductRot(np.array((np.radians(angles[0][0]), np.radians(angles[0][1]), np.radians(angles[0][2]))), dps)
        IMU2dps = matrixProductRot(np.array((np.radians(angles[1][0]), np.radians(angles[1][1]), np.radians(angles[1][2]))), dps)
        IMU3dps = matrixProductRot(np.array((np.radians(angles[2][0]), np.radians(angles[2][1]), np.radians(angles[2][2]))), dps)

        not_saturated_channels = countUnsaturedChannels(IMU1dps,IMU2dps,IMU3dps)
        if not_saturated_channels >=3:
            n_not_saturated +=1
            
    RR = n_not_saturated * 100 / N_REAL
    print(f"Recovery Rate is of : {RR} %")
    x.append(RR)

df = y
fig = px.histogram(df, x)
fig.show()
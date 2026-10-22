# Daniel Nieves NC=1343
import numpy as np

D1343=np.array([10,20,30,40,50,])
print(D1343)
print(D1343[0])
print(D1343[3])
print(D1343[-1])
print(D1343[-2])
print("--------------------------")
D1343=np.array([
    [10],[20],[30],
    [40],[50],[60]
])
print(D1343)
print(D1343.shape)
print(D1343)
print(D1343[0, 0])
print(D1343[1, 0])
print(D1343[-1, -1])
print(D1343[-2, -1])
print("--------------------------")
D1343=np.array([
    #0 -2
    [
    [10],[20],[30],
    [40],[50],[60]
],
    #1 -1
    [
     [70],[80],[90],
     [100],[110],[120]
     ]
])
print(D1343)
print(D1343[0, 0, 0])
print(D1343[1, 1, 0])
print(D1343[-1, -1, -1])

print("Daniel Nieves NC=1343")
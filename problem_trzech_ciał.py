import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.integrate import solve_ivp

#ustalamy masy początkowe - tu zrobimy suwak
m1=1
m2=2
m3=3

#pozycje początkowe - tu też możemy dać suwak
r1 = np.array([1.0, 1.0, 1.0])
r2 = np.array([0.0, 0.0, 0.0])
r3 = np.array([2.0, 2.0, 2.0])

#prędkości początkowe - nie wiem jak z suwakiem, trzeba pomyśleć
v1 = np.array([0.0, 0.5, 0.0])
v2 = np.array([1.0, 0.0, 0.1])
v3 = np.array([0.1, 0.1, 0.0])
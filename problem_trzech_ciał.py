import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


#ustalamy masy początkowe - tu zrobimy suwak
m1=1
m2=2
m3=3

q1=1
q2=1
q3=1

#pozycje początkowe - tu też możemy dać suwak
r1_0 = np.array([1.0, 1.0, 1.0])
r2_0 = np.array([0.0, 0.0, 0.0])
r3_0 = np.array([2.0, 2.0, 2.0])

#prędkości początkowe - nie wiem jak z suwakiem, trzeba pomyśleć, bo v=dx/dt
v1_0 = np.array([0.0, 0.5, 0.0])
v2_0 = np.array([1.0, 0.0, 0.1])
v3_0 = np.array([0.1, 0.1, 0.0])


#TO DO: NA SAM KONIEC UWAŻAĆ NA DZIELENIE PRZEZ 0!!!
def rownanie_rozniczkowe(t,y,m1,m2,m3, q1, q2, q3):
    r1 = y[0:3]
    r2 = y[3:6]
    r3 = y[6:9]
    v1 = y[9:12]
    v2 = y[12:15]
    v3 = y[15:18]

    #musimy obliczyć długość wektora
    r21_dl = np.linalg.norm(r2-r1)
    r31_dl = np.linalg.norm(r3-r1)
    r12_dl = r21_dl
    r32_dl = np.linalg.norm(r3-r2)
    r13_dl = r31_dl
    r23_dl = r32_dl

    x1_dtdt = (m2+q2*q1/m1)*(r2-r1)/r21_dl**3 + (m3+q3*q1/m1)*(r3-r1)/r31_dl**3
    x2_dtdt = (m1+q1*q2/m2)*(r1-r2)/r12_dl**3 + (m3+q3*q2/m2)*(r3-r2)/r32_dl**3
    x3_dtdt = (m1+q1*q3/m3)*(r1-r3)/r13_dl**3 + (m2+q2*q3/m3)*(r2-r3)/r23_dl**3

    x1_dt = v1
    x2_dt = v2
    x3_dt = v3

    return np.concatenate([x1_dt, x2_dt, x3_dt, x1_dtdt, x2_dtdt, x3_dtdt]) #bo do solve_ivp potrzeba wektora

warunki_poczatkowe = np.concatenate([r1_0, r2_0, r3_0, v1_0, v2_0, v3_0])

rozwiazanie = solve_ivp(
    fun = rownanie_rozniczkowe,
    t_span = (0,10),
    y0 = warunki_poczatkowe,
    t_eval= np.linspace(0,10,2000),
    args = (m1,m2,m3, q1, q2, q3)
)
r1_x=rozwiazanie.y[0]
r1_y=rozwiazanie.y[1]
r1_z=rozwiazanie.y[2]
r2_x=rozwiazanie.y[3]
r2_y=rozwiazanie.y[4]
r2_z=rozwiazanie.y[5]
r3_x=rozwiazanie.y[6]
r3_y=rozwiazanie.y[7]
r3_z=rozwiazanie.y[8]
r1_vx=rozwiazanie.y[9]
r1_vy=rozwiazanie.y[10]
r1_vz=rozwiazanie.y[11]
r2_vx=rozwiazanie.y[12]
r2_vy=rozwiazanie.y[13]
r2_vz=rozwiazanie.y[14]
r3_vx=rozwiazanie.y[15]
r3_vy=rozwiazanie.y[16]
r3_vz=rozwiazanie.y[17]

#print(r1_x)
#print(rozwiazanie)




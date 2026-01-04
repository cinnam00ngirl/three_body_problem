import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from problem_trzech_ciał import odpal_symulacje



okno_start, osie_start = plt.subplots()
#plt.subplots_adjust(left=0.25, bottom=0.5)
#osie_start.axis("off")

#MASY
os_m1 = plt.axes([0.25, 0.4, 0.65, 0.03])
os_m2 = plt.axes([0.25, 0.35, 0.65, 0.03])
os_m3 = plt.axes([0.25, 0.30, 0.65, 0.03])

s_m1 = Slider(os_m1, "m1", 0.1, 10, valinit=1)
s_m2 = Slider(os_m2, "m2", 0.1, 10, valinit=2)
s_m3 = Slider(os_m3, "m3", 0.1, 10, valinit=3)

#ŁADUNKI
ax_q1 = plt.axes([0.25, 0.22, 0.65, 0.03])
ax_q2 = plt.axes([0.25, 0.17, 0.65, 0.03])
ax_q3 = plt.axes([0.25, 0.12, 0.65, 0.03])
s_q1 = Slider(ax_q1, "q1", -5, 5, valinit=1)
s_q2 = Slider(ax_q2, "q2", -5, 5, valinit=1)
s_q3 = Slider(ax_q3, "q3", -5, 5, valinit=1)

#START
ramka_przycisk = plt.axes([0.4, 0.02, 0.2, 0.05])
przycisk = Button(ramka_przycisk, "START")

def start(event):
    plt.close(okno_start)
    m1 = s_m1.val
    m2 = s_m2.val
    m3 = s_m3.val
    q1 = s_q1.val
    q2 = s_q2.val
    q3 = s_q3.val

    odpal_symulacje(m1, m2, m3, q1, q2, q3)

przycisk.on_clicked(start)
plt.show()

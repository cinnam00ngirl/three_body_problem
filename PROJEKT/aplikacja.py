import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from problem_trzech_ciał import odpal_symulacje
import multiprocessing

def main():

    okno_start, osie_start = plt.subplots()
    #plt.subplots_adjust(left=0.25, bottom=0.5)
    okno_start.patch.set_facecolor('pink')
    #osie_start.axis("off")

    #MASY
    os_m1 = plt.axes([0.25, 0.8, 0.65, 0.03])
    os_m2 = plt.axes([0.25, 0.75, 0.65, 0.03])
    os_m3 = plt.axes([0.25, 0.70, 0.65, 0.03])

    s_m1 = Slider(os_m1, "masa 1", 0.1, 10, valinit=1)
    s_m2 = Slider(os_m2, "masa 2", 0.1, 10, valinit=2)
    s_m3 = Slider(os_m3, "masa 3", 0.1, 10, valinit=3)

    #ŁADUNKI
    ax_q1 = plt.axes([0.25, 0.65, 0.65, 0.03])
    ax_q2 = plt.axes([0.25, 0.6, 0.65, 0.03])
    ax_q3 = plt.axes([0.25, 0.55, 0.65, 0.03])

    s_q1 = Slider(ax_q1, "ładunek 1", -5, 5, valinit=1)
    s_q2 = Slider(ax_q2, "ładunek 2", -5, 5, valinit=1)
    s_q3 = Slider(ax_q3, "ładunek 3", -5, 5, valinit=1)


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

        p = multiprocessing.Process(target=odpal_symulacje, args=(m1, m2, m3, q1, q2, q3))
        p.start()

    przycisk.on_clicked(start)
    plt.show()

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")  # wymagane na Windows/macOS
    main()

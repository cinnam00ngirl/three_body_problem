import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, CheckButtons
import multiprocessing
from problem_trzech_ciał import odpal_symulacje

def start_okna():
    while True:  # pętla, żeby moc wracać do okna startowego
        okno_start, osie_start = plt.subplots()
        okno_start.patch.set_facecolor('pink')
        osie_start.axis("off")
        plt.title("Problem 3 ciał\n Ustawienia:")

        # MASY
        os_m1 = plt.axes([0.25, 0.80, 0.65, 0.03])
        os_m2 = plt.axes([0.25, 0.75, 0.65, 0.03])
        os_m3 = plt.axes([0.25, 0.70, 0.65, 0.03])
        s_m1 = Slider(os_m1, "masa 1", 0.1, 10, valinit=1)
        s_m2 = Slider(os_m2, "masa 2", 0.1, 10, valinit=2)
        s_m3 = Slider(os_m3, "masa 3", 0.1, 10, valinit=3)

        # ŁADUNKI
        ax_q1 = plt.axes([0.25, 0.65, 0.65, 0.03])
        ax_q2 = plt.axes([0.25, 0.60, 0.65, 0.03])
        ax_q3 = plt.axes([0.25, 0.55, 0.65, 0.03])
        s_q1 = Slider(ax_q1, "ładunek 1", -5, 5, valinit=1)
        s_q2 = Slider(ax_q2, "ładunek 2", -5, 5, valinit=1)
        s_q3 = Slider(ax_q3, "ładunek 3", -5, 5, valinit=1)


        ax_check = plt.axes([0.05, 0.45, 0.2, 0.05])
        check = CheckButtons(ax_check, ["Czarne tło"], [False])
        czarne_tlo_flag = [False]

        def zmien_tlo(label):
            czarne_tlo_flag[0] = not czarne_tlo_flag[0]

        check.on_clicked(zmien_tlo)

        # START
        ramka_przycisk = plt.axes([0.4, 0.02, 0.2, 0.05])
        przycisk = Button(ramka_przycisk, "START")

        # flaga do kontrolowania wyjścia
        start_pressed = multiprocessing.Event()

        def start(event):
            start_pressed.set()
            plt.close(okno_start)  # zamykamy tylko okno startowe

        przycisk.on_clicked(start)
        plt.show()

        if not start_pressed.is_set():
            break

        m1 = s_m1.val
        m2 = s_m2.val
        m3 = s_m3.val
        q1 = s_q1.val
        q2 = s_q2.val
        q3 = s_q3.val
        tlo = czarne_tlo_flag[0]


        p = multiprocessing.Process(target=odpal_symulacje, args=(m1, m2, m3, q1, q2, q3, tlo))
        p.start()
        p.join()  # czekamy aż animacja się zakończy i wracamy do pętli


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")  # cos tam z windowsem
    start_okna()
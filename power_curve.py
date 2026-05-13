from load_data import load_data
from sort import bubble_sort
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":

    data = load_data('activity.csv')
    power_W = data['PowerOriginal']

    sorted_power_W = bubble_sort(power_W)

    time_array = list(range(0, 1804, 1))

    plt.plot(time_array, sorted_power_W[::-1])

    plt.xlabel("Time")
    plt.ylabel("Power [W]")
    plt.title("Power Curve")

    # figures Ordner erstellen
    os.makedirs("figures", exist_ok=True)

    # speichern
    plt.savefig("figures/power_curve.png")

    # anzeigen
    plt.show()
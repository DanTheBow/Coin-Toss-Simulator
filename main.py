import numpy as np


def coin_toss(probability):
    # Binomialverteilung ausführen (gibt 0 oder 1 zurück)
    result = np.random.binomial(1, probability)
    return result


p = float(input("Gebe die Wahrscheinlichkeit ein: "))
n = int(input("Gebe die Anzahl der Würfe ein: "))

# Array für Würfe initiieren
all_dices = np.arange(n)

for i in range(0, n):
    all_dices[i] = coin_toss(p)
    i += 1

print("")
print("Wahrscheinlichkeit wurde auf " + str(p) + " gesetzt.")
print("Es wurde " + str(n) + " mal geworfen.")
print("Zahl = 0, Kopf = 1: ", all_dices)

# Kopf und Zahl zusammenzählen und anzeigen
print("Anzahl - Zahl: ", np.count_nonzero(all_dices == 0))
print("Anzahl - Kopf: ", np.count_nonzero(all_dices == 1))

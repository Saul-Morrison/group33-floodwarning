import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from floodsystem.Analysis import polyfit


def plot_risk(stations):
    Low = 0
    Moderate = 0
    High = 0 
    Severe = 0
    for station in stations:
        if station.risk == 'Low':
            Low += 1
        elif station.risk == 'Moderate':
            Moderate += 1
        elif station.risk == 'High':
            High += 1
        elif station.risk == 'Severe':
            Severe += 1
    x_pos = np.arange(4)
    Risk = ('Low', 'Moderate', 'High', 'Severe')
    Values = (Low, Moderate, High, Severe)
    plt.bar(x_pos, Values, align='center')
    plt.xticks(x_pos, Risk, rotation=45)

    plt.xlabel('Risk')
    plt.ylabel('Number of Stations')

    plt.show()


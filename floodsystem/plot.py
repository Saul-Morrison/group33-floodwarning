
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from floodsystem.Analysis import polyfit

def plot_water_levels(station, dates, levels):

    t = dates

    plt.plot(t, levels)

    plt.xlabel('dates')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()

    plt.show()


def plot_water_with_levels(station, dates, levels, p):
    
    x = matplotlib.dates.date2num(dates)
    #create polynmial and shift in dates
    poly, d0 = polyfit(dates, levels, p)

    plt.plot(dates, levels, '.')
    plt.title(station.name)
    plt.xticks(rotation=45)

    # Plot polynomial fit at 30 points along interval
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]))

    #Display plot
    plt.show()

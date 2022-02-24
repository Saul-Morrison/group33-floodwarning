import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    poly_coeff = np.polyfit(x - x[0], levels, p)

    
    poly = np.poly1d(poly_coeff)

    d0 = x[0]

    return poly, d0

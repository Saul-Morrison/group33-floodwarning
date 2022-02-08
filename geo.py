# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""


from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine
from floodsystem.stationdata import build_station_list
from Task1A import run
import numpy as np




stations = build_station_list()

#adds the distance from a coordinate q to the class for every station



def orderfromcoord(stations, q):
    stations = build_station_list()
    names = []
    distance = []
    for station in stations:
        names.append(station.name)
        distance.append(haversine(station.coord, q))

    tuple = list(zip(names, distance))
    tuple = sorted_by_key(tuple, 1)
    return(tuple)

def stations_within_range(values, q, r):
    temp = True
    i = 0
    nearstations = []
    while temp == True:
        if values[i][1] > r:
            temp = False
        else:
            nearstations.append(values[i])
        i += 1
    return nearstations



        






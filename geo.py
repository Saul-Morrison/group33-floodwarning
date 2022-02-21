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


def stations_with_river(stations):
    stationRivers = set()
    for i in range(len(stations)):
        if stations[i].river != None:
          stationRivers.add(stations[i].river)
    return stationRivers
def stations_by_river(stations):
    Riverstations = {}
    for i in range(len(stations)): # go through each station and assign variable to river name and`` station name
        river_name = stations[i].river
        station_name = [stations[i].name] 
        if river_name in Riverstations:
             Riverstations[stations[i].river].append(station_name)
        else:
          a = {river_name:station_name}
          Riverstations.update(a)
     
    return Riverstations

def rivers_by_station_number(stations, N):
    Top_list=[]
    River_dict = stations_by_river(stations)
    
    station_number = []
    river_key = list(River_dict.keys())
    for river in River_dict:
        station_number.append(len(River_dict[river]))
    
    bob = list(zip(river_key,station_number))
    bob.sort(key=lambda x:x[1])    
    while bob[len(bob)-N][1] == bob[len(bob)-(N+1)][1]:
        N = N+1
    
    Top_list = bob[len(bob)-N:len(bob)]

    return Top_list

        

        

    
        






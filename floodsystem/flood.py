from floodsystem.station import MonitoringStation
from floodsystem.utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    return_list = []
    for station in stations:
        station_level_tuple = []
        relative_level = MonitoringStation.relative_water_level(station)
        if relative_level !=None and relative_level > tol:
           station_level_tuple.append(station.name)
           station_level_tuple.append(relative_level)
           return_list.append(station_level_tuple)
     
    return sorted_by_key(return_list, 1 , reverse=True)
    #return return_list
    
 
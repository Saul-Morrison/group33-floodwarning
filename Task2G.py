from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation
from Test_2G import plot_risk

stations = build_station_list()

update_water_levels(stations)

#creating tuple of stations with highest relative water levels
tuple0 = stations_level_over_threshold(stations, 1.0)


for station in stations:
    
    member = [station.name, station.relative_level]
    if member in tuple0:
        station.risk = 'High'
    else:
        station.risk = 'Moderate'


tuple1 = stations_level_over_threshold(stations, 1.2)



for station in stations:
    member = [station.name, station.relative_level]
    if member in tuple1:
        station.risk = 'Severe'
        print(station.name)

tuple2 = stations_level_over_threshold(stations, 0.8)


for station in stations:
    
    member = [station.name, station.relative_level]
    if member not in tuple2:
        station.risk = 'Low'



for station in stations:
    if station.risk == 'High':

        print(station.name, ':  ', station.risk, '\n')

plot_risk(stations)
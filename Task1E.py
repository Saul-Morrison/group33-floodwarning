from distutils.command.build import build
from geo import stations_with_river
from geo import stations_by_river 
from floodsystem.stationdata import build_station_list
from geo import rivers_by_station_number
stations = build_station_list()
N = 11
station_number = rivers_by_station_number(stations, N)

print (station_number)
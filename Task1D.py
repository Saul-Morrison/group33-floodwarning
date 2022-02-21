from distutils.command.build import build
from geo import stations_with_river
from geo import stations_by_river 
from floodsystem.stationdata import build_station_list


stations = build_station_list()
print (stations[0])

output = stations_with_river(stations)
print(len(output))
#print(output[0:10])

river_dictionary = stations_by_river(stations)
print(river_dictionary["River Aire"])
print(river_dictionary["River Cam"])
print(river_dictionary["River Thames"])


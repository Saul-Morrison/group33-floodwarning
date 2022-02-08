from geo import stations_within_range
from geo import orderfromcoord
from floodsystem.stationdata import build_station_list

stations = build_station_list()



q1 = float(input('What is the longitude you would like to input?'))
q2 = float(input('What is the lattitude you would like to input?'))
q = (q1, q2)

r = float(input('What is the maximum distance from the coordinate a station can be?'))

values =  orderfromcoord(stations, q)

valid_stations = stations_within_range(values, q, r)

valid_stations.sort()

print('The stations within the range are:')

for i in range(len(valid_stations)):
    print(valid_stations[i][0])
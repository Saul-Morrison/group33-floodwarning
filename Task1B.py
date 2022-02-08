from geo import orderfromcoord
from haversine import haversine
from floodsystem.stationdata import build_station_list



#finds distance between two coordinates
def distances(p, q):
    distance = haversine(p, q)

    return(distance)


stations = build_station_list()

#adds the distance from a coordinate q to the class for every station

q1 = float(input('What is the longitude you would like to input?'))
q2 = float(input('What is the lattitude you would like to input?'))
q = (q1, q2)


names = []
distance = []

values = orderfromcoord(stations, q)

for i in range(10):
    print('Name of station near:', values[i][0])
    print('     distance from coordinate:', values[i][1])

print('\n')
for i in range(10):
    print('Name of station far:', values[len(values) - i - 1][0])
    print('     distance from coordinate:', values[len(values) - i - 1][1])




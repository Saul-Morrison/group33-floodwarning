from geo import orderfromcoord
from floodsystem.stationdata import build_station_list
from haversine import haversine

def test_orderfromcoord():
    stations = build_station_list()
    n = 100000
    q = (0.0, 0.0)
    for station in stations:
        if haversine(station.coord, q) < n:
            n = haversine(station.coord, q)
    ordered_stations = orderfromcoord(stations)
    print(ordered_stations)
    if ordered_stations[0][1] ==  n:
        return True
    else:
        return False

test_orderfromcoord()

        
    
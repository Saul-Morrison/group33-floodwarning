from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def check_list_length():
    stations = build_station_list
    update_water_levels(stations)
    Station_list = [stations_level_over_threshold(stations,10 )]
    print(Station_list)
    assert len(Station_list) == 10

print (check_list_length)
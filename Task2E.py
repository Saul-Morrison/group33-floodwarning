from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.utils import sorted_by_key

stations = build_station_list()

station_name = "Cam"


update_water_levels(stations)

station_cam = None

names = []
levels = []

for station in stations:
    names.append(station.name)
    levels.append(station.latest_level)


tuple = list(zip(names, levels))


for i in range(len(tuple)):
    if tuple[i][1] == None:
        print(tuple[i])
        tuple[i] = ('', 0)
        print(tuple[i])

tuple = sorted_by_key(tuple, 1)


for i in range(5):
    for station in stations:

        if tuple[i][0] == station.name:
            temp_station = station
            dates, levels = fetch_measure_levels(temp_station.measure_id, timedelta(days = 10))
            plot_water_levels(temp_station, dates, levels)
        







    



#current_water = {}

#dt = 1
#dates, level = fetch_measure_levels(station_cam.measure_id, dt = timedelta(days = dt))



#for station in stations:
#    dt = 1
#    dates, level = fetch_measure_levels(station.measure_id, dt = timedelta(days = dt))
#    print(current_water)
#    current_water[station.name] = level
    
    
#print(level)


#dt = 10
#dates, levels = fetch_measure_levels(station_cam.measure_id, dt = timedelta(days = dt))




#plot_water_levels(station_cam, dates, level)




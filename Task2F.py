from floodsystem.stationdata import build_station_list
from datetime import timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_with_levels
from floodsystem.utils import sort_by_current_levels


stations = build_station_list()

tuple = sort_by_current_levels(stations)

temp_station = None


for station in stations:
    for i in range(5):
        if tuple[i][0] == station.name:
        
            temp_station = station
            dates, levels = fetch_measure_levels(temp_station.measure_id, timedelta(days = 2))
            plot_water_with_levels(temp_station, dates, levels, 4)

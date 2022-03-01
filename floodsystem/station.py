# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town,):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town
        
        self.relative_level = None

        self.latest_level = None
        
        self.risk = None

    def typical_range_consistent(self):
        if self.typical_range is None:
            return False
        elif self.typical_range[0] > self.typical_range[1]:
            return False

        else:
            return True

    def relative_water_level(self):
        if self.typical_range != None:
            Typical_low = self.typical_range[0]
            Typical_high = self.typical_range[1]

            if self.latest_level != None:
                self.relative_level = (self.latest_level - Typical_low)/ Typical_high
            else:
                self.relative_level = None
        return self.relative_level    


    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        d += "   relative level: {}".format(self.relative_level)
        return d


    
        
        
    
    
    
    
def inconsistent_typical_range_stations(stations):
    Inconsistent_stations = []
    for MonitoringStation in stations:
        r = MonitoringStation.typical_range
        n = MonitoringStation.typical_range_consistent()
        if n == False:
            Inconsistent_stations.append(MonitoringStation.name)
            
    return Inconsistent_stations
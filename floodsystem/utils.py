# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains utility functions.

"""



def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)



from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels

def sort_by_current_levels(stations):

  update_water_levels(stations)

  names = []
  levels = []

  for station in stations:
      names.append(station.name)
      levels.append(station.latest_level)


  tuple = list(zip(names, levels))


  for i in range(len(tuple)):
      if tuple[i][1] == None:
          tuple[i] = ('', 0)

  tuple = sorted_by_key(tuple, 1)

  return(tuple)
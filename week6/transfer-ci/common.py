# coding:utf-8

import math
import sys
import tokyo

def adjacent_list(filename):
    stations = read_data()
    
    def is_in_adjacent(adj, current):
        result = -1
        for i in range(len(adj)):
            if current[0] == adj[i][0]:
                result = i
        return result
    
    adjacent = []
    for i in range(len(stations)-1):
        current_station = stations[i]
        next_station = stations[i+1]
        current_station_is_in = is_in_adjacent(adjacent, current_station)
        if current_station_is_in >= 0 :
            adjacent[current_station_is_in][1].append(next_station)
        else:
            if current_station[1] == next_station[1]:
                adjacent.append((current_station[0], [next_station]))
    for item in adjacent:
        print(item)
    return adjacent


def read_data():
    stations = []
    for item in tokyo.data:
        # print(item)
        name = item['Name']
        lst = item['Stations']
        for station in lst:
            stations.append((station, name))
    return stations

if __name__ == '__main__':
    lst = read_data()
    # print(lst)
    adjacent_list(lst)


    

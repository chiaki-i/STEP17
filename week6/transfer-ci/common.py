# coding:utf-8

import tokyo       

def result(path):
    new_start = (' ', ' ')
    if len(path) > 1:
        start = path.pop(0)
        if start[1] is None:
            new_start = (start[0], path[0][1])
    path.insert(0, new_start)
    return path

def bf_search(start, goal):
    adjacent = adjacent_list(read_data())
    
    def already_visited(path, current):
        flag = False
        for item in path:
            if item[0] == current[0]:
                flag = True
        return flag
    
    queue = [[(start, None)]]
    while queue:
        path = queue.pop(0)
        last = -1
        current_station = path[last]
        current_station_number = is_in_adjacent(adjacent, current_station)
        for x in adjacent[current_station_number][1]:
            if not already_visited(path, x):
                new_path = path[:]
                new_path.append(x)
                # print('newpath', new_path)
                if new_path[-1][0] == goal:
                    print('found!', new_path)
                    return new_path
                queue.append(new_path)
    # for item in queue:
    #     print(item)
    return queue[0]

def is_in_adjacent(adj, current):
        result = -1
        for i in range(len(adj)):
            if current[0] == adj[i][0][0]:
                result = i
        return result

def adjacent_list(filename):
    stations = read_data()
    stations_reversed = stations[::-1]
    
    def insert(stations, result):
        for i in range(len(stations)-1):
            current_station = stations[i]
            next_station = stations[i+1]
            current_station_is_in = is_in_adjacent(adjacent, current_station)
            if current_station_is_in >= 0 :
                if current_station[1] == next_station[1]:
                    adjacent[current_station_is_in][1].append(next_station)
            else:
                if current_station[1] == next_station[1]:
                    adjacent.append(((current_station[0], None), [next_station]))
        return result
    adjacent = []
    add_upward = insert(stations, adjacent)
    add_downward = insert(stations_reversed, add_upward)
    adjacent = add_downward
    # for item in adjacent:
    #     print(item)
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
    adj = adjacent_list(lst)

    bf_search('品川', '五反田')


    

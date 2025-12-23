# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/23 13:47:55 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/23 15:33:00 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 09 – Advent of Code 2015

from collections import defaultdict

def parser(fileName):
    city_map = defaultdict(list)
    with open(fileName) as f:
        data = f.read().strip().splitlines()
        for line in data:
            cities, distance = line.split('=')
            cityA, cityB = cities.strip().split('to')
            city_map[cityA.strip()].append((cityB.strip(), int(distance)))
            city_map[cityB.strip()].append((cityA.strip(), int(distance)))
    return city_map

def shortest_path_longest(city_map):
    paths = set()
    for start in city_map:
        stack = [(start, [start], {start}, 0)]
        while stack:
            curr, path, visited, total_dist = stack.pop()

            if len(path) == len(city_map):
                paths.add(total_dist)
                continue
            
            for city, dist in city_map[curr]:
                if city not in path:
                    stack.append((city, path + [city], visited | {city}, total_dist + dist))
                    
    return min(paths), max(paths)


def main():
    city_map = parser("input.txt")
    short_path, long_path = shortest_path_longest(city_map)
    print("Day 09 solution for 2015:", short_path, long_path)

if __name__ == "__main__":
    main()

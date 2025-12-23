# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/13 11:37:39 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/13 16:06:09 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 12 – Advent of Code 2021

from collections import defaultdict

def parser(fileName):
    cave_map = defaultdict(list)
    with open(fileName) as f:
        data = f.read().strip().splitlines()
        for line in data:
            start, end = line.split('-')
            cave_map[start].append(end)
            cave_map[end].append(start)
    return cave_map

def traverse(cave_map, curr='start', visited=None, allowed=1):
    if visited is None:
        visited = set()
    if curr == 'end':
        return 1
    total = 0
    for direction in cave_map[curr]:
        if direction != 'start':
            if direction.islower():
                if direction not in visited:
                    total += traverse(cave_map, direction, visited | {direction}, allowed)
                elif allowed:
                    total += traverse(cave_map, direction, visited | {direction}, 0)
            else:
                total += traverse(cave_map, direction, visited, allowed)
    return total

def main():
    cave_map = parser("input.txt")
    
    print("Day 12 solution for 2021:", traverse(cave_map))

if __name__ == "__main__":
    main()

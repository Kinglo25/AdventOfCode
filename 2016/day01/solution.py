# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/29 22:47:55 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/30 09:54:24 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 01 – Advent of Code 2016

from collections import deque
import copy

def parser(file_name):
    with open(file_name) as f:
        return deque([(e.strip()[0], int(e.strip()[1:])) for e in f.read().strip().split(',')])
    
def gps(dir, twice=False):
    degree = 0
    pos = (0, 0)
    visited = set()
    while dir:
        d = dir.popleft()
        turn = 90 if d[0] == 'R' else -90
        degree = (degree + turn) % 360
        dist = d[1]
        if abs(degree) == 0:
            dx, dy = 1, 0
        elif abs(degree) == 90:
            dx, dy = 0, 1
        elif abs(degree) == 180:
            dx, dy = -1, 0
        elif abs(degree) == 270:
            dx, dy = 0, -1
        for step in range(1, dist + 1):
            new_x = pos[0] + dx * step
            new_y = pos[1] + dy * step
            if (new_x, new_y) in visited:
                return sum((abs(new_x), abs(new_y)))
            visited.add((new_x, new_y))
        pos = (pos[0] + dx * dist, pos[1] + dy * dist)
    return (sum(abs(n) for n in pos))

def main():
    directions = parser("input.txt")
    directions_cpy = copy.deepcopy(directions)
    print("Day 01 solution for 2016:", gps(directions))
    print("Day 01 solution for 2016:", gps(directions_cpy, True))

if __name__ == "__main__":
    main()

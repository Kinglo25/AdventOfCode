# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/15 22:10:20 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/18 18:46:09 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 15 – Advent of Code 2021

import numpy as np
import heapq

def parser(fileName):
    with open(fileName) as f:
        return [[int(n) for n in row] for row in f.read().strip().splitlines()]

def shortest_path(risk_map, len_x, len_y, x, y):
    cost = 0
    priority_queue = []
    heapq.heappush(priority_queue, (cost, x, y))
    distance = np.full_like(risk_map, 9999)
    while priority_queue:
        cost, x, y = heapq.heappop(priority_queue)
        for dx, dy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if 0 <= dx < len_x and 0 <= dy < len_y:
                new_cost = cost + risk_map[dx][dy]
                if new_cost < distance[dx][dy]:
                    distance[dx][dy] = new_cost
                    if dx == len_x - 1 and dy == len_y - 1:
                        return new_cost
                    heapq.heappush(priority_queue, (new_cost, dx, dy))
    return cost

def five_time_as_large(risk_map, len_x, len_y):
    m = -1
    real_risk_map = np.zeros((len_x * 5, len_y * 5))
    for i in range(len_x * 5):
        if i % len_x == 0:
            m += 1
        n = -1
        for j in range(len_y * 5):
            if j % len_y == 0:
                n += 1
            real_risk_map[i][j] = (risk_map[i % len_x][j % len_y] + n + m) % 9
            if real_risk_map[i][j] == 0:
                real_risk_map[i][j] = 9
    return real_risk_map


def main():
    risk_map = parser('input.txt')
    print(risk_map)
    risk_map = five_time_as_large(risk_map, len(risk_map), len(risk_map[0]))
    cost = shortest_path(risk_map, len(risk_map), len(risk_map[0]), 0, 0)
    print("Day 15 solution for 2021:", cost)

if __name__ == "__main__":
    main()

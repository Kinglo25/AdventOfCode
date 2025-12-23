# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/20 14:49:07 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/21 13:23:41 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 06 – Advent of Code 2015

from collections import defaultdict


def parser(fileName):
    instructions = defaultdict(list)
    with open(fileName) as f:
        data = f.read().strip().splitlines()
    return data

def light_switch(instructions):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in instructions:
        if line.startswith("turn on"):
            (x1, y1), (x2, y2) = [[int(n) for n in coord.split(',')] for coord in line[7:].split("through")]
            action = lambda x: x + 1
        elif line.startswith("turn off"):
            (x1, y1), (x2, y2) = [[int(n) for n in coord.split(',')] for coord in line[8:].split("through")]
            action = lambda x: x - 1 if x > 0 else x
        elif line.startswith("toggle"):
            (x1, y1), (x2, y2) = [[int(n) for n in coord.split(',')] for coord in line[7:].split("through")]
            action = lambda x: x + 2 
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] = action(grid[i][j])
    return sum(n for row in grid for n in row)

def main():
    instructions = parser("input.txt")
    count = light_switch(instructions)
    print("Day 06 solution for 2015:", count)

if __name__ == "__main__":
    main()

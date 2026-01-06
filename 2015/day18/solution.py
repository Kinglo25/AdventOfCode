# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 17:50:56 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/27 15:16:54 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 18 – Advent of Code 2015

def parser(file_name):
    with open(file_name) as f:
        return [[light for light in row] for row in f.read().strip().splitlines()]

def animate(grid):
    new_grid = [[light for light in row] for row in grid]
    len_x = len(grid)
    len_y = len(grid[0])
    for x in range(len_x):
        for y in range(len_y):
            count = 0
            if  x == 0 and y == 0 or\
                x == 0 and y == len_y - 1\
                or x == len_x - 1 and y == 0 or\
                x == len_x - 1 and y == len_y - 1:
                grid[x][y] = new_grid[x][y] = '#'
                continue
            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                if 0 <= x + dx < len_x and 0 <= y + dy < len_y:
                    if grid[x + dx][y + dy] == '#':
                        count += 1
            if grid[x][y] == '#' and count != 2 and count != 3:
                new_grid[x][y] = '.'
            elif grid[x][y] == '.' and count == 3:
                new_grid[x][y] = '#'
    return new_grid

def main():
    grid = parser("input.txt")
    steps = 100
    for _ in range(steps):
        grid = animate(grid)
    print("Day 18 solution for 2015:", sum(n == '#' for row in grid for n in row))

if __name__ == "__main__":
    main()

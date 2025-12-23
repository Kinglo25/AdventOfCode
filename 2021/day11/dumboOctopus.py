# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    dumboOctopus.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/08 11:20:29 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/12 21:23:01 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def flash(grid, x, y, len_x, len_y, flashes):
	if x < 0 or x >= len_x or y < 0 or y >= len_y or grid[x][y] == 0:
		return flashes
	grid[x][y] += 1
	if grid[x][y] >= 10:
		grid[x][y] = 0
		flashes += 1
		flashes = flash(grid, x+1, y+1, len_x, len_y, flashes)
		flashes = flash(grid, x+1, y, len_x, len_y, flashes)
		flashes = flash(grid, x+1, y-1, len_x, len_y, flashes)
		flashes = flash(grid, x-1, y+1, len_x, len_y, flashes)
		flashes = flash(grid, x-1, y, len_x, len_y, flashes)
		flashes = flash(grid, x-1, y-1, len_x, len_y, flashes)
		flashes = flash(grid, x, y+1, len_x, len_y, flashes)
		flashes = flash(grid, x, y-1, len_x, len_y, flashes)
	return flashes


def dumboOctopus(grid, len_x, len_y):
	flashes = 0
	for x in range(len_x):
		for y in range(len_y):
			grid[x][y] += 1
	for x in range(len_x):
		for y in range(len_y):
			if grid[x][y] == 10:
				flashes = flash(grid, x, y, len_x, len_y, flashes)
	return flashes

def main():
	with open('input.txt', 'r') as f:
		flashes = 0
		grid = f.read().split('\n')
		len_x = len(grid)
		len_y = len(grid[0])
		grid = [[int(n) for n in row] for row in grid]
		steps = 0
		while True:
			steps += 1
			flashes += dumboOctopus(grid, len_x, len_y)
			if all(n == 0 for row in grid for n in row):
				print(steps)
				return 0
			
main()
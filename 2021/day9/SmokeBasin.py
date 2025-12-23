# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SmokeBasin.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 11:04:40 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/12 16:15:07 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from math import prod

def parser(fileName):
	with open(fileName) as f:
		return [[int(n) for n in row] for row in f.read().strip().split('\n')]

def is_low_point(heightmap, x, y, len_col, len_row, point):
	if x - 1 >= 0 and heightmap[x-1][y] <= point:
		return False
	if x + 1 < len_col and heightmap[x+1][y] <= point:
		return False
	if y - 1 >= 0 and heightmap[x][y-1] <= point:
		return False
	if y + 1 < len_row and heightmap[x][y+1] <= point:
		return False
	return True

def calculate_bassins_sizes(heightmap, x, y, len_col, len_row, size):
	stack = [(x, y)]
	while stack:
		x, y = stack.pop()
		curr = heightmap[x][y]
		if curr == -1 or curr == 9:
			continue
		size += 1
		heightmap[x][y] = -1
		for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
			if 0 <= nx < len_col and 0 <= ny < len_row:
				if heightmap[nx][ny] != 9 and heightmap[nx][ny] != -1:
					stack.append((nx, ny))
	return size

def find_low_points(heightmap, len_col, len_row):
	bassins_sizes = []
	for x in range(len_col):
		for y in range(len_row):
			if is_low_point(heightmap, x, y, len_col, len_row, heightmap[x][y]):
				bassins_sizes.append(calculate_bassins_sizes(heightmap, x, y, len_col, len_row, 0))
	return prod(sorted(bassins_sizes)[-3:])

def main():
	heightmap = parser('input.txt')
	print(find_low_points(heightmap, len(heightmap), len(heightmap[0])))
main()
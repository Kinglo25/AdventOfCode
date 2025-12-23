# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HydrothermalVenture.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/09 18:46:33 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/09 22:52:19 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def parser(fileName):
	with open(fileName) as f:
		data = f.read().strip()
		return [[[int(n) for n in coord.split(',')] for coord in row.split('->')] for row in data.split('\n')]

def add_to_diagram(x1, y1, x2, y2, diagram):
	if x1 == x2:
		increment_y = (y1 - y2)//-abs(y1 - y2)
		while y1 != y2:
			diagram[y1][x1] += 1
			y1 += increment_y
	elif y1 == y2:
		increment_x = (x1 - x2)//-abs(x1 - x2)
		while x1 != x2:
			diagram[y1][x1] += 1
			x1 += increment_x
	else:
		increment_y = (y1 - y2)//-abs(y1 - y2)
		increment_x = (x1 - x2)//-abs(x1 - x2)
		while x1 != x2 or y2 != y1:
			diagram[y1][x1] += 1
			x1 += increment_x
			y1 += increment_y
	diagram[y1][x1] += 1

def count_overlapping_lines(diagram):
	count = 0
	for row in diagram:
		for n in row:
			if n >= 2:
				count += 1
	return count


def overlap(coordinates):
	diagram = [[0 for _ in range(1000)] for _ in range(1000)]
	for coord in coordinates:
		[x1, y1], [x2, y2] = coord
		add_to_diagram(x1, y1, x2, y2, diagram)
	return count_overlapping_lines(diagram)	
		
def main():
	coordinates = parser('input.txt')
	print(overlap(coordinates))

main()
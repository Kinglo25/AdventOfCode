# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    TheTreacheryOfWhales.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/10 16:50:18 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/10 18:03:27 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def parser(fileName):
	with open(fileName) as f:
		return [int(n) for n in f.read().strip().split(',')]

def calculate_fuel_part1(crab_positions):
	min_avg_dist = 100000
	least_cost_pos = 0
	for j in range(max(crab_positions)):
		avg_dist = sum(abs(crab_pos - j) for crab_pos in crab_positions) / len(crab_positions)
		if min_avg_dist > avg_dist:
			min_avg_dist, least_cost_pos = avg_dist, j
	return sum(abs(pos - least_cost_pos) for pos in crab_positions)
def calculate_fuel_part2(crab_positions):
	avg_dist = round(sum(crab_positions)/len(crab_positions))
	fuel = 0
	for i in range(len(crab_positions)):
		dx = -1 if avg_dist - crab_positions[i] < 0 else (1 if avg_dist - crab_positions[i] > 0 else 0)
		add = 1
		while crab_positions[i] != avg_dist:
			crab_positions[i] += dx
			fuel += add
			add += 1
	return fuel

def main():
	crab_positions = parser('input.txt')
	print(calculate_fuel_part1(crab_positions))
	print(calculate_fuel_part2(crab_positions))
	

main()
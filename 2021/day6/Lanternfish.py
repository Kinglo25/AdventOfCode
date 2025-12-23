# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Lanternfish.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/10 12:40:30 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/10 13:51:15 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def parser(fileName):
	with open(fileName) as f:
		data = [[int(n), 1] for n in f.read().strip().split(',')]
	return data

def lanternfish_reproduction(state, nDays):
	count = 0
	for _ in range(nDays):
		len_state = len(state)
		count = 0
		for i in range(len_state):
			if state[i][0] == 0:
				count += state[i][1]
				state[i][0] = 7
			state[i][0] -= 1
		if count:
			state.append([8, count])
	return sum(n[1] for n in state)
			
	
def main():
	initial_state = parser('input.txt')
	nDays = 256
	print(lanternfish_reproduction(initial_state, nDays))

main()
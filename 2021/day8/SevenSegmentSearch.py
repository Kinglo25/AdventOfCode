# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SevenSegmentSearch.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/11 21:30:23 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/11 22:38:04 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from collections import defaultdict

def parser(fileName):
	with open(fileName) as f:
		return [[segment.split() for segment in data.split('|')] for data in f.read().strip().split('\n')]

def decrypt(input):
	ans = 0
	for entry in input:
		groups = defaultdict(list)
		decoded = dict()
		patterns, output = entry
		for p in patterns:
			groups[len(p)].append(frozenset(p))
		for p in patterns:
			p = frozenset(p)
			len_p = len(p)
			if len_p == 2:
				decoded[1] = p
			elif len_p == 3:
				decoded[7] = p
			elif len_p == 4:
				decoded[4] = p
			elif len_p == 7:
				decoded[8] = p
			elif len_p == 5:
				if p >= groups[2][0]:
					decoded[3] = p
				elif len(p & groups[4][0]) == 3:
					decoded[5] = p
				else:
					decoded[2] = p
			elif len_p == 6:
				if groups[4][0] <= p:
					decoded[9] = p
				elif groups[2][0] <= p:
					decoded[0] = p
				else:
					decoded[6] = p
		decoded = {pattern: digit for digit, pattern in decoded.items()}
		number = 0
		for pattern in output:
			digit = decoded[frozenset(pattern)]
			number = number * 10 + digit
		ans += number
	return ans
def main():
	input = parser('input.txt')
	print(decrypt(input))
main()
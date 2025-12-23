# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    SyntaxScoring.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/12 16:19:33 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/12 17:16:49 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def parser(fileName):
	with open(fileName) as f:
		return [line for line in f.read().strip().split('\n')]

def calculate_score(s):
	stack = []
	illegal_points = {')': 3, ']': 57, '}': 1197, '>': 25137}
	legal_char = {')': '(', ']': '[', '}': '{', '>': '<'}
	for c in s:
		if c in legal_char:
			if not stack or legal_char[c] != stack.pop():
				return None
		else:
			stack.append(c)
	completion_points = {'(': 1, '[': 2, '{': 3, '<': 4}
	score = 0
	while stack:
		score = score * 5 + completion_points[stack.pop()]
	return score

def main():
	score = 0
	scores = []
	subsystem = parser('input.txt')
	for line in subsystem:

		score = calculate_score(line)
		if score is not None:
			scores.append(score)
	print(sorted(scores)[len(scores) // 2])

main()
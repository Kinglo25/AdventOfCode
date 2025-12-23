# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    giantSquid.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/09 13:20:32 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/09 18:37:48 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def bingo(numbers, boards, count):
	for n in numbers:
		for i, board in enumerate(boards):
			for row in board:
				if n in row:
					row[row.index(n)] = -1
			if any(all(cell == -1 for cell in row) for row in board) or any(all(cell == -1 for cell in row) for row in zip(*board)):
				if count == 1 and board[0][0] != -2:
					board = [[n + 1 if n == -1 else n for n in row] for row in board]
					return sum([sum(row) for row in board]) * n
				elif board[0][0] != -2:
					count -= 1
					print(count)
					board[0][0] = -2
	return
	

def main():
	with open('input.txt', 'r') as f:
		data = f.read().strip()
		numbers = data.split('\n')[0]
		numbers = [int(n) for n in numbers.split(',')]
		boards = [[[int(n) for n in row.split()] for row in board.split('\n')] for board in data.split('\n\n')[1:]]
		
		print(bingo(numbers, boards, len(boards)))

main()
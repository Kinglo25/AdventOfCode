# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 10:30:44 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/30 11:22:59 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 02 – Advent of Code 2016

def parser():
    with open("input.txt") as f:
        return [line for line in f.read().strip().splitlines()]

def find_start_pos(keypad):
    for x in range(len(keypad[0])):
        for y in range(len(keypad)):
            if keypad[x][y] == 5:
                return x, y

def decoder(procedure, keypad, instructions):
    x, y = find_start_pos(keypad)
    code = []
    for line in procedure:
        for c in line:
            dx, dy = instructions[c]
            if 0 <= x + dx < len(keypad) and 0 <= y + dy < len(keypad[0])\
                and keypad[x+dx][y+dy] != 0:
                x += dx
                y += dy
        code.append(str(keypad[x][y]))
    return "".join(code)

def main():
    procedure = parser()
    keypad_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    keypad_2 = [
        [0, 0, 1, 0, 0],
        [0, 2, 3, 4, 0],
        [5, 6, 7, 8, 9],
        [0, 'A', 'B', 'C', 0],
        [0, 0, 'D', 0, 0]
    ]
    instructions = {
        'R': (0, 1),
        'L': (0, -1),
        'U': (-1, 0),
        'D': (1, 0)
    }
    print("Day 02 solution for 2016:", decoder(procedure, keypad_1, instructions))
    print("Day 02 solution for 2016:", decoder(procedure, keypad_2, instructions))

if __name__ == "__main__":
    main()

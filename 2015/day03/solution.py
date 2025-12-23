# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/18 21:13:57 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/18 22:02:19 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 03 – Advent of Code 2015

def parser(fileName):
    with open(fileName) as f:
        data = f.read().strip()
    return data

def calc_n_houses(directions):
    santa = robo_santa = (0, 0)
    houses = {santa}
    moves = {
    '^': (0, 1),
    'v': (0, -1),
    '>': (1, 0),
    '<': (-1, 0),
    }
    for i, dir in enumerate(directions):
        dx, dy = moves[dir]
        if i & 1:
            santa = (santa[0] + dx, santa[1] + dy)
            houses.add(santa)
        else:
            robo_santa = (robo_santa[0] + dx, robo_santa[1] + dy)
            houses.add(robo_santa)
    return len(houses)

def main():
    directions = parser("input.txt")
    n_houses = calc_n_houses(directions)
    print("Day 03 solution for 2015:", n_houses)

if __name__ == "__main__":
    main()

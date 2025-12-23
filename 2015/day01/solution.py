# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/18 19:56:37 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/18 20:07:17 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 01 – Advent of Code 2015

def parser(fileName):
    with open(fileName) as f:
        data = f.read().strip()
    return data

def what_floor(data):
    floor = 0
    basement_pos = 0
    for p in data:
        basement_pos += 1
        if p == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return basement_pos
    return floor

def main():
    data = parser("input.txt")
    floor = what_floor(data)
    print("Day 01 solution for 2015:", floor)

if __name__ == "__main__":
    main()

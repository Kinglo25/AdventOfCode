# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/29 21:21:34 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/30 12:57:38 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 20 – Advent of Code 2015

from math import sqrt

def parser(file_name):
    with open(file_name) as f:
        return int(f.read().strip())

def lowest_house_number(n):
    limit = n // 10
    houses = [0] * limit
    for elf in range(1, limit):
        for i in range(elf, min(elf * 50 + 1, limit), elf):
            houses[i] += elf * 11
    for i, presents in enumerate(houses):
        if presents >= n:
            return i

def main():
    number = parser("input.txt")
    print("Day 20 solution for 2015:", lowest_house_number(number))

if __name__ == "__main__":
    main()

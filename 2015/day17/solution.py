# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 16:26:45 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/26 17:35:56 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 17 – Advent of Code 2015

from itertools import combinations

LITTERS = 150

def parser(file_name: str):
    with open(file_name) as f:
        return [int(n) for n in f.read().strip().splitlines()]

def combinations_of_containers(containers):
    count = 0
    for i in range(1, len(containers)):
        for cmb in combinations(containers, i):
            sum_cmb = sum(n for n in cmb)
            if sum_cmb == LITTERS:
                count += 1
    return count

def main():
    containers = parser("input.txt")
    containers.sort()
    print(containers)
    print("Day 17 solution for 2015:", combinations_of_containers(containers))

if __name__ == "__main__":
    main()

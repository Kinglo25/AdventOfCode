# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/23 21:10:03 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/24 16:06:15 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 13 – Advent of Code 2015

from collections import defaultdict
from math import inf

def parser(fileName):
    happiness = defaultdict(list)
    with open(fileName) as f:
        data = f.read().strip().splitlines()
        for line in data:
            name1, _,sign, happy_lvl, _,_,_,_,_,_, name2 = line.split()
            if sign == 'lose':
                happy_lvl = int(happy_lvl) * -1
            else:
                happy_lvl = int(happy_lvl)
            happiness[name1].append((name2[:-1], happy_lvl))
    return happiness

def optimal_arrangment(happiness):
    max_happy = float(-inf)
    for name in happiness:
        stack = [(name, [name], {name}, 0)]
        while stack:
            name1, perm, visited, total_happy = stack.pop()
            if len(perm) == len(happiness):
                for name4, happy4 in happiness[name1]:
                    if name4 == name:
                        for name5, happy5 in happiness[name]:
                            if name5 == name1:
                                max_happy = max(total_happy + happy4 + happy5, max_happy)

            for name2, happy2 in happiness[name1]:
                if name2 in visited:
                    continue
                for name3, happy3 in happiness[name2]:
                    if name3 == name1:
                        stack.append((name2, perm + [name2], visited | {name2}, total_happy + happy2 + happy3))
                        break
    return max_happy


def main():
    happiness = parser("input.txt")
    print("Day 13 solution for 2015:", optimal_arrangment(happiness))

if __name__ == "__main__":
    main()

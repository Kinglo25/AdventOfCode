# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/27 15:42:40 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/29 20:56:24 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 19 – Advent of Code 2015

from collections import defaultdict

def parser(file_name):
    replacement = defaultdict(list)
    with open(file_name) as f:
        raw, molecule = f.read().strip().split("\n\n")
        for r in raw.splitlines():
            old, new = r.strip().split(" => ")
            replacement[old].append(new)
        return replacement, molecule

def n_distinct_molecule(replacement, molecule):
    molecules = set()
    for i in range(len(molecule)):
        if molecule[i] in replacement:
            for r in replacement[molecule[i]]:
                molecules.add(molecule[:i] + r + molecule[i+1:])
        elif i < len(molecule) - 1 and molecule[i] + molecule[i + 1] in replacement:
            for r in replacement[molecule[i] + molecule[i + 1]]:
                molecules.add(molecule[:i] + r + molecule[i+2:])
    return len(molecules)

def main():
    replacement, molecule = parser("input.txt")
    print("Day 19 solution for 2015:", n_distinct_molecule(replacement, molecule))

if __name__ == "__main__":
    main()

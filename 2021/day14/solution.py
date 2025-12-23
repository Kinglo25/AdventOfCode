# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/15 18:12:15 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/15 22:03:24 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 14 – Advent of Code 2021

def parser(fileName):
    rules = {}
    polymer = {}
    with open(fileName) as f:
        polymer_str, data = f.read().strip().split('\n\n')
        last_elem = polymer_str[-1]
        for i in range(len(polymer_str) - 1):
            pair = polymer_str[i] + polymer_str[i + 1]
            polymer[pair] = 1
        for line in data.split('\n'):
            pair, insertion = line.split('->')
            rules[pair.strip()] = insertion.strip()
    return polymer, rules, last_elem

def polymerization(polymer, rules):
    new_polymer = {}
    for pair in polymer:
        insert = rules[pair]
        new_polymer[pair[0] + insert] = new_polymer.get(pair[0] + insert, 0) + polymer[pair]
        new_polymer[insert + pair[1]] = new_polymer.get(insert + pair[1], 0) + polymer[pair]
    return new_polymer

def main():
    polymer, rules, last_elem = parser("input.txt")
    steps = 40
    counter = {}
    counter[last_elem] = 1
    for _ in range(steps):
        polymer = polymerization(polymer, rules)
    for elem in polymer:
        counter[elem[0]] = counter.get(elem[0], 0) + polymer.get(elem)
    count = max(val for val in counter.values()) - min(val for val in counter.values())
    
    print("Day 14 solution for 2021:", count)
        

if __name__ == "__main__":
    main()

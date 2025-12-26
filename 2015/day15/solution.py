# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/24 18:02:05 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/25 22:51:04 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 15 – Advent of Code 2015

from collections import defaultdict
import copy

def parser(fileName):
    ingredients = defaultdict(dict)
    with open(fileName) as f:
        data = f.read().strip().splitlines()
        for line in data:
            parts = line.split(':')
            name = parts[0]
            for part in parts[1].strip().split(','):
                properties, q = part.split()
                ingredients[name][properties.strip()] = int(q)
    return ingredients

def calc_score(ingredients, f, c, b, s):
    score = 1
    combination = [f, c, b, s]
    recipe = copy.deepcopy(ingredients)
    for i, name in enumerate(recipe):
        for p in recipe[name]:
            recipe[name][p] *= combination[i]
    sums = []
    for p in recipe["Frosting"]:
        sums.append(sum(recipe[name][p] for name in recipe))
    if sums[-1] != 500:
        return 0
    for n in sums[:-1]:
        if n <= 0:
            return 0
        score *= n
    return score

def find_best_cookie(ingredients, teaspoons=100):
    score = 0
    for x in range(teaspoons + 1):
        for y in range(teaspoons + 1 - x):
            for z in range(teaspoons + 1 - x - y):
                w = teaspoons - x - y - z
                score = max(calc_score(ingredients, x, y, z, w), score)
    return score
        
def main():
    ingredients = parser("input.txt")

    print("Day 15 solution for 2015:", find_best_cookie(ingredients))

if __name__ == "__main__":
    main()

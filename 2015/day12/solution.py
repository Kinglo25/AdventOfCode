# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/23 17:34:53 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/23 21:00:48 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 12 – Advent of Code 2015

import json

def parser(fileName):
    with open(fileName) as f:
        return json.loads(f.read().strip())
        
def add_numbers(data):
    if isinstance(data, int):
        return data
    if isinstance(data, list):
        return sum(add_numbers(n) for n in data)
    if isinstance(data, dict):
        if "red" in data.values():
            return 0
        return sum(add_numbers(n) for n in data.values())
    return 0

def main():
    data = parser("input.txt")
    print("Day 12 solution for 2015:", add_numbers(data))

if __name__ == "__main__":
    main()

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/18 22:12:23 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/18 23:28:45 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 04 – Advent of Code 2015

import hashlib

def parser(fileName):
    with open(fileName) as f:
        data = f.read().strip()
    return data

def find_hash(key):
    i = 0
    while True:
        hexa = hashlib.md5((key + str(i)).encode()).hexdigest()
        if str(hexa).startswith('000000'):
            return i
        i += 1

def main():
    key = parser("input.txt")
    lowest_number = find_hash(key)
    print("Day 04 solution for 2015:", lowest_number)

if __name__ == "__main__":
    main()

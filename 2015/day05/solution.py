# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/18 23:31:45 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/19 00:15:25 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 05 – Advent of Code 2015

def parser(fileName):
    with open(fileName) as f:
        data = f.read().strip().splitlines()
    return data

def is_nice(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    bad_pairs = {'ab', 'cd', 'pq', 'xy'}
    prev = s[0]
    vowels_count = 0
    if s[0] in vowels:
        vowels_count += 1
    twice = False
    for c in s[1:]:
        if c in vowels:
            vowels_count += 1
        if prev + c in bad_pairs:
            return False
        if prev == c:
            twice = True
        prev = c
    return vowels_count >= 3 and twice
        
def main():
    data = parser("input.txt")
    count = 0
    for line in data:
        if is_nice(line):
            count += 1
    print("Day 05 solution for 2015:", count)

if __name__ == "__main__":
    main()

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/18 20:08:05 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/18 21:07:07 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 02 – Advent of Code 2015

def parser(fileName):
    with open(fileName) as f:
        return  [tuple(int(n) for n in line.split('x')) for line in f.read().strip().splitlines()]
        
def calc_area(dimensions):
    total = 0
    for l, w, h in dimensions:
        area = 2*l*w + 2*w*h + 2*h*l
        extra = min(l*w, w*h, h*l)
        total += extra + area
    return total

def calc_ribbon(dimensions):
    total = 0
    for l, w, h in dimensions:
        ribbon = min(l+w, l+h, w+h)*2 + l*w*h
        total += ribbon
    return total

def main():
    dimensions = parser("input.txt")
    paper_size = calc_area(dimensions)
    ribbon_size = calc_ribbon(dimensions)
    print("Day 02 solution for 2015:", paper_size, ribbon_size)

if __name__ == "__main__":
    main()

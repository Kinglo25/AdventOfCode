# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/23 16:37:39 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/23 17:29:14 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 11 – Advent of Code 2015

def parser(fileName):
    with open(fileName) as f:
        return [c for c in f.read().strip()]

# def alphabet_to_dec(n):
#     base = "abcdefghijklmnopqrstuvwxyz"
#     dec = 0
#     for c in n:
#         base.index(c)

def valid(p):
    dup_lst = []
    dup = False
    incr = False
    for i in range(len(p)):
        if p[i] in ('i', 'o', 'l'):
            return False
        if i < len(p) - 1 and p[i] == p[i + 1]:
            dup_lst.append(i)
            if len(dup_lst) >= 2 and dup_lst[-1] - dup_lst[-2] > 1:
                dup = True
        if i < len(p) - 2 and (ord(p[i]) == ord(p[i + 1]) - 1 == ord(p[i + 2]) - 2):
            incr = True
    return dup and incr


def next_password(p, steps):
    base = "abcdefghijklmnopqrstuvwxyz"
    i = 1
    step = 0
    while not valid(p) or step != steps:
        p[-i] = base[(base.index(p[-i]) + 1) % 26]
        while p[-i] == 'a':
            i += 1
            p[-i] = base[(base.index(p[-i]) + 1) % 26]
        i = 1
        if valid(p):
            step += 1
    return p


def main():
    password = parser("input.txt")
    steps = 2
    password = next_password(password, steps)
    print("Day 11 solution for 2015:", password)

if __name__ == "__main__":
    main()

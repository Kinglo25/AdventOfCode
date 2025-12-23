# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/21 13:42:55 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/23 13:37:56 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 08 – Advent of Code 2015

def parser(fileName):
    with open(fileName) as f:
        return f.read().strip()

def is_hexa(c):
    return c in "abcdef1234567890"

def str_literal_len(s):
    count = 0
    i = 1
    while i < len(s) - 1:
        if s[i] == '\\' and s[i + 1] == 'x':
            if is_hexa(s[i + 2]) and is_hexa(s[i + 3]):
                i += 4
        elif s[i] == '\\' and (s[i + 1] == '\\' or s[i + 1] == '\"'):
            i += 2
        else:
            i += 1
        count += 1
    return count

def new_encoded_string(s):
    count = 2  # new surrounding quotes
    for c in s:
        if c == '"' or c == '\\':
            count += 2
        else:
            count += 1
    return count

def main():
    data = parser("input.txt")
    total1 = total2 = total3 = 0
    for line in data.splitlines():
        total1 += len(line)
        total2 += str_literal_len(line)
        total3 += new_encoded_string(line)
    print("Day 08 solution for 2015:", total1 - total2, "and ", total3 - total1)
if __name__ == "__main__":
    main()

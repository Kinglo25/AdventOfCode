# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 17:50:56 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/26 17:52:08 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 18 – Advent of Code 2015

def parser(file_name):
    with open(file_name) as f:
        data = f.read().strip()


def main():
    grid = parser("input.txt")
    print("Day 18 solution for 2015:", data)

if __name__ == "__main__":
    main()

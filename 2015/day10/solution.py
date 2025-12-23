# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/23 15:45:26 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/23 16:25:29 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 10 – Advent of Code 2015

def parser(fileName):
    with open(fileName) as f:
        return f.read().strip()

def look_and_say(digit):
    prev = digit[0]
    count = 1
    new_n = ""
    for n in digit[1:]:
        if n == prev:
            count += 1
        else:
            new_n += str(count) + str(prev)
            count = 1
            prev = n
    return new_n



def main():
    digits = parser("input.txt")
    steps = 50
    print(digits)
    for _ in range(steps):
        digits = look_and_say(digits + 'x')
        print("Day 10 solution for 2015:", len(digits))

if __name__ == "__main__":
    main()

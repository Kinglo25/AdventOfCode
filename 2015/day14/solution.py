# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/24 16:06:31 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/24 17:56:32 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 14 – Advent of Code 2015

from collections import defaultdict

def parser(fileName):
    reindeers = defaultdict(dict)
    with open(fileName) as f:
        data = f.read().strip().splitlines()
        for line in data:
            parts = line.strip().split()
            name = parts[0]
            reindeers[name]["speed"] = int(parts[3])
            reindeers[name]["time"] = int(parts[6])
            reindeers[name]["rest"] = int(parts[13])
    return reindeers

def race(reindeers, seconds=2503):
    state = defaultdict(dict)
    for _ in range(seconds):
        for reindeer in reindeers:
            if state[reindeer].get("rest", 0) != 0:
                state[reindeer]["rest"] -= 1
                continue
            state[reindeer]["time"] = state[reindeer].get("time", reindeers[reindeer]["time"])
            state[reindeer]["time"] -= 1
            if state[reindeer]["time"] == 0:
                state[reindeer]["rest"] = reindeers[reindeer]["rest"]
                state[reindeer]["time"] = reindeers[reindeer]["time"]
            state[reindeer]["dist"] = state[reindeer].get("dist", 0) + reindeers[reindeer]["speed"]
        for reindeer in state:
            state[reindeer]["score"] = state[reindeer].get("score", 0)
            if state[reindeer]["dist"] == max(state[reindeer]["dist"] for reindeer in reindeers):
                state[reindeer]["score"] += 1
    return max(state[reindeer]["score"] for reindeer in reindeers)

def main():
    reindeers = parser("input.txt")
    print("Day 14 solution for 2015:", race(reindeers))

if __name__ == "__main__":
    main()

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/26 15:11:27 by Lomajeru          #+#    #+#              #
#    Updated: 2025/12/26 16:28:23 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 16 – Advent of Code 2015

from typing import Dict, List

# Part 2 comparison rules
SPECIAL_GT = {"cats", "trees"}
SPECIAL_LT = {"pomeranians", "goldfish"}

TICKER_TAPE: Dict[str, int] = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

def parse_aunts(file_name: str) -> List[Dict[str, int]]:
    aunts: List[Dict[str, int]] = []
    with open(file_name) as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            props = line.split(":", 1)[1].strip()
            aunt: Dict[str, int] = {}
            for part in props.split(","):
                key, val = part.strip().split(":")
                aunt[key.strip()] = int(val)
            aunts.append(aunt)
    return aunts

def matches(prop: str, value: int, tape: Dict[str, int]) -> bool:
    if prop not in tape:
        return True
    if prop in SPECIAL_GT:
        return value > tape[prop]
    if prop in SPECIAL_LT:
        return value < tape[prop]
    return value == tape[prop]


def find_matching_aunt_index(aunts: List[Dict[str, int]], tape: Dict[str, int]) -> int:
    for i, aunt in enumerate(aunts):
        ok = True
        for prop, value in aunt.items():
            if not matches(prop, value, tape):
                ok = False
                break
        if ok:
            return i + 1
    return -1


def main() -> None:
    aunts = parse_aunts("input.txt")
    print("Day 16 solution for 2015:", find_matching_aunt_index(aunts, TICKER_TAPE))

if __name__ == "__main__":
    main()

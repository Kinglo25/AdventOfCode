# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 16:50:10 by Lomajeru          #+#    #+#              #
#    Updated: 2026/01/06 00:52:32 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# Day 21 – Advent of Code 2015

from dataclasses import dataclass
from math import inf
import itertools

@dataclass
class Item:
    name: str
    cost: int
    damage: int
    armor: int

@dataclass
class Character:
    damage: int = 0
    armor: int = 0
    hit_points: int = 100
    base_hp: int = 100

    def equip(self, items):
        self.armor = sum(item.armor for item in items if item)
        self.damage = sum(item.damage for item in items if item)

    def unequip(self):
        self.damage = 0
        self.armor = 0
    
    def attack(self, enemy):
        amount = max(1, self.damage - enemy.armor)
        enemy.take_damage(amount)

    def take_damage(self, amount):
        self.hit_points -= amount
    
    def reset(self):
        self.hit_points = self.base_hp

def parse_items(line):
    name = " ".join(line[:-3])
    cost, damage, armor = map(int, line[-3:])
    return Item(name, cost, damage, armor)

def parse_shop(path: str = "shop.txt") -> dict[str, list[Item]]:
    with open(path) as f:
        text = f.read().strip()
    shop: dict[str, list[Item]] = {}
    for block in text.split('\n\n'):
        lines = block.splitlines()
        header = lines[0]
        category = header.split(':')[0]
        items: list[Item] = []
        for line in lines[1:]:
            items.append(parse_items(line.split()))
        shop[category] = items
    return shop

def parse_boss(path: str = "input.txt"):
    with open(path) as f:
        text = f.read().strip()
        lines = text.splitlines()
        hit_point = int(lines[0].split()[-1])
        damage = int(lines[1].split()[-1])
        armor = int(lines[2].split()[-1])
        return Character(damage, armor, hit_point, hit_point)

def parser():
    boss = parse_boss()
    shop = parse_shop()
    return boss, shop

def generate_all_loadouts(shop):
    for weapon in shop["Weapons"]:
        for armor in shop["Armor"] + [None]:
            for ring_atk in shop["Rings"][:3] + [None]:
                for ring_def in shop["Rings"][3:] + [None]:
                    yield (weapon, armor, ring_atk, ring_def)
                    
def play(boss, player):
    turn = 1
    while boss.hit_points > 0 and player.hit_points > 0:
        if turn & 1:
            player.attack(boss)
        else:
            boss.attack(player)
        turn += 1
    return "Player" if player.hit_points > 0 else "Boss"

def generate_all_loadouts_part2(shop):
    for weapon in shop["Weapons"]:
        for armor in shop["Armor"] + [None]:
            for ring in itertools.chain.from_iterable(
                itertools.combinations(shop["Rings"], r) for r in range(3)):
                yield (weapon, armor, *ring)

def launch_game(loadout, player, boss):
    player.equip(loadout)
    winner = play(boss, player)
    boss.reset()
    player.reset()
    player.unequip()
    return winner

def game(boss, shop, player):
    min_cost = float(+inf)
    max_cost = float(-inf)
    for loadout in generate_all_loadouts(shop):
        winner = launch_game(loadout, player, boss)
        if winner == "Player":
            cost = sum(item.cost for item in loadout if item)
            min_cost = min(min_cost, cost)
    for loadout in generate_all_loadouts_part2(shop):
        winner = launch_game(loadout, player, boss)
        if winner == "Boss":
            cost = sum(item.cost for item in loadout if item)
            max_cost = max(cost, max_cost)
    return min_cost, max_cost
        

def main():
    boss, shop = parser()
    player = Character()
    print("Day 21 solution for 2015:", game(boss, shop, player))

if __name__ == "__main__":
    main()

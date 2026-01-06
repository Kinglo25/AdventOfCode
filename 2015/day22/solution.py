# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    solution.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Lomajeru <lomajeru@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/06 00:57:15 by Lomajeru          #+#    #+#              #
#    Updated: 2026/01/06 02:35:06 by Lomajeru         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Day 22 – Advent of Code 2015

from dataclasses import dataclass

@dataclass
class Spell:
    name: str
    mana_cost: int
    duration: int = 0

    def effect(self, caster, target, game_state):
        raise NotImplementedError
    
@dataclass
class MagicMissile(Spell):
    def effect(self, caster, target, game_state):
        target.hp -= 4

@dataclass
class Drain(Spell):
    def effect(self, caster, target, game_state):
        target.hp -= 2
        caster.hp += 2

@dataclass
class Shield(Spell):
    def effect(self, caster, target, game_state):
        caster.armor += 7

@dataclass
class Poison(Spell):
    def effect(self, caster, target, game_state):
        target.hp -= 3

@dataclass
class Recharge(Spell):
    def effect(self, caster, target, game_state):
        caster.mana += 101

@dataclass
class Character:
    hp: int
    mana: int
    armor: int
    damage: int

def initialize_game():
    player = Character(50, 500, 0, 0)
    boss = Character(51, 0, 0, 9)
    magic_missile = MagicMissile("Magic Missile", 53)
    drain = Drain("Drain", 73)
    shield = Shield("Shield", 113, 6)
    poison = Poison("Poison", 173, 6)
    recharge = Recharge("Recharge", 229, 5)
    return player, boss, [magic_missile, drain, shield, poison, recharge]

def main():
    player, boss, spell_book = initialize_game()
    print("Day 22 solution for 2015:", print(player, boss, spell_book))

if __name__ == "__main__":
    main()

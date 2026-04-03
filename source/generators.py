import random
from source.entity import Entity


def gen_event():
    events_list = ["find a treasure", "find a monster",
                   "find nothing"]
    event = random.choice(events_list)
    return event


def gen_player():
    name = input("Enter player name: ")
    player = Entity(name, 100, 0, 20)
    return player


def gen_monster(player_level: int) -> object:
    monster_list = ["ork",
                    "slime",
                    "vampire bat",
                    "dino",
                    "spider",
                    "Skeleton"]
    name = random.choice(monster_list)
    level = random.randint(player_level + 1, player_level + 2)
    base_hp = 80 + (20 * level)
    base_atk = 10 + (5 * level)
    monster = Entity(name, base_hp, level, base_atk)
    return monster

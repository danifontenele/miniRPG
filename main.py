import random


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def get_choice(self) -> int:
        choice = -1
        while choice < 1 or choice > 3:
            try:
                choice = int(input("action:\n1)attack\n2)heal\n3)run\n"))
            except ValueError:
                print("invlaid choice, try again!")
        return choice

    def start(self):
        while self.player.hp > 0 and self.enemy.hp > 0:
            print("=== Battle ===\n")
            print(f"{self.player.name}\n"
                  f"level: {self.player.level}\n"
                  f"hp: {self.player.hp}")
            print(f"\nx\n\n{self.enemy.name}\n"
                  f"level: {self.enemy.level}\n"
                  f"hp: {self.enemy.hp}\n")

            choice = self.get_choice()
            if choice == 1:
                ret_attack = self.player.do_attack(self.enemy)
                if ret_attack < 0:
                    print(f"\n{self.enemy.name} died\n")
                    self.player.hp += 10
                    if self.player.hp >= self.player.max_hp_per_level:
                        self.player.level_up()
                    break
                print(f"\nYou attacked\nDamage: -{ret_attack}\n")

            elif choice == 2:
                potion = 15
                self.player.heal(potion)
                print("\nPotion used: +15 hp\n")

            elif choice == 3:
                print(f"\nYou ran away from {self.enemy.name}\n")
                break
            ret_attack = self.enemy.do_attack(self.player)
            if ret_attack < 0:
                return -1
            print(f"{self.enemy.name} attacked\nDamage: -{ret_attack}\n")


# Class with features and methods for all the entities of the game
class Entity:
    def __init__(self, name: str, hp: int, level: int, attack: int):
        self.name = name
        self.hp = hp
        self.level = level
        self.attack = attack
        self.max_hp = hp
        self.xp = 0
        self.max_xp_per_level = 50
        self.cash = 0

    def level_up(self) -> None:
        self.hp = self.max_hp
        self.level += 1
        self.hp += 10
        self.max_hp += 10
        self.attack += 10
        self.max_xp_per_level += 30
        print(f"{self.name} did level-up to level {self.level}!")

    def gain_money(self, amount: int) -> None:
        self.cash += amount

    def spend_money(self, amount: int) -> None:
        self.cash -= amount

    def do_attack(self, target):
        is_dead = target.take_damage(self.attack)
        if is_dead is True:
            return -1
        return self.attack

    def take_damage(self, damage):
        self.hp = self.hp - damage
        if self.hp <= 0:
            self.hp = 0
            return True
        return False

    def heal(self, amount: int) -> None:
        self.hp = min(self.hp + amount, self.max_hp)


def gen_event():
    events_list = ["find a treasure", "find a monster",
                   "find nothing"]
    event = random.choice(events_list)
    return event


def gen_player():
    name = input("Enter player name: ")
    player = Entity(name, 100, 0, 20)
    return player


def gen_monster() -> object:
    monster_list = ["ork", "slime", "vampire bat", "dino", "spider"]
    name = random.choice(monster_list)
    level = random.randint(1, 4)
    if level == 1:
        monster_l1 = Entity(name, 90, 1, 15)
        return monster_l1
    elif level == 2:
        monster_l2 = Entity(name, 105, 2, 20)
        return monster_l2
    elif level == 3:
        monster_l3 = Entity(name, 120, 3, 30)
        return monster_l3
    elif level == 4:
        boss = Entity(name, 150, 4, 35)
        return boss


def game_loop():
    input("Digit Enter to start\n")
    print("Generating player...")
    player = gen_player()
    print(f"Player {player.name} generated!\n")
    while True:
        print(f"{player.name}\n"
              f"level: {player.level}\n"
              f"hp: {player.hp}\n"
              f"coins: {player.cash}\n")
        choice = int(input("Choices:\n"
                           "1)Explore\n"
                           "2)Store\n"
                           "0)Exit\n"))
        if choice == 0:
            print("\nClosing the game...")
            break
        elif choice == 1:
            event = gen_event()
            print(f"\nYou did {event}!\n")
            if event == "find a treasure":
                player.gain_money(10)
                print("+10$\n")
            elif event == "find a monster":
                monster = gen_monster()
                battle = Battle(player, monster)
                ret_battle = battle.start()
                if ret_battle == -1:
                    print("You died!")
                    choice = int(input("Choices:\n"
                                       "1) Try gain\n"
                                       "2) Give up\n"))
                    if choice == 1:
                        continue
                    elif choice == 2:
                        print("Game over!")
                        return
                if ret_battle == 1:
                    print(f"You defeated {monster.name}!\n")
    print("Game finished!")


def main():
    game_loop()


if __name__ == "__main__":
    main()

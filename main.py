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
                    return 1
                print(f"\nYou attacked\nDamage: {ret_attack}\n")

            elif choice == 2:
                if self.player.potions > 0:
                    self.player.use_potion()
                else:
                    print("\nYou have no more potions!\n")

            elif choice == 3:
                print(f"\nYou ran away from {self.enemy.name} "
                      f"level {self.enemy.level}\n")
                return 0
            ret_attack = self.enemy.do_attack(self.player)
            if ret_attack < 0:
                return -1
            print(f"{self.enemy.name} attacked\nDamage: {ret_attack}\n")


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
        self.potions = 0

    def gain_xp(self, amount: int):
        self.xp += amount
        if self.xp >= self.max_xp_per_level:
            self.level_up()
            self.xp = 0

    def level_up(self) -> None:
        self.hp = self.max_hp  # retore hp
        self.level += 1  # level up
        self.hp += 10  # upgrade hp
        self.max_hp += 10  # upgrade min xp for next level
        self.attack += 10  # upgrade damage
        self.max_xp_per_level += 30
        print(f"{self.name} did level-up to level {self.level}!")

    def gain_money(self, amount: int) -> None:
        self.cash += amount

    def spend_money(self, amount: int) -> None:
        self.cash -= amount

    def do_attack(self, target):
        damage = max(1, random.randint(self.attack - 5, self.attack + 5))
        is_dead = target.take_damage(damage)
        if is_dead is True:
            return -1
        return damage

    def take_damage(self, damage):
        self.hp = self.hp - damage
        if self.hp <= 0:
            self.hp = 0
            return True
        return False

    def use_potion(self) -> None:
        potions = [15, 20, 25]
        amount = random.choice(potions)
        self.heal(amount)
        print(f"\nPotion used: +{amount} hp\n")

    def heal(self, amount: int) -> None:
        self.hp = min(self.hp + amount, self.max_hp)
        return amount


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
    monster_list = ["ork",
                    "slime",
                    "vampire bat",
                    "dino",
                    "spider",
                    "Skeleton"]
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


def store(player: object):
    while True:
        print("\n=== Store ===\n")
        print(f"{player.name}\n"
              f"Cash: {player.cash}\n")
        print("Buy an item:\n"
              "1) Potion: 10$\n"
              "2) Medium Sword: 50$\n"
              "3) Epic Sword: 100$\n"
              "4) Legendary Sword: 250$\n"
              "0) Exit")
        store_choice = int(input("\nChoice: \n"))
        if store_choice == 0:
            break
        elif store_choice == 1:
            if player.cash < 10:
                print("You don't have cash enough")
            else:
                player.spend_money(10)
                player.potions += 1
                print("Bought Potion (-10$)")
        elif store_choice == 2:
            if player.cash < 50:
                print("You don't have cash enough")
            else:
                player.spend_money(50)
                player.attack += 5
                print("\nBought Medium Sword\n+5 attack\n-50$\n")
        elif store_choice == 3:
            if player.cash < 100:
                print("You don't have cash enough")
            else:
                player.spend_money(100)
                player.attack += 15
                print("Bought Epic Sword\n+15 attack\n-100$")
        elif store_choice == 4:
            if player.cash < 250:
                print("You don't have cash enough")
            else:
                player.spend_money(250)
                player.attack += 50
                print("Bought Legendary\n+50 attack\n-250$)\n")


def inventory(player: object):
    while True:
        print("\n=== Inventory ===\n")
        print(f"0) Exit\n"
              f"1) Potions: {player.potions}\n")
        choice = int(input("Choose intem: "))
        if choice == 0:
            return
        elif choice == 1:
            if player.potions > 0:
                player.use_potion()
            else:
                print("\nYou have no more potions!\n")


def game_loop():
    input("Digit Enter to start\n")
    print("Generating player...")
    player = gen_player()
    print(f"Player {player.name} generated!\n")
    while True:
        print(f"{player.name}\n"
              f"level: {player.level}\n"
              f"hp: {player.hp}/{player.max_hp}\n"
              f"xp: {player.xp}/{player.max_xp_per_level}\n"
              f"coins: {player.cash}\n")
        choice = int(input("Choices:\n"
                           "1)Explore\n"
                           "2)Store\n"
                           "3)Inventory\n"
                           "0)Exit\n"))

        if choice == 0:
            print("\nClosing the game...")
            break

        elif choice == 2:
            store(player)
        
        elif choice == 3:
            inventory(player)

        elif choice == 1:
            event = gen_event()
            print(f"\nYou did {event}!\n")
            if event == "find a treasure":
                treasures = [5, 10, 15]
                amount = random.choice(treasures)
                player.gain_money(amount)
                print(f"{amount}$\n")

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
                        player.heal(player.max_hp)
                        player.xp = 0
                        continue
                    elif choice == 2:
                        print("Game over!")
                        return

                elif ret_battle == 1:
                    print(f"You defeated {monster.name}!\n")
                    amount_xp = monster.level * 20
                    amount_cash = monster.level * 5
                    player.gain_xp(amount_xp)
                    player.gain_money(amount_cash)
                    print(f"\n+{amount_xp}xp\n+{amount_cash}$\n")

                elif ret_battle == 0:
                    continue
    print("Game finished!")


def main():
    game_loop()


if __name__ == "__main__":
    main()

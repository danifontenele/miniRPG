class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def get_choice(self) -> int:
        choice = -1
        while choice < 1 or choice > 3:
            try:
                print("actions:\n1)attack\n2)heal\n3)run\n")
                choice = int(input("choice: "))
            except ValueError:
                print("\ninvlaid choice, try again!\n")
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

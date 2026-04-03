import random


# Class with features and methods for all the entities of the game
class Entity:
    def __init__(self, name: str, hp: int, level: int, base_attack: int):
        self.name = name
        self.hp = hp
        self.level = level
        self.weapon_attack = 0
        self.base_attack = base_attack
        self.max_hp = hp
        self.xp = 0
        self.max_xp_per_level = 50
        self.cash = 0
        self.potions = 0

    def get_attack(self):
        return self.base_attack + self.weapon_attack

    def gain_xp(self, amount: int):
        self.xp += amount
        # Loop to make sure it level up even 2 levels at once
        while self.xp >= self.max_xp_per_level:
            self.xp = self.xp - self.max_xp_per_level
            self.level_up()

    def level_up(self) -> None:
        self.hp = self.max_hp  # retore hp
        self.level += 1  # level up
        self.hp += 10  # upgrade hp
        self.max_hp += 10  # upgrade min xp for next level
        self.base_attack += 10  # upgrade damage
        self.max_xp_per_level += 30
        print(f"{self.name} did level-up to level {self.level}!")

    def gain_money(self, amount: int) -> None:
        self.cash += amount

    def spend_money(self, amount: int) -> None:
        self.cash -= amount

    def do_attack(self, target):
        base = self.get_attack()
        damage = max(1, random.randint(base - 5, base + 5))
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
        if self.potions <= 0:
            return
        potions = [15, 20, 25]
        amount = random.choice(potions)
        self.heal(amount)
        self.potions -= 1
        print(f"\nPotion used: +{amount} hp\n")

    def heal(self, amount: int) -> None:
        self.hp = min(self.hp + amount, self.max_hp)
        return amount

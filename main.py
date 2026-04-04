import random
from source.battle import Battle
from source.generators import gen_event, gen_player, gen_monster
from source.store import store
from source.inventory import inventory


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
        print("Actions:\n"
              "1)Explore\n"
              "2)Store\n"
              "3)Inventory\n"
              "0)Exit\n")
        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("\nInvalid option, try again!\n")
            continue
        if choice == 0:
            try:
                confirm = int(input("\nDo you want to quit the game?\n"
                                    "1) Yes\n"
                                    "2) No\n"))
                if confirm == 1:
                    print("\nClosing the game...")
                    break
            except ValueError:
                print("\nInvalid option, try again!\n")
            continue

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
                monster = gen_monster(player.level)
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
                        player.cash = 0
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

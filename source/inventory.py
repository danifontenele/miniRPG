def inventory(player: object):
    while True:
        try:
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
        except ValueError:
            print("\ninvlaid choice, try again!\n")

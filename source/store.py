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
        try:
            store_choice = int(input("\nChoice: "))
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
                    player.weapon_attack = 5
                    print("\nBought Medium Sword\n+5 attack\n-50$\n")
            elif store_choice == 3:
                if player.cash < 100:
                    print("You don't have cash enough")
                else:
                    player.spend_money(100)
                    player.weapon_attack = 15
                    print("Bought Epic Sword\n+15 attack\n-100$")
            elif store_choice == 4:
                if player.cash < 250:
                    print("\nYou don't have cash enough")
                else:
                    player.spend_money(250)
                    player.weapon_attack = 50
                    print("Bought Legendary\n+50 attack\n-250$)\n")
        except ValueError:
            print("\ninvlaid choice, try again!\n")

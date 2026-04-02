*This project simulates a simplified RPG.

Created by Carlos Alvares.
# mini RPG
## Description
This project implements a simple role-playing game on terminal.
The game get your username, creating your player. You can explore and fight different level of monsters. The game has different level of monster increasing the difficulty.

### Goal


### The challenges and solutions
• Create different enviroments(main menu, store, inventory)
- I used infinite loops for each enviroment with an exit option.

• Upgrade the player
- System of xp gaining + level up, store with itens to upgrade player damage, store with item to heal the player after fights

• Monster factory
- Create a variable system of monsters generation to make the game more interesting to play!

## System Design

### Full program flow:
```
main.py
```

## The algorithm
For each track in the dataset:

1. 

## Project Structure
```
miniRT/
│
├── main.py
└── 
```
## How to Run
```
Clone the repository:

https:

git clone https://github.com/danifontenele/miniRPG.git

or

ssh:

git clone git@github.com:danifontenele/miniRPG.git

Run the program:

python3 main.py
```
## Example run
```
user@User_MAC miniRPG_rep % python3 main.py  
Digit Enter to start

Generating player...
Enter player name: calvares
Player calvares generated!

calvares
level: 0
hp: 100/100
xp: 0/50
coins: 0

Choices:
1)Explore
2)Store
3)Inventory
0)Exit
1 //input

You did find a monster!

=== Battle ===

calvares
level: 0
hp: 100

x

dino
level: 4
hp: 150

action:
1)attack
2)heal
3)run
3 //input

You ran away from dino level 4

...

calvares
level: 0
hp: 100/100
xp: 0/50
coins: 35

Choices:
1)Explore
2)Store
3)Inventory
0)Exit
3

=== Inventory ===

0) Exit
1) Potions: 0

Choose intem: 0
calvares
level: 0
hp: 100/100
xp: 0/50
coins: 35

Choices:
1)Explore
2)Store
3)Inventory
0)Exit
0

Closing the game...
Game finished!

```

## Limitations
. The game has only CLI, so the progress depends on choosing options with keyboard input.

## Improvements to include:
```
[] Equipment system
[] Change the system design increasing modular organization: allow to improve more in the future
[] Critic attack: random attack hits more
[] Better enemy generation: factory model
[] Storytelling
[x] Store to buy potions and upgrades.
[x] Variable damage in the attacking system.
```

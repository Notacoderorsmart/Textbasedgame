# combat loop example

import random

class Weapon:
    def __init__(self, weapon_type, min_damage, max_damage):
        self.weapon_type = weapon_type
        self.min_damage = min_damage
        self.max_damage = max_damage

    def attack(self):
        attack = random.randint(self.min_damage, self.max_damage)
        print(f"{self.weapon_type} does {attack} damage")
        return attack


weapons_dict = {
    "sword": Weapon("sword", 1, 6),
    "axe": Weapon("axe", 1, 9),
    "bow": Weapon("bow", 1, 10),
    "wand": Weapon("wand", 1, 7)
}


class Enemy:
    def __init__(self, name, health, weapon=None):
        self.name = name
        self.health = health
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            damage = self.weapon.attack()
            print(f"{self.name} attacks with {self.weapon.weapon_type} and does {damage} damage!")
        else:
            damage = random.randint(1, 5)
            print(f"{self.name} attacks with fists and does {damage} damage!")
        return damage


def generate_enemy():
    enemy_type = random.choice(["Goblin", "Orc", "Troll"])
    health = random.randint(50, 100)
    weapon_type = random.choice(list(weapons_dict.keys()))
    weapon = weapons_dict[weapon_type]
    enemy = Enemy(enemy_type, health, weapon)
    print(f"A {enemy.name} appears with {enemy.health} health and a {enemy.weapon.weapon_type} as a weapon!\n")
    return enemy


def combat(player, enemy):
    round_num = 1
    while player.health > 0 and enemy.health > 0:
        print(f"Round {round_num}")
        print(f"{player.name} has {player.health} health left")
        print(f"{enemy.name} has {enemy.health} health left\n")
        input("Press Enter to continue...")
        player_damage = player.attack()
        enemy.health -= player_damage
        if enemy.health <= 0:
            break
        enemy_damage = enemy.attack()
        player.health -= enemy_damage
        print()
        input("Press Enter to continue...")
        round_num += 1
    if player.health <= 0:
        print("Game Over - You lose!")
    else:
        print("You won the battle!")


player = Enemy("Player", 100, weapons_dict["sword"])

# First fight
print("Fight 1:")
enemy1 = generate_enemy()
combat(player, enemy1)

# Second fight
print("Fight 2:")
enemy2 = generate_enemy()
combat(player, enemy2)

# Third fight
print("Fight 3:")
enemy3 = generate_enemy()
combat(player, enemy3)

print("Game Over - You won all the fights!") 


#### #### #### #### #### #### #### ####
#                                     #
#            DOCUMENTATION            #
#                                     #
#### #### #### #### #### #### #### ####


Introduction
This code is a simple text-based combat game where the player fights against randomly generated enemies. The game is turn-based, with the player and enemy taking turns to attack until one of them loses all their health points.

Code Explanation
The code begins by importing the random module, which is used for generating random numbers.

The Weapon Class
The Weapon class is defined next. It has an __init__ method that initializes the attributes weapon_type, min_damage, and max_damage. It also has an attack method that generates a random number between min_damage and max_damage (inclusive) and prints a message indicating the amount of damage dealt. The attack method then returns the damage amount as an integer.

The Enemy Class
The Enemy class is defined next. It has an __init__ method that initializes the attributes name, health, and weapon (which is set to None by default). It also has an attack method that checks if the enemy has a weapon. If it does, the method calls the weapon's attack method and prints a message indicating the amount of damage dealt. If the enemy does not have a weapon, the method generates a random number between 1 and 5 (inclusive) and prints a message indicating the amount of damage dealt. The attack method then returns the damage amount as an integer.

The generate_enemy Function
The generate_enemy function generates a new enemy with a random name, health between 50 and 100, and a random weapon selected from a dictionary of weapons (weapons_dict). The function then prints a message indicating the enemy's name, health, and weapon, and returns the newly created Enemy object.

The combat Function
The combat function takes two Enemy objects as arguments: player and enemy. It starts a turn-based combat sequence where the player and enemy take turns attacking until one of them loses all their health points. The function uses a while loop to repeatedly execute a single round of combat. In each round, the function prints the current round number, the current health points of both the player and the enemy, and waits for the user to press Enter before continuing. The function then calls the attack method of the player object and subtracts the resulting damage from the enemy's health. If the enemy's health is reduced to zero or below, the loop breaks and the function ends. Otherwise, the function calls the attack method of the enemy object and subtracts the resulting damage from the player's health. The function then waits for the user to press Enter again before starting the next round. If the player's health is reduced to zero or below, the function ends with a "Game Over - You lose!" message. Otherwise, if the enemy's health is reduced to zero or below, the function ends with a "You won the battle!" message.

Starting the Game
The code then creates a player object with the name "Player", 100 health points, and a sword weapon with minimum and maximum damage of 1 and 6, respectively. It then starts three fights using the generate_enemy function and the combat function, printing a message indicating the current fight number before each fight. If the player wins all three fights, the code ends with a "Game Over - You won all the fights!" message.
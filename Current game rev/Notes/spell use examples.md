# class use examples

import random

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Spells:
    def __init__(self, spell_name, min_damage, max_damage, health_cost):
        self.spell_name = spell_name
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.health_cost = health_cost

    def attack(self, user,target):
        attack = random.randint(self.min_damage, self.max_damage)
        user_health_damage = random.randint(1, self.health_cost)
        user.health -= user_health_damage
        target.health -= attack
        print(f"{user.name} lost {user_health_damage} health as a result of using {self.spell_name}")
        print(f"{self.spell_name} does {attack} damage to {target.name}")
        print(f"{target.name} has {target.health} health left")

    def use(self, user, target):
        if user.health < self.health_cost:
            print(f"{user.name} does not have enough health to use {self.spell_name}")
        else:
            self.attack(user, target)

player = Character("Player", 100)
enemy = Character("Enemy", 100)

fireball = Spells("Fireball", 10, 20, 5)

while player.health > 0 and enemy.health > 0:
    print("\n--- New Round ---")
    print(f"{player.name} has {player.health} health left")
    print(f"{enemy.name} has {enemy.health} health left")
    fireball.use(player, enemy)
    if enemy.health <= 0:
        break
    fireball.use(enemy, player)

if player.health <= 0:
    print("Game Over - You lose!")
else:
    print("Game Over - You win!")

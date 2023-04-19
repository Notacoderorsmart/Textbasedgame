# enemy class use example

The enemy class should be constructed as below, you can add more if you require more information

class Enemy:
    def __init__(self, enemy_type, health, weapon,strength, endurance, dexterity, intelligence, wisdom, charisma,loot):
        self.enemy_type = enemy_type
        self.health = health
        self.weapon = weapon
        self.strength = strength
        self.endurance = endurance
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.loot = loot

when creating an enemy you write it like below

enemy1 = Enemy(enemy_type="Goblin", health=50, weapon="Sword", strength=10, endurance=8, dexterity=6, intelligence=4, wisdom=2, charisma=3, loot=["Gold", "Potion"])

import random
from colorama import Fore, Style

class Player:
    def __init__(self, player_name, player_health, player_strength, player_endurance, player_dexterity, player_intelligence, player_wisdom, player_charisma, player_inventory, player_gold, player_armour, player_xp_points, player_level=1):
        self.name             = player_name
        self.health           = player_health
        self.strength         = player_strength
        self.endurance        = player_endurance
        self.dexterity        = player_dexterity
        self.intelligence     = player_intelligence
        self.wisdom           = player_wisdom
        self.charisma         = player_charisma
        self.inventory        = player_inventory
        self.gold             = player_gold
        self.armour           = player_armour
        self.xp               = player_xp_points
        self.level            = player_level
        self.xp_to_next_level = 100 # starting xp value of player
        self.xp_increment     = 100 # constand value of d(n-1)

    def level_up(self):
            current_xp = self.xp
            xp_inc = self.xp_increment
            xp_to_next_level = self.xp_to_next_level

            # check if player has enough XP to level up
            if current_xp >= xp_to_next_level:
                self.level += 1
                self.xp_to_next_level += self.xp_to_next_level + xp_inc + ((self.level - 2) * xp_inc) # formula to increase xp needed each level
            self.level_up()  # recursive call to check if player can level up again

    def gain_xp(self, enemy):
        self.xp += enemy.xp
        self.level_up()  # check if player can level up after gaining XP

    def armour_defence(self, enemy):
        armour = self.armour
        damage_to_player = enemy.enemy_attack
        if damage_to_player > armour:
            damage_to_player = enemy.enemy_attack - armour
        if damage_to_player <= armour:
            print(Fore.GREEN, f"Your armour completely absorped the damage from that attack, that was lucky!" + Style.RESET_ALL)
        else:
            armour_block = enemy.enemy_attack - damage_to_player
            print(Fore.GREEN, f"Your armour blocked {armour_block} points of damage!" + Style.RESET_ALL)
            return damage_to_player
        self.health -= damage_to_player
        return self.health

    def player_combat_loop(self,enemy):
        player_attack_choice = None
        while player_attack_choice is None:
            player_attack_choice = input("""Do you want to use magic or weapon?\nPlease select either magic, or weapon!\n> """).lower()
            if "magic" in player_attack_choice:
                print(Fore.YELLOW, """You open up your spell book.\nYour spell book contains these spells""" + Style.RESET_ALL)
                for key in spell_type.keys():
                    print(key)
                spell_choice = input("{}What spell do you want to use?{}\n>".format(Fore.YELLOW, Style.RESET_ALL)).lower()
                if spell_choice in spell_type.keys():
                    attack_choice = spell_choice
                    Player.player_spell_attack(player,spell_choice, enemy)
                    return attack_choice
                else:
                    print(f"{Fore.RED}{spell_choice} is not in your spell book! Please pick another.{Style.RESET_ALL}")
                    player_attack_choice = None
            elif "weapon" in player_attack_choice:
                self.weapon = "weapon"
                attack_choice = self.weapon
                Player.player_attack(self, enemy)
                return attack_choice
            else:
                print_error_message("ERROR: I am sorry i didnt understand you, please try again!")
                player_attack_choice = None
        if spell_choice in spell_type.keys():
            self.player_spell_attack(spell_choice, enemy)
            player_attack_damage = self.spell_type[spell_choice]
            player_attack_type = spell_choice

            return attack_choice
        if player.player_combat_loop(attack_choice) == "weapon":
                player_attack_type = player.player_attack(player_attack_type)
                player_attack_damage = player.player_attack(player_attack_damage)
        else:
            player_attack_type = player.player_spell_attack(player_attack_type)
            player_attack_damage = player.player_spell_attack(player_attack_damage)
        print(Fore.GREEN, f"You attack the {enemy.enemy_type} with your {player_attack_type}")
        print(f"{player_attack_type} does {player_attack_damage} damage" + Style.RESET_ALL)
        print_debug_message("DEBUG: class:weapon - Player.attack - weapon_attack = " + str(player_attack_damage))
        return player_attack_damage
            
    def player_spell_attack(user, self,target):
        int_mod = user.intelligence
        print_debug_message(f"DEBUG: Player - player_spell_attack - user.intelligence + int_mod = user_intelligence:{user.intelligence} + int_mod:{int_mod}")
        spell_used = spell_type[self]
        print_debug_message(f"DEBUG: Player - player_spell_attack - spell_used + spell_type[self] = spell_used:{spell_used} spell_type{spell_type}")
        attack = random.randint(spell_used.min_damage, spell_used.max_damage)
        print_debug_message(f"DEBUG: Player - player_spell_attack - user.health + int_mod =  health:{user.health}  intelligence mod{int_mod}")
        user_health_damage = spell_used.health_cost - int_mod
        user.health -= user_health_damage
        target.health -= attack
        print(f"{self} does {attack} damage to {target.enemy_type}")
        print(f"{target.enemy_type} has {target.health} health left")
        print(f"{user.name} lost {user_health_damage} health as a result of using {self}")
        player_spell_damage = attack
        attack_type = self
        attack_damage = player_spell_damage
        return player_spell_damage, attack_damage, attack_type,

    def player_attack(self):
        while self.weapon  == "weapon":
            self.weapon = input("Please pick a weapon to fight with!\n>").lower()
            if self.weapon is None:
                print("Please pick a weapon")
            elif self.weapon not in weapon_type.keys():
                    print("You Do not have that weapon, please pick another!")
                    self.weapon = None
            else:
                if self.weapon in weapon_type.keys():
                    weapon_used = self.weapon
                    if self.weapon == "bow":
                        weapon_modifier = "dexterity"
                    elif "sword" in self.weapon or "axe" in self.weapon:
                        weapon_modifier = "strength"
                    else:
                        weapon_modifier = "intelligence"

                    if weapon_modifier == "strength":
                        modifier = self.strength
                    elif weapon_modifier == "dexterity":
                        modifier = self.dexterity
                    elif weapon_modifier == "intelligence":
                        modifier = self.intelligence
                    else:
                        modifier = 0
                    print_debug_message("DEBUG: Player - player_attack - self.weapon - weapon_modifier = "+str(weapon_modifier))
                    weapon_attack = random.randint(weapon_type[self.weapon].min_damage, weapon_type[self.weapon].max_damage)
                    print_debug_message("DEBUG: Player - player_attack - self.weapon - weapon_attack = "+str(weapon_attack))
                    weapon_attack += modifier
                    return weapon_attack, weapon_used

class Enemy:
    def __init__(self, enemy_type, health, weapon, strength, endurance, dexterity, intelligence, wisdom, charisma, gold, xp_points):
        self.enemy_type = enemy_type
        self.health = health
        self.weapon =weapon
        self.strength = strength
        self.endurance = endurance
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.gold = gold
        self.xp = xp_points
        self.inventory = {}

    @classmethod
    def gen_random_enemy(cls, enemy_info):
        enemy_type = random.choice(list(enemy_info.keys()))
        enemy_data = enemy_info[enemy_type]
        health = enemy_data[1]
        return cls(enemy_type, health, *enemy_data[2:])

    def loot_drop(self):
        if self.health <= 0:
            loot = {'weapon': self.weapon}
            for item, amount in self.inventory.items():
                loot[item] = amount
            return loot
        else:
            return None

    def add_to_inventory(self, item, amount):
        if item in self.inventory:
            self.inventory[item] += amount
        else:
            self.inventory[item] = amount

    def enemy_attack(self):

        if self.weapon == "bow":
            weapon_modifier = "dexterity"
        elif "sword" is self.weapon or "axe" in self.weapon:
            weapon_modifier = "strength"
        else:
            weapon_modifier = "intelligence"

        if weapon_modifier == "strength":
            modifier = self.strength
        elif weapon_modifier == "dexterity":
            modifier = self.dexterity
        elif weapon_modifier == "intelligence":
            modifier = self.intelligence
        else:
            modifier = 0
        weapon_attack = random.randint(weapon_type[self.weapon].min_damage, weapon_type[self.weapon].max_damage)
        weapon_attack += modifier
        print(Fore.RED, f"The {self.enemy_type} attacks with {self.weapon}")
        print(f"{self.weapon} does {weapon_attack} damage" + Style.RESET_ALL)
        print_debug_message("DEBUG: class:weapon func_attack attack = " + str(weapon_attack))
        return weapon_attack

class Weapon:
    def __init__(self, weapon_type, min_damage, max_damage, weapon_stat_mod, weapon_value,):
        self.weapon_type         = weapon_type
        self.min_damage          = min_damage
        self.max_damage          = max_damage
        self.weapon_stat_mod     = weapon_stat_mod
        self.weapon_value        = weapon_value
        self.weapon_user         = self

class Spells:
    def __init__(self, spell_name, min_damage, max_damage, spell_stat_mod, health_cost):
        self.spell_name     = spell_name
        self.min_damage     = min_damage
        self.max_damage     = max_damage
        self.spell_stat_mod = spell_stat_mod
        self.health_cost    = health_cost

    def use(self, user, target,):
        spell = spell_type.get(self)
        # spell = getattr(self, "spell_types", None)
        print_debug_message("DEBUG: Spell use Spell = " + str(self))
        print_debug_message("DEBUG: Spell use health_cost = " + str(spell.health_cost))
        if user.health < spell.health_cost:
            print(f"{user.name} does not have enough health to use {self}")
            return None
        else:
            Spells.attack(spell, user, target)


def print_debug_message(message):
    if message.startswith("DEBUG:"):
        print(Fore.GREEN + message + Style.RESET_ALL)
    else:
        print(message)

def print_error_message(message):
    if message.startswith("ERROR:"):
        print(Fore.RED + message + Style.RESET_ALL)
    else:
        print(message)



weapon_type = {
    "sword": Weapon("sword", min_damage =1, max_damage =6, weapon_stat_mod="strength", weapon_value= 10,),
    "axe": Weapon("axe", min_damage=1,max_damage=9, weapon_stat_mod="strength",weapon_value=10),
    "bow": Weapon("bow", min_damage=1, max_damage=10, weapon_stat_mod="dexterity", weapon_value=10),
    "wand": Weapon("wand", min_damage=1, max_damage=7, weapon_stat_mod="intelligence", weapon_value=10)
}

spell_type = {
    "fire whip": Spells("fire whip", min_damage =4, max_damage =6, spell_stat_mod = "intelligence", health_cost = 2),
    "lightning shock": Spells("lightning shock", min_damage=5,max_damage=9, spell_stat_mod = "intelligence", health_cost = 4),
    "ground shake": Spells("ground shake", min_damage=1, max_damage=10, spell_stat_mod = "intelligence", health_cost = 6),
    "poison sling": Spells("poison sling", min_damage=1, max_damage=7, spell_stat_mod = "intelligence", health_cost = 3)
}


enemy_info = {
    "cave goblin" : ( "cave goblin", random.randint(6,6), random.choice(list(weapon_type.keys())), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(-1,0), random.randint(0,1), random.randint(-2,0), random.randint(0,3), 50),
    "forrest goblin" : ("forrest goblin", random.randint(4,6), random.choice(list(weapon_type.keys())), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(-1,0), random.randint(0,1), random.randint(-2,0), random.randint(0,3), 50)
}


def combat(player, enemy,):
    round_num = 1
    target = enemy
    attack_choice = None
    while player.health > 0 and enemy1.health > 0:
        print(f"Round {round_num}")
        print_debug_message(f"DEBUG: {enemy1.enemy_type} has a {enemy1.weapon}")
        print(f"{player.name} has {player.health} health left")
        print(f"{enemy1.enemy_type} has {enemy1.health} health left\n")
        input("Press Enter to continue...")
        player_iniative = random.randint(0,20) + player.dexterity
        enemy_iniative = random.randint (0,20) + enemy1.dexterity
        player_iniative = 20
        enemy_iniative = 1
        if player_iniative > enemy_iniative:
            Player.player_combat_loop(player,enemy)
           

        else:
            Enemy.attack(player)
            
        player_attack_damage = 0    
        player_attack_damage = Player.player_combat_loop[player_attack_damage]
        print(f"{Fore.GREEN}The {enemy.enemy_type} has got " + str(max(enemy.health - player_attack_damage, 0)) + f" health left!{Style.RESET_ALL}")
        enemy.health -= player_attack_damage
        player.weapon = None
        if enemy.health <= 0:
            enemy.health = 0
            print(Fore.GREEN, f"You have defeated the {enemy.enemy_type}!" + Style.RESET_ALL)
            break
        enemy_damage = enemy.enemy_attack()
        player.health -= enemy_damage
        input("Press Enter to continue...")
        round_num += 1
    if player.health <= 0:
        print("Game Over - You lose!")
    else:
        print("You won the battle!")

# enemy1 = enemy.gen_random_enemy(enemy_info)
# enemy2 = enemy.gen_random_enemy(enemy_info)
# enemy3 = enemy.gen_random_enemy(enemy_info)
# enemy4 = enemy.gen_random_enemy(enemy_info)

player = Player("John", 100, 3, 1, 4, 2, 1, 2, {}, 30, 8, 10, 1)

#

# First fight
print("Fight 1:")
enemy1 = Enemy.gen_random_enemy(enemy_info)
combat(player, enemy1)

# Second fight
print("Fight 2:")
enemy2 = Enemy.gen_random_enemy(enemy_info)
combat(player, enemy2)

# Third fight
print("Fight 3:")
enemy3 = Enemy.gen_random_enemy(enemy_info)
combat(player, enemy3)

print("Game Over - You won all the fights!")


#player_weapon = Weapon("sword", 1, 6, "strength", 10, user=player)
# enemy_weapon = weapon("axe", 1, 9, "strength", 10, user=enemy)

# player.attack()
# enemy.enemy_weapon.attack()

import random
from colorama import Fore, Style
import time
import sys
import textwrap
import shutil
import msvcrt
import os
import pickle
from tkinter import filedialog
import tkinter as tk
import csv  
import itertools
from spells import player_spells

#######################################
#                                     #
#               Classes               #
#                                     #
#######################################

class Game:
    def __init__(self, player_name, player_health, player_strength, player_endurance, player_dexterity, player_intelligence, player_wisdom, player_charisma, player_gold, player_armour, player_xp_points, player_level):
        self.player_character = self.Player(player_name, player_health, player_strength, player_endurance, player_dexterity, player_intelligence, player_wisdom, player_charisma, player_gold, player_armour, player_xp_points, player_level)
        self.player_location = "main cave hub"
        end_location = "Bleak Falls Village"

    class Weapon:
        """ class Weapon
        This class, Weapon, represents a weapon object with attributes such as the name
        of the weapon, minimum and maximum damage that the weapon can inflict, a weapon
        stat modifier and the value of the weapon.

        The init method initializes the instance of the Weapon class with the
        aforementioned attributes. The 'weapon_name' attribute is a string that
        represents the name of the weapon. The 'min_damage' attribute is an integer that
        denotes the minimum damage that the weapon can inflict. The 'max_damage'
        attribute is an integer that denotes the maximum damage that the weapon can
        inflict. The 'weapon_stat_mod' attribute is a float that represents a modifier
        for the weapon's statistics. Finally, the 'weapon_value' attribute is an integer
        that denotes the value of the weapon.

        This class can be used to create multiple weapon objects with different
        attribute values. These objects can be used in a variety of applications such as
        games and simulations that require weapon objects.
        """
        def __init__(self,weapon_name, min_damage, max_damage, weapon_stat_mod, weapon_value):
            self.weapon_name     = weapon_name
            self.min_damage      = min_damage
            self.max_damage      = max_damage
            self.weapon_stat_mod = weapon_stat_mod
            self.weapon_value    = weapon_value

    class Spells:
        """ class Spells
        This class represents a spell object, which has various attributes such as spell
        name, minimum and maximum damage, spell stat modifier, and health cost. The
        init() function is used to initialize the spell object with the provided values
        for the attributes. Parameters:
            - spell_name: The name of the spell. 
            - min_damage: The minimum amount of damage the spell can cause. 
            - max_damage: Themaximum amount of damage the spell can cause. 
            - spell_stat_mod: The modifier that affects the spell's effectiveness, 
            such as intelligence or strength. 
            - health_cost: The amount of health that the caster loses when using the spell.

        Once the object is created, these attributes can be accessed using the dot
        notation. For example, to access the name of a spell object named "fireball",
        you would write fireball.spell_name. Overall, this class is useful for creating
        and managing spells in a role-playing game or other similar applications.
        """

        def __init__(self, spell_name, spell_description, spell_damage ,spell_stat_mod, spell_health_cost):
            self.spell_name     = spell_name
            self.description    = spell_description
            self.spell_damage   = spell_damage
            self.spell_stat_mod = spell_stat_mod
            self.health_cost    = spell_health_cost

        def cast(self, target):
            damage = random.randint(*self.damage_range)
            health_cost = random.randint(*self.health_cost_range)

            target.health -= damage
            self.owner.health -= health_cost

            return damage, health_cost


 
    class Combat_loop:

        class Enemy:
                def __init__(self,enemy_name, enemy_health, enemy_min_damage, enemy_max_damage, enemy_strength, enemy_endurance, enemy_dexterity,enemy_intelligence,enemy_wisdom,enemy_charisma,enemy_gold, enemy_armour,enemy_xp_points, enemy_loot_drop ):
                    self.enemy_name         = enemy_name
                    self.enemy_health       = enemy_health
                    self.enemy_min_damage   = enemy_min_damage
                    self.enemy_max_damage   = enemy_max_damage
                    self.enemy_strength     = enemy_strength
                    self.enemy_endurance    = enemy_endurance
                    self.enemy_dexterity    = enemy_dexterity
                    self.enemy_intelligence = enemy_intelligence
                    self.enemy_wisdom       = enemy_wisdom
                    self.enemy_charisma     = enemy_charisma
                    self.enemy_gold         = enemy_gold
                    self.enemy_armour       = enemy_armour
                    self.enemy_xp_points    = enemy_xp_points
                    self.enemy_loot_drop    = enemy_loot_drop
                    self.enemy_spells       = [Bleak_falls.Spells(**spells[spell_name]) for spell_name in spells]


        def __init__(self, player):
            self.player = player
            self.player_location = player.player_location


        def enemy_creation(self):
            enemies = locations[self.player_location]["enemies"]
            enemy_list = []
            with open('enemy_type.csv', newline='') as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=[
                    'enemy_name',
                    'enemy_health',
                    'enemy_min_damage',
                    'enemy_max_damage',
                    'enemy_strength',
                    'enemy_endurance',
                    'enemy_dexterity',
                    'enemy_intelligence',
                    'enemy_wisdom',
                    'enemy_charisma',
                    'enemy_gold',
                    'enemy_armour',
                    'enemy_xp_points',
                    'enemy_loot_drop'
                ])
                counter = itertools.count(start=1)
                for row in reader:
                    if row['enemy_name'] in enemies:
                        name = f"{row['enemy_name']} {next(counter)}"
                        enemy = self.Enemy(
                            name,
                            int(row['enemy_health']),
                            int(row['enemy_min_damage']),
                            int(row['enemy_max_damage']),
                            int(row['enemy_strength']),
                            int(row['enemy_endurance']),
                            int(row['enemy_dexterity']),
                            int(row['enemy_intelligence']),
                            int(row['enemy_wisdom']),
                            int(row['enemy_charisma']),
                            int(row['enemy_gold']),
                            int(row['enemy_armour']),
                            int(row['enemy_xp_points']),
                            row['enemy_loot_drop']
                        )
                        enemy_list.append(enemy)
            return enemy_list

        # def combat(self):
        #     location = self.player_location
        #     enemies_in_location = location["enemies"]
        #     enemy_list = self.enemy_creation()
        #     print_debug_message("DEBUG: Game - combat_loop - enemy_list:{}".format(str(list(enemy_list.keys))))

        #     while len(enemy_list) > 0:
        #         fight_num = 1
        #         round_num = 1
        #         for enemy_chosen in enemy_list:
        #             print(f"Fight {fight_num}")
        #             while player_character.player_health > 0 and enemy_chosen.enemy_health > 0:
        #                 print(f"Round {round_num}")
        #                 print_debug_message(f"DEBUG: {enemy_chosen.enemy_name} has a {enemy_chosen.enemy_weapon}")
        #                 print(f"{player_character.player_name} has {player_character.player_health} health left")
        #                 print(f"{enemy_chosen.enemy_name} has {enemy_chosen.enemy_health} health left\n")
        #                 input("Press Enter to continue...")
        #                 player_iniative = random.randint(0,20) + player_character.player_dexterity
        #                 enemy_iniative = random.randint (0,20) + enemy_chosen.enemy_dexterity
        #                 if player_iniative > enemy_iniative:
        #                     player_attack_choice = input("How would you like to to attack?\nWith Magic or a Weapon?").lower().split()
        #                     if "magic" in player_attack_choice:
        #                         player_character.player_spell_attack(player_character,enemy_chosen)
        #                         enemy_chosen.enemy_health -= player_character.player_spell_damage 
                            
        #                 elif enemy_iniative > player_iniative:
                            
                    
        #             # Check if the player defeated the enemy
        #             if enemy_chosen.health <= 0:
        #                 print(f"You defeated {enemy_chosen.enemy_name}!")
        #                 enemy_list.remove(enemy_chosen)
        #                 input("Press Enter to continue...")
        #                 continue

        #             # If the enemy defeated the player, end the combat
        #             if player_character.health <= 0:
        #                 print("You have been defeated!")
        #                 input("Press Enter to continue...")
        #                 return
                    
        #     print("You have defeated all enemies!")
        #     input("Press Enter to continue...")

    class Player:
        """ class Player
        This class, Player, represents a player object with various attributes such as
        name, health, strength, endurance, dexterity, intelligence, wisdom, charisma,
        gold, armour, experience points (XP), and level. It also includes several
        methods to handle different aspects of the player object.

        The init method initializes the instance of the Player class with the
        aforementioned attributes. The 'player_name' attribute is a string that
        represents the name of the player. The 'player_health' attribute is an integer
        that denotes the current health of the player. The 'player_strength',
        'player_endurance', 'player_dexterity', 'player_intelligence', 'player_wisdom',
        and 'player_charisma' attributes are integers that represent the corresponding
        statistics of the player. The 'player_gold' attribute is an integer that denotes
        the amount of gold that the player has. The 'player_armour' attribute is an
        integer that represents the level of protection provided by the player's armour.
        The 'player_xp_points' attribute is an integer that denotes the amount of
        experience points that the player has. The 'player_level' attribute is an
        integer that denotes the current level of the player. The 'player_xp_to_level'
        attribute is an integer that represents the amount of experience points required
        for the player to level up. The 'player_xp_incra' attribute is an integer that
        represents the increment in experience points required for each level up.

        The class includes several methods that handle different aspects of the player
        object. The 'player_move' method is a placeholder for any movement-related
        actions that the player can take. The 'player_level_up' method is responsible
        for increasing the player's level and modifying the player's attributes
        accordingly. The 'player_armour_calc' method calculates the player's armor
        rating based on their equipped armor. The 'player_combat_loop' method is a
        placeholder for any combat-related actions that the player can take. The
        'player_weapon_attack' and 'player_spell_attack' methods handle attacks using
        the player's weapon and spells, respectively.

        This class can be used to create multiple player objects with different
        attribute values. These objects can be used in a variety of applications such as
        games and simulations that require player objects.
        """
    
        def __init__(self, player_name, player_health, player_strength, player_endurance, player_dexterity, player_intelligence, player_wisdom, player_charisma, player_gold, player_armour, player_xp_points, player_level, Bleak_falls):
            self.player_name         = player_name
            self.player_health       = player_health
            self.player_strength     = player_strength
            self.player_endurance    = player_endurance
            self.player_dexterity    = player_dexterity
            self.player_intelligence = player_intelligence
            self.player_wisdom       = player_wisdom
            self.player_charisma     = player_charisma
            self.player_gold         = player_gold
            self.player_armour       = player_armour
            self.player_xp_points    = player_xp_points
            self.player_level        = player_level
            self.player_xp_incra     = 100
            self.player_xp_to_level  = 100
            self.player_spells       = [Bleak_falls.Spells(**spells[spell_name]) for spell_name in spells]
        #==========// Player Creation functions \\==========#

        def get_player_stats(self):
            return {
                'player_name': self.player_name,
                'player_health': self.player_health,
                'player_strength': self.player_strength,
                'player_endurance': self.player_endurance,
                'player_dexterity': self.player_dexterity,
                'player_intelligence': self.player_intelligence,
                'player_wisdom': self.player_wisdom,
                'player_charisma': self.player_charisma,
                'player_gold': self.player_gold,
                'player_armour': self.player_armour,
                'player_xp_points': self.player_xp_points,
                'player_level': self.player_level
            }
            
        def update_stats(self, player_class):
            if "blacksmith" in player_class:
                self.player_health = player_class["blacksmith"][1]
                self.player_strength = player_class["blacksmith"][2]
                self.player_endurance = player_class["blacksmith"][3]
                self.player_dexterity = player_class["blacksmith"][4]
                self.player_intelligence = player_class["blacksmith"][5]
                self.player_wisdom = player_class["blacksmith"][6]
                self.player_charisma = player_class["blacksmith"][7]
                self.player_gold = player_class["blacksmith"][8]
                self.player_armour = player_class["blacksmith"][9]
                self.player_xp_points = player_class["blacksmith"][10]
                self.player_level = player_class["blacksmith"][11]
            elif "hunter" in player_class:
                self.player_health = player_class["hunter"][1]
                self.player_strength = player_class["hunter"][2]
                self.player_endurance = player_class["hunter"][3]
                self.player_dexterity = player_class["hunter"][4]
                self.player_intelligence = player_class["hunter"][5]
                self.player_wisdom = player_class["hunter"][6]
                self.player_charisma = player_class["hunter"][7]
                self.player_gold = player_class["hunter"][8]
                self.player_armour = player_class["hunter"][9]
                self.player_xp_points = player_class["hunter"][10]
                self.player_level = player_class["hunter"][11]
            elif "student" in player_class:
                self.player_health = player_class["student"][1]
                self.player_strength = player_class["student"][2]
                self.player_endurance = player_class["student"][3]
                self.player_dexterity = player_class["student"][4]
                self.player_intelligence = player_class["student"][5]
                self.player_wisdom = player_class["student"][6]
                self.player_charisma = player_class["student"][7]
                self.player_gold = player_class["student"][8]
                self.player_armour = player_class["student"][9]
                self.player_xp_points = player_class["student"][10]
                self.player_level = player_class["student"][11]


        #==========// Player Movement Functions \\==========#

        def player_move():
            return

        #==========// Player Combat Functions \\==========#    

        def player_get_xp(self, player_gained_xp):
            self.player_xp_points += player_gained_xp
            self.player_level_up()

        def player_level_up(self):
            print_debug_message(f"DEBUG: Player.player_level_up - player_xp_points:{self.player_xp_points} - player_xp_to_level:{self.player_xp_to_level} - player_level:{self.player_level} - player_xp_incra:{self.player_xp_incra}")
            if self.player_xp_points >= self.player_xp_to_level:
                self.player_level += 1
                self.player_xp_points = 0
                self.player_xp_incra += self.player_xp_to_level + self.player_xp_points + ((self.player_level - 2) * self.player_xp_to_level)
                self.player_xp_to_level += self.player_xp_incra
                print_debug_message(f"DEBUG: Player.player_level_up - player_xp_points:{self.player_xp_points} - player_xp_to_level:{self.player_xp_to_level} - player_level:{self.player_level} - player_xp_incra:{self.player_xp_incra}")
                self.choose_attributes()

        def choose_attributes(self):
            print("Select two attributes to increase:")
            stats = self.get_player_stats()
            stat_names = ['strength', 'endurance', 'dexterity', 'intelligence', 'wisdom', 'charisma']
            for i, name in enumerate(stat_names):
                print(f"{i+1}. {name}: {stats[f'player_{name}']}")
                
            valid_choices = ["strength", "endurance", "dexterity", "intelligence", "wisdom", "charisma"]
            choice1, choice2 = None, None
                
            while choice1 not in valid_choices:
                choice1 = input("Enter attribute to increase by 1:\n >").lower()

                if choice1 == "strength":
                    self.player_strength += 1
                elif choice1 == "endurance":
                    self.player_endurance += 1
                elif choice1 == "dexterity":
                    self.player_dexterity += 1
                elif choice1 == "intelligence":
                    self.player_intelligence += 1
                elif choice1 == "wisdom":
                    self.player_wisdom += 1
                elif choice1 == "charisma":
                    self.player_charisma += 1
            print("Your {} has been increased by 1 point to {}\n".format(choice1, getattr(Bleak_falls.player_character, "player_"+ choice1)))

            while choice2 not in valid_choices: 
                choice2 = input("Enter attribute to increase by 1:\n >").lower()
                if choice2 == "strength":
                    self.player_strength += 1
                elif choice2 == "endurance":
                    self.player_endurance += 1
                elif choice2 == "dexterity":
                    self.player_dexterity += 1
                elif choice2 == "intelligence":
                    self.player_intelligence += 1
                elif choice2 == "wisdom":
                    self.player_wisdom += 1
                elif choice2 == "charisma":
                    self.player_charisma += 1    
            print("Your {} has been increased by 1 point to {}\n".format(choice2, getattr(Bleak_falls.player_character, "player_"+ choice2)))

        def player_armour_calc():
            return
        def player_weapon_attack():
            return
        def player_spell_attack(player_character, enemy_chosen):
            print("You open up your spell to choose your spell")
            print("You currently know these spells:")
            for i, spells in enumerate(player_character.player_spells):
                print(f"{i+1}. {spells.name}")
            spell_choice = int(input("\nChoose a spell: "))
            spell = player_character.player_spells[spell_choice-1]

            da




            return

        #==========// Player Loot Functions \\==========#

        def add_item(self, item_name, item_quantity=1):
            """
            Adds an item to the player's inventory.

            Args:
                item_name (str): The name of the item to add. 
                item_quantity (int, optional): The quantity of the item to add. Defaults to 1.

            Returns:
                None
            """
            if item_name in self.inventory:
                self.inventory[item_name] += item_quantity
            else:
                self.inventory[item_name] = item_quantity

        def remove_item(self, item_name, item_quantity=1):
            if item_name in self.inventory:
                if self.inventory[item_name] > item_quantity:
                    self.inventory[item_name] -= item_quantity
                else:
                    del self.inventory[item_name]

        def has_item(self, item_name):
            return item_name in self.inventory

        def display_inventory(self):
            if self.inventory:
                print(f"{self.player_name}'s inventory:")
                for item_name, item_quantity in self.inventory:
                    print(f"- {item_name} ({item_quantity})")
            else:
                print(f"{self.player_name}'s inventory is empty.")

        inventory = {
            'sword' : 'The trusted companion for most adventurers, it is lucky you have yours with you',
            'bandages' : 'A staple of any first aid kit, try to make sure you dont need to use them!',
            'gold pieces' : 10
            },
        




    def game_start(self,player_character):
        """ game_start explination
            This function is responsible for starting the game and initializing the player's stats. It takes one argument, Player, which is an instance of the Player class.

            First, it creates a new Player object with default values for all the stats. Then, it prints a description of the game and waits for the player to press the enter button to continue.

            Next, it asks the player to input their name and stores it in the player_name attribute of the Player object.

            Then, it asks the player to choose their profession from a list of three options: Blacksmith, Hunter, or Student. It presents a description of each option and asks the player if they're sure they want to choose that profession.

            If the player confirms their choice, the function sets the player_class_selected variable to the chosen profession and breaks out of the while loop.

            Once the player has chosen their profession, the function sets the player_class variable to a dictionary containing the stats for the chosen profession.

            Finally, it calls the update_stats method of the Player object with the player_class dictionary as an argument to update the player's stats with the chosen profession's stats.

            The function also includes several debug messages to print the player's name and stats for testing purposes.
            """
        
        player_stats = {
        'player_name': '',
        'player_health': 100,
        'player_strength': 10,
        'player_endurance': 10,
        'player_dexterity': 10,
        'player_intelligence': 10,
        'player_wisdom': 10,
        'player_charisma': 10,
        'player_gold': 0,
        'player_armour': None,
        'player_xp_points': 0,
        'player_level': 1
    }

        print_slow(f"{Fore.LIGHTCYAN_EX} In 'Bleak Falls,' you find yourself lost in a treacherous wilderness far from home.\n You have no memory of how you got there or what happened to you, but you know that you must find your way back to your village before it's too late.\n As you journey through the harsh and unforgiving landscape, you soon discover that something sinister is afoot.\n Strange occurrences and ominous signs suggest that there is more to your predicament than meets the eye.\n With danger lurking around every corner and your life hanging in the balance, you must uncover the truth behind the mystery of Bleak Falls before it's too late.\n {Style.RESET_ALL}")
        input("\nPress enter button to continue....")
        while player_character.player_name is '':
            print_slow(f"{Fore.GREEN}Welcome Adventurer!\n What is your name?{Style.RESET_ALL}")
            player_character.player_name = input("\n> ")
        print_debug_message(f"DEBUG: game_start - Player = {player_character.player_name}")
        player_class_selected = False
        while player_class_selected == False:
            print_slow(f"What is your profession?\n Blacksmith, Hunter, or Student?")
            player_class_select = input("\n>").lower()
            if player_class_select == "blacksmith":
                print_slow("Long days working the forge has shaped your body into a tool.\n Stronger and more hardy than the average man, you find the best way to solve a problem is to get a bigger hammer.\n Are you sure this is your profession?")
                player_input = input("\n>").lower()
                if player_input == "yes":
                    print_slow(f"Lets get you back the forge then {player_character.player_name}!")
                    player_class_selected = "blacksmith"
                    break
            if player_class_select == "hunter":
                print_slow("Patience and practice are your best traits. Spending long days waiting for the perfect shot means you cant afford to miss.\n Your mastery of the boy has made you quick and nimble.\n Are you sure this is your profession?")
                player_input = input("\n>").lower()
                if player_input == "yes":
                    print_slow(f"Its time to get back to the hunt then {player_character.player_name}!")
                    player_class_selected = "hunter"
                    break
            if player_class_select == "student":
                print_slow("Unlike most people in your village you've always been fascinated in how the world works.\n When you became of age you began studying with the closest scholar to your village, learning as much as you can.\n Are you sure this is your profession?")
                player_input = input("\n>").lower()
                if player_input == "yes":
                    print_slow(f"Knowledge waits for no man, it's time to continue your studies {player_character.player_name}!")
                    player_class_selected = "student"
                    break
        if player_class_selected == "blacksmith":
            player_class = {"blacksmith": (player_character.player_name, 15, 3, 3, 0, -1, -1, 0, 0, 0, 0, 1)}
        if player_class_selected == "hunter":
            player_class = {"hunter": (player_character.player_name, 13,  0,  0, 3, 0, 0, 2, 0, 0, 0, 1)}
        if player_class_selected == "student":
            player_class = {"student": (player_character.player_name, 10,  -1,  -1, -1, 3, 3, 0, 0, 0, 0, 1)}
        player_character.update_stats(player_class)    
        print_debug_message(f"DEBUG: game_start - Player stats = {player_character.get_player_stats()}")
        self.player_character = player_character
        input("\nPress any buttone to continue")
        self.player_current_location()
        
    def press_continue(self):
        input("Press any button to continue.....")

    def player_current_location(self):
        """ player_current_location explanation
        Displays information about the player's current location, including
        its description, enemies, and loot (if any). If there are enemies
        present, initiates the combat loop. After displaying the information,
        prompts the player for a movement choice using the player_movement
        method.
        """
        if self.player_location == "Bleak Falls Village":
            self.end_game()
        location = locations[self.player_location]
        description = location["description"]
        print_slow(description)
        if "enemies" in location:
            enemies = location["enemies"]
            if enemies is not None:
                print("\nThere are {} enemies in this location! Prepare to fight!".format(len(list(enemies))))
                input("Press any button to continue.....")
                self.Combat_loop()

        if "loot" in location:
            loot = location["loot"]
            if loot is not None:
                print("\nLooking around you see {}").format(str(loot))
        
        self.player_movement()

    def player_movement(self):
        """ player_movement explanation
        Moves the player through the locations in the game.

        Args:
        player_location (str): The current location of the player.
        player_current_location (str): The location where the player started.

        Returns:
        None
        """
        location = locations[self.player_location]
        description = location["description"]
        exits = location["exits"]
        player_movement_choice = None
        while player_movement_choice is None:
            print("\nYou have {} choices of directions, which way will you go?\n {}".format(len(location["exits"]), list(location["exits"].values())))
            player_movement_choice = input(">").lower().split()
            player_movement_choice_str = " ".join(player_movement_choice)
            for choice in player_movement_choice:
                if choice in exits or player_movement_choice_str in exits:
                    self.player_location = player_movement_choice_str
                    print(f"\nYou have moved to {self.player_location}")
                    input("\nPress any button to continue.....")
                    self.player_current_location()

                if choice not in exits or player_movement_choice_str not in exits:
                    player_movement_choice = None
                    player_movement_choice_str = None
                    print(f"\n{Fore.RED}Choice is not a valid exit location, please choose again.{Style.RESET_ALL}")
                    break
                else:
                    if player_movement_choice is None:
                        print(f"\n{Fore.RED}Choice is not a valid exit location, please choose again.{Style.RESET_ALL}")
                        break

    def start_combat(self):
        location = locations[self.player_location]
        enemies = location["enemies"]
        enemies_info = enemy_info
        while enemies is not None:
                self.Combat_loop.combat()
                
    def save_game(self,):
        # get the file path from the user
        file_path = filedialog.asksaveasfilename(defaultextension=".sav")
        # if the user didn't cancel the dialog box
        if file_path:
            # save the file
            with open(file_path, "wb") as f:
                pickle.dump(self.__dict__, f)

    def load_game(self, ):
        with open('wb') as f:
            state = pickle.load(f)
        self.__dict__.update(state)

Bleak_falls = Game("",0,0,0,0,0,0,0,0,0,0,1)
player_character = Bleak_falls.Player()


#######################################
#                                     #
#             Functions               #
#                                     #
#######################################


def print_slow(message):
    """
    Print a message to the terminal one character at a time, with a delay of
    0.05 seconds between each character. The function wraps long lines to fit
    the terminal width, and clears the screen before printing. If the user
    presses a key during the printing, the function stops and waits for the user
    to press another key.

    Parameters   : message (str): The message to be printed.

    Returns: None
    """
    terminal_width = shutil.get_terminal_size((80,20)).columns
    wrapped_text = textwrap.wrap(message, width=terminal_width, break_long_words=True)
    stop = False
    for line in wrapped_text:
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
            if msvcrt.kbhit():  
                stop = True
                msvcrt.getch()                
                break
        if stop == True:
            sys.stdout.write("\n".join(wrapped_text))
            return
        sys.stdout.write("\n")
        sys.stdout.flush()
       
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

def game_start(player_character):
        """ game_start explination
            This function is responsible for starting the game and initializing the player's stats. It takes one argument, Player, which is an instance of the Player class.

            First, it creates a new Player object with default values for all the stats. Then, it prints a description of the game and waits for the player to press the enter button to continue.

            Next, it asks the player to input their name and stores it in the player_name attribute of the Player object.

            Then, it asks the player to choose their profession from a list of three options: Blacksmith, Hunter, or Student. It presents a description of each option and asks the player if they're sure they want to choose that profession.

            If the player confirms their choice, the function sets the player_class_selected variable to the chosen profession and breaks out of the while loop.

            Once the player has chosen their profession, the function sets the player_class variable to a dictionary containing the stats for the chosen profession.

            Finally, it calls the update_stats method of the Player object with the player_class dictionary as an argument to update the player's stats with the chosen profession's stats.

            The function also includes several debug messages to print the player's name and stats for testing purposes.
            """
        
        player_stats = {
        'player_name': '',
        'player_health': 100,
        'player_strength': 10,
        'player_endurance': 10,
        'player_dexterity': 10,
        'player_intelligence': 10,
        'player_wisdom': 10,
        'player_charisma': 10,
        'player_gold': 0,
        'player_armour': None,
        'player_xp_points': 0,
        'player_level': 1
    }

        print_slow(f"{Fore.LIGHTCYAN_EX} In 'Bleak Falls,' you find yourself lost in a treacherous wilderness far from home.\n You have no memory of how you got there or what happened to you, but you know that you must find your way back to your village before it's too late.\n As you journey through the harsh and unforgiving landscape, you soon discover that something sinister is afoot.\n Strange occurrences and ominous signs suggest that there is more to your predicament than meets the eye.\n With danger lurking around every corner and your life hanging in the balance, you must uncover the truth behind the mystery of Bleak Falls before it's too late.\n {Style.RESET_ALL}")
        input("\nPress enter button to continue....")
        while player_character.player_name is '':
            print_slow(f"{Fore.GREEN}Welcome Adventurer!\n What is your name?{Style.RESET_ALL}")
            player_character.player_name = input("\n> ")
        print_debug_message(f"DEBUG: game_start - Player = {player_character.player_name}")
        player_class_selected = False
        while player_class_selected == False:
            print_slow(f"What is your profession?\n Blacksmith, Hunter, or Student?")
            player_class_select = input("\n>").lower()
            if player_class_select == "blacksmith":
                print_slow("Long days working the forge has shaped your body into a tool.\n Stronger and more hardy than the average man, you find the best way to solve a problem is to get a bigger hammer.\n Are you sure this is your profession?")
                player_input = input("\n>").lower()
                if player_input == "yes":
                    print_slow(f"Lets get you back the forge then {player_character.player_name}!")
                    player_class_selected = "blacksmith"
                    break
            if player_class_select == "hunter":
                print_slow("Patience and practice are your best traits. Spending long days waiting for the perfect shot means you cant afford to miss.\n Your mastery of the boy has made you quick and nimble.\n Are you sure this is your profession?")
                player_input = input("\n>").lower()
                if player_input == "yes":
                    print_slow(f"Its time to get back to the hunt then {player_character.player_name}!")
                    player_class_selected = "hunter"
                    break
            if player_class_select == "student":
                print_slow("Unlike most people in your village you've always been fascinated in how the world works.\n When you became of age you began studying with the closest scholar to your village, learning as much as you can.\n Are you sure this is your profession?")
                player_input = input("\n>").lower()
                if player_input == "yes":
                    print_slow(f"Knowledge waits for no man, it's time to continue your studies {player_character.player_name}!")
                    player_class_selected = "student"
                    break
        if player_class_selected == "blacksmith":
            player_class = {"blacksmith": (player_character.player_name, 15, 3, 3, 0, -1, -1, 0, 0, 0, 0, 1)}
        if player_class_selected == "hunter":
            player_class = {"hunter": (player_character.player_name, 13,  0,  0, 3, 0, 0, 2, 0, 0, 0, 1)}
        if player_class_selected == "student":
            player_class = {"student": (player_character.player_name, 10,  -1,  -1, -1, 3, 3, 0, 0, 0, 0, 1)}
        player_character.update_stats(player_class)    
        print_debug_message(f"DEBUG: game_start - Player stats = {player_character.get_player_stats()}")
        return player_character
    


#######################################
#                                     #
#             Game Loop               #
#                                     #
#######################################


player_stats = {
    'player_name': 'John Doe',
    'player_health': 100,
    'player_strength': 10,
    'player_endurance': 8,
    'player_dexterity': 12,
    'player_intelligence': 15,
    'player_wisdom': 10,
    'player_charisma': 8,
    'player_gold': 50,
    'player_armour': 5,
    'player_xp_points': 0,
    'player_level': 1
}


#######################################
#                                     #
#           Dictionaries              #
#                                     #
#######################################


""" Weapon_type dictionary:
Each key represents a different type of weapon, with a corresponding Weapon
object as its value. The Weapon object contains various attributes of the
weapon, such as its name, damage range, and stat modifiers. The four types of
weapons included in this dictionary are "sword", "axe", "bow", and "wand".
"""

weapon_type = {
        "sword": Bleak_falls.Weapon("sword", min_damage =1, max_damage =6, weapon_stat_mod="strength", weapon_value= 10,),
        "axe": Bleak_falls.Weapon("axe", min_damage=1,max_damage=9, weapon_stat_mod="strength",weapon_value=10),
        "bow": Bleak_falls.Weapon("bow", min_damage=1, max_damage=10, weapon_stat_mod="dexterity", weapon_value=10),
        "wand": Bleak_falls.Weapon("wand", min_damage=1, max_damage=7, weapon_stat_mod="intelligence", weapon_value=10)
}

""" spell_type Dictionary
The `spell_type` dictionary contains four different spells, each represented by a Spells object. The keys in the dictionary
are the names of the spells, and the values are the corresponding Spells objects. Each Spells object contains information about
the spell, such as its name, minimum and maximum damage, the stat that it is based on (in this case, "intelligence"), and the
health cost of using the spell. This dictionary can be used to look up information about the different types of spells
available to a character in a game or other context.
"""

spells = {
    "fireball": {
        "spell_name": "Embers",
        "spell_description": "A powerful spell that creates a ball of fire and hurls it at the target.",
        "spell_damage": (3, 6), # random integer between 10 and 20
        "spell_stat_mod": "intelligence", # player's attribute to decrease health cost
        "spell_health_cost": (1, 4) # random integer between 5 and 10
    },
    "heal": {
        "spell_name": "Heal",
        "spell_description": "A spell that restores health to the user.",
        "spell_damage": (-5, 0), # spell has a chance to heal target as well
        "spell_stat_mod": "wisdom",
        "spell_health_cost": (-6, -1) # random integer between -6 and -1 (i.e. heals instead of dealing damage)
    },
    "ice_blast": {
        "spell_name": "Ice Blast",
        "Spell_description": "A spell that creates a blast of ice and hurls it at the target.",
        "Spell_damage": (3, 6),
        "spell_stat_mod": "intelligence",
        "spell_health_cost": (1, 4)
    }
}

player_data = {
    'player_name'        : '',
    'player_health'      : 0,
    'player_strength'    : 0,
    'player_endurance'   : 0,
    'player_dexterity'   : 0,
    'player_intelligence': 0,
    'player_wisdom'      : 0,
    'player_charisma'    : 0,
    'player_gold'        : 0,
    'player_armour'      : None,
    'player_xp_points'   : 0,
    'player_level'       : 1
}

enemy_info = {
    "cave goblin" : ("cave goblin", random.randint(4,6), random.choice(list(weapon_type.keys())), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(-1,0), random.randint(0,1), random.randint(-2,0), random.randint(0,3), 50),
    "forrest goblin" : ("forrest goblin", random.randint(4,6), random.choice(list(weapon_type.keys())), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(-1,0), random.randint(0,1), random.randint(-2,0), random.randint(0,3), 50)
}

locations_enemy_description = "some enemies"
locations = {
    "start": {
        "description": "You awake in the pitch black, the sound of dripping water echos around you. The cold hard ground underneath you feels like stone. You reach into your bad and pull out a tourch to light. The flame flickers to life and reveals that you are in a cave. You can see two passage ways out of the area, do you take the one on the right or the left?",
        "exits":{
        "left": "left passageway",
        "right": "right passageway"
        }
    },
    "left passageway":{
        "description": "As you enter the passageway you notice a cool breeze blowing against your face. The walls around you are slick with water and the ground begins to become coated in more and more soil the further along you go. Do you continue or turn around?",
        "exits": {
            "forrest": "forest",
            "starting room": "starting room"
        }
    },
    "right passageway": {
      "description": "You begin to walk down the passageway and notice that the air is becoming more and more stale the further you go. In the distance you swear you can hear the sound of something moving. Do you continue or turn around?",
      "exits": {
          "main cave hub": "main cave hub",
          "starting room": "starting room"
      }  
    },
    "forest": {
        "description": "You see the blinding light of day growing brighter and brighter as you move quickly up the passageway until you finally emerge from the cave. Taking a second to drinkn in your surroundings you find yourself in a dense thick forrest, the sound of wild life can be heard all around. You notice an opening in the tree line straight a head and a climbable tree to the right of you. What do you do?",
        "exits": {
            "forest opening": "forest opening",
            "tree climb": "tree climb",
            "cave return": "cave return"
        }
    },
    "main cave hub": {
        "description": "You step into a gaint canverness room. Water dripping from the ceiling splashes around you as you examine the area. Out of the corner of your eye you spot a green flash dart into the darkness. What do you do?",
        "exits": {
            "goblin chase": "goblin chase",
            "starting room": "starting room"
        }
    },
    "goblin chase": {
        "description": "Not wanting to let the mystery figure escape you begin to chase after it. Running fast through the cave, your foot steps echoing as you go, you begin to gain ground on it. Your blood is thumping in your ears as you turn a corner and finally see the figures cornered in a deadend. You are now face to face with 3 Cave Goblins. What do you do?",
        "exits": {
            "goblin talk": "goblin talk",
            "running away": "running away",
        },
        "enemies": {
            f"cave goblin {i+1}": "cave goblin"
            for i in range(3)
        },
        "end_of_fight": {"goblin fight": "goblin fight"},
        "fight_loot": {},
        "combat": True
    },
    "goblin talk": {
        "description": "The goblin looks afriad and confused. 'Why are you chasing me? leave me alone!'. You are surprised by this. Do you go back to the main room?",
        "exits":{
            "main cave hub": "main cave hub return"
        }
    },
    "goblin fight": {
        "description": "As the goblin snarls you instenctivly reach down and grasb the hilt of your sword. Seeing the danager the goblin lunges at you and manages to plung a dagger into your leg. Feeling a rush of pain you quickly swing your sword with all your might, cleaving the goblins head off. Your leg is badly damaged, you have lost 20 health points. With the goblin defeated what do you do?",
        "exits":{
            "search the goblin": "goblin search",
            "bandage my leg": "leg bandage",
            "main cave hub": "main cave hub return"
        }
    },
    "goblin search": {
        "description": "You look through the pockets of the goblin and only find 2 gold pieces and a few small bones from the goblins last meal. You stand back up and trun around to face the passageway back to big room, you glance down at your bleeding leg. What do you do?",
        "exits": {
            "bandage my leg": "leg bandage",
            "main cave hub": "main cave hub return"
        }
    },
    "leg bandage": {
        "description": "You take your bag off and look for a bandage. Finding one in the front pocket of the bag you take it out and wrap it tightly around your leg. Happy that youve stopped the bleeding you look at the goblin on the floor and passageway back to the main hub. What do you want to do?",
        "exits": {
            "search the goblin": "goblin search",
            "main cave hub": "main cave hub return"
        }
    },
    "main cave hub return": {
        "description": "You manage to make your way back to the large room in the cave. You notice a cool breeze coming from the passageway back to where you woke up. With your back to the passageway that is now the goblins tomb, what do you do?",
        "exits":{
            "return to the goblin": "goblin corpse",
            "follow the breeze": "starting room"
        }
    },
    "goblin corpse":{
        "description": "You go back down the passageway to the goblin's corpse. What do you do?",
        "exits":{
            "search the goblin": "goblin search",
            "main cave hub": "main cave hub return"
        }
    },
    "starting room": {
        "description": "You enter the room where you woke up. You can see two passage ways out of the area, do you take the one on the right or the left?",
        "exits": {
            "right": "main cave hub return",
            "left": "left passageway"
        }
    },
    "testing hall": {
        "description": "You have entered the dev testing hall"
    }
}

Bleak_falls.game_start(player_character)
print_debug_message(f"DEBUG: game_start - Player stats = {player_character.get_player_stats()}")

import random as r
from colorama import Fore, Style
import colorama as c
import time as t
import os
import msvcrt
import time
import customtkinter as ctk

green = Fore.GREEN
red = Fore.RED
rcolour = Style.RESET_ALL

 
"""This class represents a message box with a title and a journal of entries. It uses the CTk library for creating the GUI.

    Attributes:
    system_input (str): The message to be displayed in the message area.
    title (str): The title of the message box.
    journal_entries (list): A list of journal entries to be displayed in the buttons.

    Methods:
    init(self, system_input, title, journal_entries): Initializes the message box and creates the GUI.
    display_entry(self, entry): Displays the selected entry in the message area.
    close_window(self): Destroys the message box GUI.

    Usage:
    To use this class, create an instance of it with the necessary parameters, and then call the mainloop() method on it to display the message box.
    You can then select journal entries to display by clicking on the corresponding buttons.
"""
class Message_box:
    def __init__(self, system_input, title, journal_entries):
        self.system_input = system_input
        self.title = title
        self.journal_entries = journal_entries

        # Set the appearance mode and color theme for the CTk library
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

        # Create a new CTk window and configure its properties
        self.root = ctk.CTk()
        self.root.geometry('800x400')
        self.root.title(self.title)
        self.root.wm_attributes("-topmost", 1)

        # Create a frame within the window and configure its properties
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.pack(pady=20, padx=20, fill='both', expand=True, side='top')

        # Create a text box for displaying messages and configure its properties
        self.message_area = ctk.CTkTextbox(master=self.frame)
        self.message_area.grid(row=0, column=0, sticky='nsew')

        # Create a frame for the journal entry buttons and configure its properties
        self.button_frame = ctk.CTkFrame(master=self.frame)
        self.button_frame.grid(row=1, column=0, pady=10)

        # Create buttons for each journal entry and add them to the button frame
        self.buttons = []
        # Create a button with the entry's text and a command to display that entry
        for i, entry in enumerate(self.journal_entries):
            button_text = f"Entry {i+1}"
            button = ctk.CTkButton(master=self.button_frame, text=button_text, command=lambda e=entry: self.display_entry(e))
            button.grid(row=0, column=i, padx=5)
            self.buttons.append(button)
            
        # Insert the system input message into the message area
        self.message_area.insert('0.0', self.system_input)
        self.message_area.configure(state='disabled', wrap='word')

        # Create a close button and add it to the frame
        self.close_button = ctk.CTkButton(master=self.frame, text='Close', command=self.close_window)
        self.close_button.grid(row=2, column=0, pady=10)

        # Start the main loop for the CTk window
        self.root.mainloop()

    # Display the selected journal entry in the message area
    def display_entry(self, entry):
        self.message_area.configure(state='normal')
        self.message_area.delete('1.0', 'end')
        self.message_area.insert('0.0', entry)
        self.message_area.configure(state='disabled', wrap='word')

    # Destroy the CTk window
    def close_window(self):
        self.root.destroy()


def print_debug_message(message):
    print(green + 'DEBUG:' + message + rcolour)


def print_error_message(message):
    if message.startswith("ERROR:"):
        print(Fore.RED + message + Style.RESET_ALL)
    else:
        print(message)


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
    # Print message
    # Check if the message is a dictionary
    if isinstance(message, dict):
        # If it is, join the dictionary keys into a single string
        message = ''.join(message)

    # Split the message into sentences using the period as the delimiter
    sentences = message.split('.')

    # Initialize the stop flag and time delay
    stop = False
    t = 0.05

    # Iterate through each sentence in the list of sentences
    for sentence in sentences:
        # Iterate through each character in the current sentence
        for char in sentence:
            # Print the character without a newline and flush the output buffer
            print(char, end='', flush=True)
            # Increment the printed characters counter
            printed_chars += 1
            # Sleep for the specified time delay
            time.sleep(t)
            # Check if a key was pressed
            if msvcrt.kbhit():
                # If a key was pressed, set the stop flag to True
                stop = True
                # Retrieve the pressed key
                msvcrt.getch()
                # Set the time delay to 0
                t = 0
        # Print a newline character after printing all characters in the sentence
        else:
            print()


class Player_character:
    def __init__(self, player_name, player_health, player_class, player_strength, player_endurance, player_dexterity, player_intelligence, player_wisdom, player_charisma, player_gold, player_level, player_xp, player_location, player_inv):
        self.player_name = player_name
        self.player_health = player_health
        self.player_class = player_class
        self.player_strength = player_strength
        self.player_endurance = player_endurance
        self.player_dexterity = player_dexterity
        self.player_intelligence = player_intelligence
        self.player_wisom = player_wisdom
        self.player_charisma = player_charisma
        self.player_gold = player_gold
        self.player_level = player_level
        self.player_xp = player_xp
        self.player_inv = {}
        self.player_weapons = player_weapon_type
        self.player_location = 'start'

   # def weapon_skill_add_exp(self):

    def weapon_skill_level(self):
        levels = self.player_weapon_skills['weapon skill levels']
        experiance = self.player_weapon_skills['weapon skill experience']
        while True:
            for skill in experiance:
                for weapon, exp_range in experiance[skill].items():
                    if exp_range[0] > exp_range[1]:
                        levels[skill][weapon] += 1
                        exp_range[0] = 0
                        exp_range[1] += 100
                    else:
                        experiance[skill][weapon] = (
                            exp_range[0]+1, exp_range[1]+1)
            break

    def weapon_attack(self):
        # print_debug_message('DEBUG:', str(list(player_weapon_type.keys())))
        weapon_choice = None
        while weapon_choice == None:
            print_slow(
                f'Please select one of your weapons to attack with\n{list(player_weapon_type.keys())}')
            weapon_choice = input('\n>')
            if weapon_choice in player_weapon_type:
                weapon_choice = list(player_weapon_type[weapon_choice])
                # print_debug_message(f'DEBUG: weapon_choice = {weapon_choice}')
                weapon_selected = Weapon(*weapon_choice)
                weapon_type = weapon_selected.weapon_type
                weapon_skill = weapon_selected.weapon_skill
                # Asign weapon skill stats to variables
                pws = player_weapon_skills["weapon skill experience"][weapon_type][weapon_skill]
                pwsd = player_weapon_skills["weapon skill levels"][weapon_type][weapon_skill]
                print_debug_message(
                    f'DEBUG: weapon selected sweapon skill = {player_weapon_skills["weapon skill experience"][weapon_type][weapon_skill]}')
                pws[0] += 20
                if pws[0] > pws[1]:
                    self.weapon_skill_level()
                print_debug_message(
                    f'DEBUG: weapon selected sweapon skill = {player_weapon_skills["weapon skill experience"][weapon_type][weapon_skill]}')
                # print_debug_message(f'DEBUG: weapon_selected = {weapon_selected}')
                weapon_damage = r.randint(
                    weapon_selected.weapon_min, weapon_selected.weapon_max)
                # print_debug_message(f'DEBUG: {weapon_selected.getatt()}')
                damage_mod = weapon_selected.weapon_stat_mod
                damage_mod = 'player_'+damage_mod
                damage_mod = getattr(self, damage_mod)
                # print_debug_message(f'DEBUG: damage mod = {damage_mod}')
                weapon_damage = (weapon_damage + damage_mod + pwsd)
                return weapon_damage, weapon_selected.weapon_name
            else:
                weapon_choice = None

    def spell_attack(self):
        spell_choice = None
        while spell_choice == None:
            # print_debug_message(f"player_spells =  {list(player_spells.keys())}")
            spell_choice = input(
                f"You open your book of spells:\n{str(list(player_spells.keys()))}\nPlease select a spell to use!\n>")
            # print_debug_message(f'spell_choice = {spell_choice}')
            if spell_choice in player_spells:
                spell_choice = list(player_spells[spell_choice].values())
                # print_debug_message(f'spell_choice = {spell_choice}')
                spell_choice = Spell(*spell_choice)
                # print_debug_message(f'spell_choice = {spell_choice}')
                spell_damage = r.randint(*spell_choice.spell_damage)
                # print_debug_message(f'spell_damage = {spell_damage}')
                health_damage = r.randint(*spell_choice.health_cost)
                # print_debug_message(f'health_damage = {health_damage}')
                return spell_damage, health_damage
            else:
                print('select another spell dumbass')
                spell_choice = None

    # def skill_level(self):


class Enemy:
    """
    A class to represent an enemy in a role-playing game.

    Attributes:
    -----------
    enemy_name : str
        The name of the enemy.
    enemy_description : str
        A description of the enemy.
    enemy_health : int
        The amount of health the enemy has.
    enemy_strength : int
        The enemy's strength attribute.
    enemy_endurance : int
        The enemy's endurance attribute.
    enemy_dexterity : int
        The enemy's dexterity attribute.
    enemy_intelligence : int
        The enemy's intelligence attribute.
    enemy_wisdom : int
        The enemy's wisdom attribute.
    enemy_charisma : int
        The enemy's charisma attribute.
    enemy_weapon : str
        The weapon the enemy is using.
    enemy_weapon_type : str
        The type of weapon the enemy is using (e.g. "goblin_weapons", "orc_weapons", etc.).
    enemy_gold : int
        The amount of gold the enemy is carrying.
    enemy_xp : int
        The amount of experience points the enemy is worth.

    Methods:
    --------
    gen_random_enemy(enemy):
        Generates a random enemy based on the given enemy type.

        Parameters:
        -----------
        enemy : str
            The type of enemy to generate. Valid options are "cave goblin", "forrest goblin", "Orc Warrior",
            "Orc Shaman", "Orc Archer", "Orc Berserker", "Zombie", and "Skeleton".

        Returns:
        --------
        enemy : Enemy
            A new instance of the Enemy class representing the generated enemy.
    """
    def __init__(self, enemy_name, enemy_description, enemy_health, enemy_strength, enemy_endurance, enemy_dexterity, enemy_intelligence, enemy_wisdom, enemy_charisma, enemy_weapon, enemy_weapon_type, enemy_gold, enemy_xp):
        self.enemy_name = enemy_name
        self.enemy_description = enemy_description
        self.enemy_health = enemy_health
        self.enemy_strength = enemy_strength
        self.enemy_endurance = enemy_endurance
        self.enemy_dexterity = enemy_dexterity
        self.enemy_intelligence = enemy_intelligence
        self.enemy_wisdom = enemy_wisdom
        self.enemy_charisma = enemy_charisma
        self.enemy_weapon = enemy_weapon
        self.enemy_weapon_type = enemy_weapon_type
        self.enemy_gold = enemy_gold
        self.enemy_xp = enemy_xp

    def gen_random_enemy(enemy):
        enemy_info = {
            'goblin types': {
                "cave goblin": ("cave goblin", 'A small greyish creature, half the height of the average man. It could be mistaken for child if it wasnt for the large pointed ears and sharp fang like teeth', r.randint(4, 6), r.randint(0, 1), r.randint(0, 1), r.randint(0, 1), r.randint(-1, 0), r.randint(0, 1), r.randint(-2, 0), r.choice(list(enemy_weapon_type["goblin_weapons"].keys())), 'goblin_weapons', r.randint(0, 3), 50),
                "forrest goblin": ("forrest goblin", 'A dark green creature, hlaf the height of the average man. It could be mistaken for a child it wasnt for the large pointed ears and sharp fang like teeth', r.randint(4, 6), r.randint(0, 1), r.randint(0, 1), r.randint(0, 1), r.randint(-1, 0), r.randint(0, 1), r.randint(-2, 0), r.choice(list(enemy_weapon_type["goblin_weapons"].keys())), 'goblin_weapons', r.randint(0, 3), 50),
            },
            'orc types': {
                "Orc Warrior": ("Orc Warrior", "A tall and muscular creature, with green skin and a mean scowl. Known for their brutal strength and fierce loyalty to their clans.", r.randint(8, 12), r.randint(1, 2), r.randint(1, 2), r.randint(1, 2), r.randint(0, 1), r.randint(0, 1), r.randint(-2, 0), r.choice(list(enemy_weapon_type["orc_weapons"].keys())), 'orc_weapons', r.randint(0, 5), 100),
                "Orc Shaman": ("Orc Shaman", "A wizened orc with deep knowledge of dark magic. They are often found leading orc raiding parties, using their spells to bolster their warriors and weaken their enemies.", r.randint(8, 12), r.randint(1, 2), r.randint(1, 2), r.randint(1, 2), r.randint(0, 1), r.randint(0, 1), r.randint(-2, 0), r.choice(list(enemy_weapon_type["orc_weapons"].keys())), 'orc_weapons', r.randint(0, 5), 100),
                "Orc Archer": ("Orc Archer", "A lean orc with excellent aim. They are often found providing ranged support for orc raiding parties, raining arrows down on their enemies from a safe distance.", r.randint(8, 12), r.randint(1, 2), r.randint(1, 2), r.randint(1, 2), r.randint(0, 1), r.randint(0, 1), r.randint(-2, 0), r.choice(list(enemy_weapon_type["orc_weapons"].keys())), 'orc_weapons', r.randint(0, 5), 100),
                "Orc Berserker": ("Orc Berserker", "A massive orc with an uncontrollable rage. They are often used as shock troops, charging headlong into enemy lines and wreaking havoc.", r.randint(8, 12), r.randint(1, 2), r.randint(1, 2), r.randint(1, 2), r.randint(0, 1), r.randint(0, 1), r.randint(-2, 0), r.choice(list(enemy_weapon_type["orc_weapons"].keys())), 'orc_weapons', r.randint(0, 5), 100),
            },
            'undead types': {
                "Zombie": ("Zombie", "A shambling corpse with rotting flesh and an insatiable hunger for brains. These undead are slow, but persistent, and can overwhelm even the most skilled warrior with their sheer numbers.", r.randint(4, 6), r.randint(0, 1), r.randint(0, 1), r.randint(0, 1), r.randint(-1, 0), r.randint(-1, 0), r.randint(-3, -1), r.choice(list(enemy_weapon_type["undead_weapons"].keys())), 'undead_weapons', r.randint(0, 3), 75),
                "Skeleton": ("Skeleton", "A walking pile of bones, animated by dark magic. These undead are fragile, but can be difficult to hit due to their bony frames. They often carry weapons and wear armor, making them more dangerous than they first appear.", r.randint(4, 6), r.randint(0, 1), r.randint(0, 1), r.randint(0, 1), r.randint(-1, 0), r.randint(-1, 0), r.randint(-3, -1), r.choice(list(enemy_weapon_type["undead_weapons"].keys())), 'undead_weapons', r.randint(0, 3), 75),
                "Wraith": ("Wraith", "A ghostly apparition with the power to drain the life force of its enemies. These undead are difficult to hit with physical attacks, but can be vulnerable to magic. They are often found haunting old ruins and graveyards.", r.randint(6, 8), r.randint(0, 1), r.randint(0, 1), r.randint(1, 2), r.randint(-2, 0), r.randint(-2, 0), r.randint(-4, -2), r.choice(list(enemy_weapon_type["undead_weapons"].keys())), 'undead_weapons', r.randint(0, 3), 150),
            },
            "Troll Berserker": ("Troll Berserker", "A massive creature with grey-green skin and razor-sharp claws. Known for their incredible strength and ability to enter a berserker rage during combat.", r.randint(15, 20), r.randint(2, 3), r.randint(2, 3), r.randint(2, 3), r.randint(-1, 1), r.randint(-1, 1), r.randint(-3, -1), r.choice(list(enemy_weapon_type["troll_weapons"].keys())), 'toll_weapons', r.randint(0, 8), 200),
            "Necromancer": ("Necromancer", "A dark and twisted individual with the power to control the undead. They are often found in dark and foreboding places, performing their dark rituals.", r.randint(6, 8), r.randint(0, 1), r.randint(0, 1), r.randint(0, 2), r.randint(-2, 0), r.randint(-2, 0), r.randint(-4, -2), r.choice(list(enemy_weapon_type["magic_weapons"].keys())), 'troll_weapons', r.randint(0, 3), 150),
            "Giant Spider": ("Giant Spider", "A massive arachnid with venomous fangs and a deadly bite. Often found in dark and damp places, they are known for their ability to spin webs and lay traps for their prey.", r.randint(4, 6), r.randint(0, 1), r.randint(0, 1), r.randint(0, 1), r.randint(-1, 0), r.randint(-1, 0), r.randint(-3, -1), r.choice(list(enemy_weapon_type["beast_weapons"].keys())), 'troll_weapons', r.randint(0, 3), 75),
            "Demon Hunter": ("Demon Hunter", "A skilled warrior with a deep hatred for all things demonic. They are often found hunting demons and other evil creatures, using their knowledge of the occult to aid them in battle.", r.randint(8, 10), r.randint(1, 2), r.randint(1, 2), r.randint(1, 2), r.randint(0, 1), r.randint(0, 1), r.randint(-2, 0), r.choice(list(enemy_weapon_type["holy_weapons"].keys())), 'troll_weapons', r.randint(0, 5), 175),
        }
        enemy = r.choice(list(enemy_info[enemy].values()))
        enemy = Enemy(*enemy)
        return enemy

    def spell_attack(self):
        # print_debug_message(str(list(enemy_spells.keys())))
        spell_choice = r.choice(list(enemy_spells.values()))
        spell_chosen = Spell(*spell_choice.values())
        spell_damage = r.randint(*spell_chosen.spell_damage)
        health_cost = r.randint(*spell_chosen.health_cost)
        # print_debug_message(f'spell_damage={spell_damage}. health_cost={health_cost}')
        spell_mod = spell_chosen.spell_stat_mod
        if spell_mod == "wisdom":
            spell_mod = self.enemy_wisdom
        elif spell_mod == 'intelligence':
            spell_mod = self.enemy_intelligence
        # print_debug_message(f'spell_stat_mod={spell_chosen.spell_stat_mod}. spell_mod={spell_mod}')
        spell_damage += spell_mod
        health_cost -= spell_mod
        spell_name = spell_chosen.spell_name
        return spell_damage, health_cost, spell_name

    def weapon_attack(self):
        weapon_choice = list((enemy_weapon_type)[
                             self.enemy_weapon_type][self.enemy_weapon])
        weapon_chosen = Weapon(*weapon_choice)
        damage = r.randint(weapon_chosen.weapon_min, weapon_chosen.weapon_max)
        weapon_mod = weapon_chosen.weapon_stat_mod
        if weapon_mod == "strength":
            weapon_mod = self.enemy_strength
        if weapon_mod == 'dexterity':
            weapon_mod = self.enemy_dexterity
        if weapon_mod == 'charisma':
            weapon_mod = self.enemy_charisma
        if weapon_mod == 'intelligence':
            weapon_mod = self.enemy_intelligence
        damage += weapon_mod
        return damage, self.enemy_weapon

    # def __str__(self):
    #     return f'{green}enemy name:{self.enemy_name}, enemy description: {self.enemy_description}, enemy health:{self.enemy_health}, enemy strength: {self.enemy_strength}, enemy endurance: {self.enemy_endurance}, enemy dexterity: {self.enemy_dexterity}, enemy intelligence: {self.enemy_intelligence}, enemy wisdom: {self.enemy_wisdom}, enemy charisma: {self.enemy_charisma}, enemy weapon: {self.enemy_weapon}, enemy gold: {self.enemy_gold}, enemy xp: {self.enemy_xp}{rcolour}'


class Weapon:
    """This is a Python class called Weapon that represents a weapon object in a game. Here is a breakdown of its attributes and methods:

        Attributes:

        weapon_name: a string representing the name of the weapon
        weapon_description: a string representing a brief description of the weapon
        weapon_min: an integer representing the minimum damage the weapon can inflict
        weapon_max: an integer representing the maximum damage the weapon can inflict
        weapon_stat_mod: an integer representing a modifier to the damage based on a player's stats
        weapon_value: a float representing the value of the weapon
        weapon_type: a string representing the type of weapon (e.g. sword, bow, etc.)
        weapon_skill: a string representing the skill required to use the weapon
        
        Methods:

        __init__(self, weapon_name, weapon_description, weapon_min, weapon_max, weapon_stat_mod, weapon_value, weapon_type, weapon_skill): the constructor method for the class, initializes the attributes of the object
        __str__(self): a method that returns a string representation of the object
        getatt(self): a method that prints out some of the attributes of the object
        Overall, this class provides a way to create and store information about different types of weapons in a game.
    """

    def __init__(self, weapon_name, weapon_description, weapon_min, weapon_max, weapon_stat_mod, weapon_value, weapon_type, weapon_skill):
        self.weapon_name = weapon_name
        self.weapon_description = weapon_description
        self.weapon_min = weapon_min
        self.weapon_max = weapon_max
        self.weapon_stat_mod = weapon_stat_mod
        self.weapon_value = weapon_value
        self.weapon_type = weapon_type
        self.weapon_skill = weapon_skill

    def __str__(self):
        return f"{self.weapon_name}: {self.weapon_min}-{self.weapon_max} damage"

    def getatt(self):
        weapon_name = self.weapon_name
        weapon_min = self.weapon_min
        weapon_max = self.weapon_max
        weapon_stat_mod = self.weapon_stat_mod
        print(weapon_name, weapon_min, weapon_max, weapon_stat_mod)

class Spell:
    """
    Represents a magical spell that can be used to deal damage to enemies.

    Attributes:
    -----------
    spell_name : str
        The name of the spell.
    spell_description : str
        A brief description of the spell.
    spell_damage : int
        The amount of damage that the spell can deal.
    spell_stat_mod : str
        The statistic that the spell's damage is based on (e.g. "intelligence").
    health_cost : int
        The amount of health that the caster must sacrifice to cast the spell.

    Methods:
    --------
    __str__() -> str
        Returns a string representation of the spell, including its name, damage, and health cost.
    """
    def __init__(self, spell_name, spell_description, spell_damage, spell_stat_mod, health_cost):
        self.spell_name = spell_name
        self.spell_description = spell_description
        self.spell_damage = spell_damage
        self.spell_stat_mod = spell_stat_mod
        self.health_cost = health_cost

    def __str__(self):
        return f"{self.spell_name}: {self.spell_damage}- spell_damage : {self.health_cost}-health_damage"


class Combat_loop:
    """
    This class represents a combat loop in a game. It takes a player character and an enemy as inputs and initializes their
    attributes for combat. The class has a method called start_combat that begins the combat between the player and the enemy.

    Attributes:
    ----------
    player_character : object
        The player character object that is participating in combat.
    enemy : object
        The enemy object that is participating in combat.

    Methods:
    -------
    start_combat():
        Begins the combat loop between the player and the enemy.
    """
    def __init__(self, player_character, enemy):
        self.player_character = player_character
        self.enemy = enemy

    def start_combat(self):
        player_character_init = r.randint(
            1, 20) + player_character.player_dexterity
        enemy_init = r.randint(1, 20) + self.enemy.enemy_dexterity
        round = 1
        player_attc_choice = None
        print_slow(f'You are entering combat with a {self.enemy.enemy_name}')
        print_slow(
            f'You roll a {player_character_init} and the {self.enemy.enemy_name} has rolled a {enemy_init}')
        if player_character_init > enemy_init:
            print_slow(
                f'You are faster to react than the {self.enemy.enemy_name}, you get to go first!')
            while True:
                print_slow(f'\nRound {round}')
                print_slow(
                    f'{player_character.player_name} has {player_character.player_health} health and the {self.enemy.enemy_name} has {self.enemy.enemy_health} health')
                if player_character_init > enemy_init:
                    while player_attc_choice not in ['spell', 'weapon']:
                        player_attc_choice = input(
                            f'\nPlease chose how you want to attack!\nWith a "spell" or with a "weapon"?\n>').lower()
                        if player_attc_choice == "spell":
                            enemy_damage_player_health_cost = player_character.spell_attack()
                            player_character.player_health -= enemy_damage_player_health_cost[1]
                            self.enemy.enemy_health -= enemy_damage_player_health_cost[0]
                            print_slow(
                                f'{green}You deal {enemy_damage_player_health_cost[0]} damage to the {self.enemy.enemy_name} but take {enemy_damage_player_health_cost[1]} damage as a result of using the spell{rcolour}')

                            if self.enemy.enemy_health <= 0:
                                print(
                                    f'{green}You have defeated the {self.enemy.enemy_name} and won the fight!{rcolour}')
                                return
                        if player_attc_choice == "weapon":
                            player_attc_damage = player_character.weapon_attack()
                            print_slow(
                                f'{green}You have done {player_attc_damage[0]} with your {player_attc_damage[1]} to the {self.enemy.enemy_name}{rcolour}')
                            self.enemy.enemy_health -= player_attc_damage[0]
                            if self.enemy.enemy_health <= 0:
                                print(
                                    f'{green}You have defeated the {self.enemy.enemy_name} and won the fight!{rcolour}')
                                return
                    player_attc_choice = None
                    attack_choice_spell = r.randint(
                        1, 20) + self.enemy.enemy_intelligence
                    attack_choice_weapon = r.randint(
                        1, 20) + self.enemy.enemy_strength
                    if attack_choice_spell > attack_choice_weapon:
                        damage = self.enemy.spell_attack()
                        print_slow(
                            f'{red}The {self.enemy.enemy_name} attacked you with {damage[2]} dealing {damage[0]} to you!\nThey also take {damage[1]} by using the spell!{rcolour}')
                        player_character.player_health -= damage[0]
                        self.enemy.enemy_health -= damage[1]
                        round += 1
                        if player_character.player_health <= 0:
                            print_slow(
                                f'{red}You have been defeated by the {self.enemy.enemy_name}, better luck next time!{rcolour}')
                            if self.enemy.enemy_health <= 0:
                                print_slow(
                                    f'{green}You have defeated the {self.enemy.enemy_name} and won the fight!{rcolour}')
                                return
                    if attack_choice_weapon > attack_choice_spell:
                        damage = self.enemy.weapon_attack()
                        print_slow(
                            f'{red}The {self.enemy.enemy_name} is attacking with a {damage[1]}{rcolour}')
                        print_slow(
                            f'{red}The {self.enemy.enemy_name} did {damage[0]} damage to you!{rcolour}.')
                        player_character.player_health -= damage[0]
                        round += 1
                        if player_character.player_health <= 0:
                            print_slow(
                                f'{red}You have been defeated by the {self.enemy.enemy_name}, better luck next time!{rcolour}')
                            exit
        if enemy_init > player_character_init:
            print_slow(
                    f'{red}The {self.enemy.enemy_name} has reacted quicker than you, they go first!{rcolour}')
            while True:
                print_slow(f'Round {round}')
                print_slow(
                    f'{player_character.player_name} has {player_character.player_health} health and the {self.enemy.enemy_name} has {self.enemy.enemy_health} health')
                attack_choice_spell = r.randint(
                    1, 20) + self.enemy.enemy_intelligence
                attack_choice_weapon = r.randint(
                    1, 20) + self.enemy.enemy_strength
                if attack_choice_spell > attack_choice_weapon:
                    damage = self.enemy.spell_attack()
                    print_slow(
                        f'{red}The {self.enemy.enemy_name} attacked you with {damage[2]} dealing {damage[0]} to you!\nThey also take {damage[1]} by using the spell!{rcolour}')
                    player_character.player_health -= damage[0]
                    self.enemy.enemy_health -= damage[1]
                    round += 1
                    if player_character.player_health <= 0:
                        print_slow(
                            f'{red}You have been defeated by the {self.enemy.enemy_name}, better luck next time!{rcolour}')
                        exit
                if attack_choice_weapon > attack_choice_spell:
                    damage = self.enemy.weapon_attack()
                    print_slow(
                        f'{red}The {self.enemy.enemy_name} attacked you with a {damage[1]} and did {damage[0]} damage!{rcolour}')
                    player_character.player_health -= damage[0]
                    if player_character.player_health <= 0:
                        print_slow(
                            f'{red}You have been defeated by the {self.enemy.enemy_name}, better luck next time!{rcolour}')
                        exit
                player_attc_choice = None
                while player_attc_choice is not 'spell' or not 'weapon':
                    player_attc_choice = input(
                        f'Please chose how you want to attack!\nWith a "spell" or with a "weapon"?\n>').lower()
                    if player_attc_choice == "spell":
                        enemy_damage_player_health_cost = player_character.spell_attack()
                        player_character.player_health -= enemy_damage_player_health_cost[1]
                        self.enemy.enemy_health -= enemy_damage_player_health_cost[0]
                        print_slow(
                            f'{green}You deal {enemy_damage_player_health_cost[0]} damage to the {self.enemy.enemy_name} but take {enemy_damage_player_health_cost[1]} damage as a result of using the spell{rcolour}')
                        round += 1
                        if self.enemy.enemy_health <= 0:
                            print(
                                f'{green}You have defeated the {self.enemy.enemy_name} and won the fight!{rcolour}')
                            return
                    if player_attc_choice == "weapon":
                        player_attc_damage = player_character.weapon_attack()
                        print_slow(
                            f'{green}You have done {player_attc_damage[0]} with your {player_attc_damage[1]} to the {self.enemy.enemy_name}{rcolour}')
                        self.enemy.enemy_health -= player_attc_damage[0]
                        round += 1
                        if self.enemy.enemy_health <= 0:
                            print(
                                f'{green}You have defeated the {self.enemy.enemy_name} and won the fight!{rcolour}')
                            return
                    break


class Location:
    def __init__(self):
        self.exit_choices = locations[player_character.player_location]['exits']
        self.player_location = locations[player_character.player_location]
        self.enemies = locations[player_character.player_location]['enemies']

    def location_change(self, player_location):
        exit_choice = None
        exit_locations = locations[player_location]['exits']
        print_slow('Please choose a location:')
        i = 0
        for choice in exit_locations.values():
            i += 1
            print(i, choice)
        while exit_choice == None:
            exit_choice = input('>')
            if exit_choice in exit_locations:
                exit_choice = exit_locations[exit_choice]
                player_character.player_location = exit_choice
                # print_debug_message(f'player_location = {exit_choice}')
                return player_character.player_location, self.player_location,self.location_choices()
            else:
                rnum = r.randint(1, 10)
                if rnum <= 9:
                    print_slow("That is not a valid exit choice")
                    exit_choice=None
                else:
                    print_slow(
                        "Stop trying to make new locations!.What do you think you know better than me or something?.Is my story not interesting enough for you?.")
                    exit_choice=None

    def location_choices(self):
        ldescription = locations[player_character.player_location]['description']
        print_slow(f"{ldescription}\n")
        if 'enemies' in locations[player_character.player_location]:
            if locations[player_character.player_location]['enemies'] != {}:
                lenemies = locations[player_character.player_location]['enemies'].values(
                )
                lenemies = ', '.join(lenemies)
                print_slow(
                    f'{red}You have been attacked by {lenemies}.Prepare to fight.{rcolour}')
                fightnum = 1
                for enemy in list(locations[player_character.player_location]['enemies'].keys()):
                    print_slow(f'Fight {fightnum}')
                    enemy_created = Enemy.gen_random_enemy(enemy)
                    fight = Combat_loop(player_character, enemy_created)
                    fight.start_combat()
                    del locations[player_character.player_location]['enemies'][enemy]
                    fightnum += 1
                    if locations[player_character.player_location]['enemies'] == {}:
                        print_slow(
                            'You have defeated all the enemies in the area!.')
                        lchoice = None
        
        if 'player journal entry' in  locations[player_character.player_location]:
            new_journal_entry = locations[player_character.player_location]['player journal entry']
            entry_num = len(player_journal) + 1
            player_journal.append(f'Entry {entry_num}: {new_journal_entry}')
        
        lchoice = None
        while lchoice == None:
            print_slow(
                f'What do you want to do?.1 : Move to new location.2 : Explore current location.3 : Talk.4 : Fight enemies.5 : Open your Journal')
            
            lchoice = input('>')

            if lchoice == '1':
                self.location_change(player_character.player_location)
            elif lchoice == '2':
                if 'explore' in locations[player_character.player_location]:
                    self.location_explore()
                else:
                    print_slow(
                        'You look around but do not see anything to investigate')
                    lchoice = None
            elif lchoice == '3':
                if 'NPCs' in self.player_location:
                    self.location_conversation()
                else:
                    print_slow(
                        "Talking to yourself is fine.It's when you start talking back that you should worry!")
                    lchoice = None
            elif lchoice == '4':
                if locations[player_character.player_location]['enemies'] != {}:
                    fightnum = 1
                    for enemy in list(self.enemies.keys()):
                        print_slow(f'Fight {fightnum}')
                        enemy_created = Enemy.gen_random_enemy(enemy)
                        fight = Combat_loop(player_character, enemy_created)
                        fight.start_combat()
                        del self.enemies[enemy]
                        fightnum += 1
                        if locations[player_character.player_location]['enemies'] == {}:
                            print_slow(
                                'You have defeated all the enemies in the area!.')
                            lchoice = None
                else:
                    print_slow('There are no enemies for you to fight!.')
                    lchoice = None
            elif lchoice == '5':
                journal_info = ''
                for entry in player_journal:
                    journal_info += f'{entry}\n\n'
                journal_window = Message_box(journal_info, f'{player_character.player_name} Journal', player_journal)
                lchoice = None
            else:
                lchoice = None


    def location_explore(self):
        edescription = locations[player_character.player_location]['explore']['description']
        print_slow(edescription)
        eloot = locations[player_character.player_location]['explore']['loot'].values(
        )
        for value in eloot:
            if isinstance(value, str):
                print_slow(value)
        self.location_choices()


enemy_spells = {
    "fireball": {
        "spell_name": "Inferno",
        "spell_description": "A spell that creates a massive explosion of fire and engulfs the target.",
        "spell_damage": (5, 8),  # random integer between 5 and 8
        "spell_stat_mod": "wisdom",  # enemy's attribute to decrease health cost
        "spell_health_cost": (2, 5)  # random integer between 7 and 12
    },
    "poison": {
        "spell_name": "Venom",
        "spell_description": "A spell that poisons the target and deals damage over time.",
        "spell_damage": (2, 4),  # random integer between 2 and 4
        "spell_stat_mod": "intelligence",
        "spell_health_cost": (1, 3)
    },
    "frost_bolt": {
        "spell_name": "Frost Bolt",
        "spell_description": "A spell that shoots a bolt of freezing ice at the target.",
        "spell_damage": (3, 6),
        "spell_stat_mod": "intelligence",
        "spell_health_cost": (1, 4)
    }
}

player_spells = {
    "embers": {
        "spell_name": "Embers",
        "spell_description": "A powerful spell that creates a ball of fire and hurls it at the target.",
        "spell_damage": (3, 6),  # random integer between 10 and 20
        "spell_stat_mod": "intelligence",  # player's attribute to decrease health cost
        "spell_health_cost": (1, 4)  # random integer between 5 and 10
    },
    "heal": {
        "spell_name": "Heal",
        "spell_description": "A spell that restores health to the user.",
        "spell_damage": (-5, 0),  # spell has a chance to heal target as well
        "spell_stat_mod": "wisdom",
        # random integer between -6 and -1 (i.e. heals instead of dealing damage)
        "spell_health_cost": (-6, -1)
    },
    "ice_blast": {
        "spell_name": "Ice Blast",
        "Spell_description": "A spell that creates a blast of ice and hurls it at the target.",
        "Spell_damage": (3, 6),
        "spell_stat_mod": "intelligence",
        "spell_health_cost": (1, 4)
    }
}

player_weapon_type = {
    "rusty sword": ("rusty sword", "A rusty old sword, probably been in the family for generations", 1, 4, "dexterity", 10, 'malee weapon skills', 'one handed weapons'),
    "rusty axe": ("rusty axe", "A rusty old axe, probably been in the family for generations", 1, 4, "strength", 10, 'malee weapon skills', 'one handed weapons'),
    "splintered bow": ("splintered bow", "A old bow showing signs of splintering, nearly at its breaing point", 1, 4, "dexterity", 10, 'ranged weapon skills', 'bows'),
    "cracked wand": ("cracked wand", "An old family heirloom, damaged from excessive use", 1, 4, "intelligence", 10, 'magic weapon skills', 'wands')
}

""" Player weapon skill dictionary
This is a dictionary that stores information about a player's weapon skills. It has two main keys:

'weapon skill levels': which contains the player's skill level for each type of weapon.
'weapon skill experience': which contains the player's experience for each type of weapon.
Each of these keys has subkeys for different types of weapons:

'melee weapon skills': which contains subkeys for one-handed weapons, two-handed weapons, and daggers.
'ranged weapon skills': which contains subkeys for bows, crossbows, and guns.
'magic weapon skills': which contains subkeys for wands, staffs, and holy symbols.
Each subkey contains a value that represents the player's skill level or experience for that particular weapon.

This dictionary is used to keep track of a player's progress in developing their weapon skills, and is likely to be updated as the player gains experience and becomes more proficient with different types of weapons.

"""
player_weapon_skills = {
    'weapon skill levels': {
        'malee weapon skills': {
            'one handed weapons': 0,
            'two handed weapons': 0,
            'dagger': 0,
        },
        'ranged weapon skills': {
            'bows': 0,
            'cross bows': 0,
            'guns': 0,
        },
        'magic weapon skills': {
            'wands': 0,
            'staffs': 0,
            'holy symbols': 0,
        }
    },
    'weapon skill experience': {
        'malee weapon skills': {
            'one handed weapons': [0, 100],
            'two handed weapons': [0, 100],
            'dagger': [0, 100],
        },
        'ranged weapon skills': {
            'bows': [0, 100],
            'cross bows': [0, 100],
            'guns': [0, 100],
        },
        'magic weapon skills': {
            'wands': [0, 100],
            'staffs': [0, 100],
            'holy symbols': [0, 100],
        },
    },
}

enemy_weapon_type = {
    'goblin_weapons': {
        'goblin dagger': ('goblin dagger', 'A crude attempt at a makeshift weapon. A sharpened stone with ragged cloth tied at the base for a handle', 1,  3, 'dexterity', 0, 'None', 'None',),
        'goblin club': ('goblin club', 'A crude makeshift weapon. A large stone forced into a chunck of wood', 1, 3, 'strength', 0, 'None', 'None',),
        'sack of rocks': ('sack of rocks', 'A collection of smaller rocks, some covered in blood.', 1, 3, 'dexterity', 0, 'None', 'None',)
    },
    'orc_weapons': {
        'orc axe': ('orc axe', 'A large and heavy axe, made for crushing bones and splitting shields.', 2, 6, 'strength', 50, 'None', 'None'),
        'orc mace': ('orc mace', 'A brutal weapon made of iron spikes attached to a heavy wooden handle.', 2, 6, 'strength', 50, 'None', 'None'),
        'orc spear': ('orc spear', 'A long and deadly weapon, designed for piercing through armor and enemies alike.', 2, 6, 'dexterity', 50, 'None', 'None')
    },
    'undead_weapons': {
        'bone sword': ('bone sword', 'A sword made from the bones of the undead. Its jagged edges can cause severe damage to living foes.', 2, 6, 'strength', 50, 'None', 'None'),
        'death scythe': ('death scythe', 'A grim weapon that can instantly reap the souls of those it strikes down. It is said that the scythe itself is alive.', 3, 6, 'strength', 75, 'None', 'None'),
        'necrotic staff': ('necrotic staff', 'A staff that channels the power of the undead. It can weaken the lifeforce of enemies and drain their vitality.', 2, 8, 'intelligence', 50, 'None', 'None')
    },
    'troll_weapons': {
        'troll hammer': ('troll hammer', 'A massive hammer, capable of smashing through solid stone with ease.', 3, 9, 'strength', 100, 'None', 'None'),
        'troll claws': ('troll claws', 'Long and razor-sharp claws, designed to shred through armor and flesh alike.', 3, 9, 'dexterity', 100, 'None', 'None'),
        'troll javelin': ('troll javelin', 'A long and heavy javelin, capable of impaling multiple enemies at once.', 3, 9, 'strength', 100, 'None', 'None')
    },
    'magic_weapons': {
        'fireball staff': ('fireball staff', 'A powerful staff imbued with the power of fire, capable of unleashing devastating spells.', 1, 3, 'intelligence', 75, 'None', 'None'),
        'ice shard wand': ('ice shard wand', 'A wand that creates sharp shards of ice, piercing through enemies and leaving them frozen in place.', 1, 3, 'intelligence', 75, 'None', 'None'),
        'necrotic scythe': ('necrotic scythe', 'A scythe imbued with dark magic, capable of draining the life force from enemies with each strike.', 1, 3, 'intelligence', 75, 'None', 'None')
    },
    'beast_weapons': {
        'poisonous fangs': ('poisonous fangs', 'Long and deadly fangs, capable of injecting venom into enemies and causing them to weaken.', 2, 5, 'dexterity', 25, 'None', 'None'),
        'acidic spines': ('acidic spines', 'Spiny protrusions from a beast, coated in a powerful acid that can burn through armor and flesh.', 2, 5, 'dexterity', 25, 'None', 'None'),
        'crushing tail': ('crushing tail', 'A massive and powerful tail, used by beasts to crush and maim enemies.', 2, 5, 'strength', 25, 'None', 'None')
    },
    'holy_weapons': {
        'divine sword': ('divine sword', 'A beautiful and powerful sword, imbued with the power of divine magic.', 2, 7, 'strength', 150, 'None', 'None'),
        'holy mace': ('holy mace', 'A weapon of pure light and energy, capable of striking down evil and undead enemies with ease.', 2, 7, 'strength', 150, 'None', 'None'),
        'holy bow': ('holy bow', 'A bow imbued with holy magic, capable of firing arrows of pure energy that smite enemies on contact.', 2, 7, 'dexterity', 150, 'None', 'None')
    }
}

locations = {
    "start": {
        "description": "You awake in the pitch black, the sound of dripping water echos around you.The cold hard ground underneath you feels like stone.You reach into your bad and pull out a tourch to light.The flame flickers to life and reveals that you are in a cave.You can see two passageways out of the area, do you take the one on the right or the left?",
        "exits": {
            "1": "left passageway",
            "2": "right passageway"
        },
        'enemies': {},
        "explore": {
            "description": "The cave is damp and cold, with jagged rocks protruding from the walls and ceiling. The ground is uneven and covered in a layer of dust and dirt. The air is thick with the smell of damp earth and mold.",
            "loot": {
                'bones': 'Scattered around the floor are various remains of creatures',
                'rusty broken sword': 'A rust covered broken sword, not worth taking'
            },
        },
    },
    "left passageway": {
        "description": "As you enter the passageway you notice a cool breeze blowing against your face. The walls around you are slick with water and the ground begins to become coated in more and more soil the further along you go. Do you continue or turn around?",
        "exits": {
            "1": "forest",
            "2": "starting room"
        }
    },
    "right passageway": {
        "description": "You begin to walk down the passageway and notice that the air is becoming more and more stale the further you go. In the distance you swear you can hear the sound of something moving. Do you continue or turn around?",
        "exits": {
            "1": "main cave hub",
            "2": "starting room"
        }
    },
    "forest": {
        "description": "You see the blinding light of day growing brighter and brighter as you move quickly up the passageway until you finally emerge from the cave. Taking a second to drinkn in your surroundings you find yourself in a dense thick forrest, the sound of wild life can be heard all around. You notice an opening in the tree line straight a head and a climbable tree to the right of you. What do you do?",
        "exits": {
            "1": "forest opening",
            "2": "tree climb",
            "3": "cave return"
        }
    },
    "main cave hub": {
        "description": "You step into a gaint canverness room. Water dripping from the ceiling splashes around you as you examine the area. Out of the corner of your eye you spot a green flash dart into the darkness. What do you do?",
        "exits": {
            "1": "goblin chase",
            "2": "starting room"
        },
        "player journal entry" :""" Gaint cave hub\n 
As I stepped into the cavernous room, I couldn't help but feel a sense of awe. The room was massive, and the sound of water dripping from the ceiling echoed off the walls. As I took a moment to examine the area, I couldn't help but feel a sense of unease. Something didn't feel right.

Out of the corner of my eye, I spotted a flash of green dart into the darkness. I knew I had to investigate. I drew my sword and shield, ready for whatever lay ahead. As I moved deeper into the cavern, the sound of my footsteps echoed loudly.

As I drew closer to the spot where I saw the green flash, I couldn't help but feel a sense of apprehension. I knew that danger lurked in these caverns, and I needed to be cautious. My hand tightened around the hilt of my sword as I stepped closer to the darkness.

Suddenly, I heard a rustling sound and a low growl. I was not alone in this cavern. I gripped my sword tightly and prepared to face whatever lay ahead."""
    },
    "goblin chase": {
        "description": "Not wanting to let the mystery figure escape you begin to chase after it.Running fast through the cave, your foot steps echoing as you go, you begin to gain ground on it.Your blood is thumping in your ears as you turn a corner and finally see the figures cornered in a deadend.You are now face to face with 3 Cave Goblins.What do you do?",
        "exits": {
            "1": "goblin talk",
            "2": "running away",
        },
        "enemies": {
            'goblin types': 'cave goblin 1',
        },
        "end_of_fight": {"goblin fight": "goblin fight"},
        "fight_loot": {},
        "combat": True,
        "player journal entry" :""" First kill\n 
Today I faced my first battle against a cave goblin, and I emerged victorious. I cannot help but feel a sense of pride mixed with a tinge of sadness. It was the first time I have ever killed such a large creature, and I cannot help but reflect on the experience.

As I was exploring the caverns, I heard the sound of footsteps approaching. I knew that danger was near, so I drew my sword and shield, ready for whatever lay ahead.

Suddenly, a cave goblin appeared before me. It was small, but fierce, with razor-sharp teeth and beady eyes that glinted in the dim light. It lunged at me, but I was ready for it.

We engaged in a quick but deadly battle. The goblin was fast, but I was able to parry its attacks with my shield and strike back with my sword. After a few minutes of intense fighting, I finally landed a fatal blow, and the goblin fell to the ground, dead.

As I caught my breath and looked at the lifeless body of the goblin, I couldn't help but feel a mix of emotions. On the one hand, I was proud of myself for defeating such a formidable foe. On the other hand, I couldn't help but feel a sense of sadness at taking another creature's life.

But such is the life of an adventurer. I knew that I would face many more battles like this in the future, and that I needed to be prepared to defend myself against whatever lay ahead.

I gathered my wits about me and continued on my journey, knowing that I had overcome this challenge and was ready for whatever lay ahead.

Until next time, Journal.""",

    },
    "goblin talk": {
        "description": "The goblin looks afriad and confused. 'Why are you chasing me? leave me alone!'. You are surprised by this. Do you go back to the main room?",
        "exits": {
            "1": "main cave hub return"
        }
    },
    "goblin fight": {
        "description": "As the goblin snarls you instenctivly reach down and grasb the hilt of your sword. Seeing the danager the goblin lunges at you and manages to plung a dagger into your leg. Feeling a rush of pain you quickly swing your sword with all your might, cleaving the goblins head off. Your leg is badly damaged, you have lost 20 health points. With the goblin defeated what do you do?",
        "exits": {
            "1": "goblin search",
            "2": "leg bandage",
            "3": "main cave hub return"
        }
    },
    "goblin search": {
        "description": "You look through the pockets of the goblin and only find 2 gold pieces and a few small bones from the goblins last meal. You stand back up and trun around to face the passageway back to big room, you glance down at your bleeding leg. What do you do?",
        "exits": {
            "1": "leg bandage",
            "2": "main cave hub return"
        }
    },
    "leg bandage": {
        "description": "You take your bag off and look for a bandage. Finding one in the front pocket of the bag you take it out and wrap it tightly around your leg. Happy that youve stopped the bleeding you look at the goblin on the floor and passageway back to the main hub. What do you want to do?",
        "exits": {
            "1": "goblin search",
            "2": "main cave hub return"
        }
    },
    "main cave hub return": {
        "description": "You manage to make your way back to the large room in the cave. You notice a cool breeze coming from the passageway back to where you woke up. With your back to the passageway that is now the goblins tomb, what do you do?",
        "exits": {
            "1": "goblin corpse",
            "2": "starting room"
        }
    },
    "goblin corpse": {
        "description": "You go back down the passageway to the goblin's corpse. What do you do?",
        "exits": {
            "1": "goblin search",
            "2": "main cave hub return"
        }
    },
    "starting room": {
        "description": "You enter the room where you woke up. You can see two passage ways out of the area, do you take the one on the right or the left?",
        "exits": {
            "1": "main cave hub return",
            "2": "left passageway"
        }
    },
    "testing hall": {
        "description": "You have entered the dev testing hall"
    }
}

player_journal= [
"""
Entry 1: The worst headache\n
I'm not entirely sure what happened to me, but I seem to have found myself in quite a predicament.The last thing I remember was going to bed, and now I'm lying on the hard, cold ground of a cave. The darkness is all-encompassing, and the only sound is that of dripping water echoing around me. 
    
I fumble around in my bag, hoping to find something useful. My hand brushes against a flashlight, and I breathe a sigh of relief. I turn it on, and the flame flickers to life, casting a dim light around me. The cave is vast and seems to go on forever. I try to remember how I got here, but my mind draws a blank. Was I kidnapped? Did I wander here on my own? I simply cannot recall. All I know is that I need to find my way out of this cave and back to civilization.

I will keep you updated, Journal, as I continue to navigate this unknown terrain. For now, I'll keep moving forward, one step at a time.
"""
]


player_character = Player_character(
    'Ed', 100, None, 5, 5, 5, 5, 5, 5, 5, 5, 5, None, None)
# print(str(player_character))
# print(player_character.weapon_attack())
# print(player_character.spell_attack())

enemy_info = {
    "cave goblin": ("cave goblin", 'A small greyish creature, half the height of the average man. It could be mistaken for child if it wasnt for the large pointed ears and sharp fang like teeth', r.randint(4, 6), r.randint(0, 1), r.randint(0, 1), r.randint(0, 1), r.randint(-1, 0), r.randint(0, 1), r.randint(-2, 0), r.choice(list(enemy_weapon_type["goblin_weapons"].keys())), r.randint(0, 3), 50),
    "forrest goblin": ("forrest goblin", 'A dark green creature, hlaf the height of the average man. It could be mistaken for a child it wasnt for the large pointed ears and sharp fang like teeth', r.randint(4, 6), r.randint(0, 1), r.randint(0, 1), r.randint(0, 1), r.randint(-1, 0), r.randint(0, 1), r.randint(-2, 0), r.choice(list(enemy_weapon_type["goblin_weapons"].keys())), r.randint(0, 3), 50),
}

os.system('cls')
movement = Location()
movement.location_choices()

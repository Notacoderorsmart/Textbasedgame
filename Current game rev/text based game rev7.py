# Text based averture game
from colorama import Fore, Back, Style
import json
import random
import re


ERROR_COLOR = Fore.RED
DEBUG_COLOR = Fore.YELLOW

player_location = "goblin chase" 
end_location = "Town"
current_location = ()
player_init_roll = ()
enemy_init_roll = ()

##############################
#                            #
#          Classes           #
#                            #
##############################

class player:
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
        self.xp_to_next_level = 0 # starting xp value of player
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
        if damage_to_player > 0:
            damage_to_player = enemy.enemy_attack - armour
            if damage_to_player <= 0:
                print(Fore.GREEN, f"Your armour completely absorped the damage from that attack, that was lucky!" + Style.RESET_ALL)
            else:
                armour_block = enemy.enemy_attack - damage_to_player
                print(Fore.GREEN, f"Your armour blocked {armour_block} points of damage!" + Style.RESET_ALL)
                return damage_to_player
        self.health -= damage_to_player
        return self.health

    def add_to_inventory(self, item, amount):
        if item in self.inventory:
            self.inventory[item] += amount
        else:
            self.inventory[item] = amount

class location:
    def __init__(self,name, description, shops_in_location, inns_in_location, shop_names, inns_names, enemies):
        self.name              = name
        self.description       = description
        self.shops_in_location = shops_in_location
        self.inns_in_location  = inns_in_location
        self.shop_names        = shop_names
        self.inns_names        = inns_names
        self.enemies           = enemies

class enemy:
    def __init__(self, enemy_type, enemy_health, enemy_weapon, enemy_attack, enemy_strength, enemy_endurance, enemy_dexterity, enemy_intelligence, enemy_wisdom, enemy_charisma, enemy_gold, enemy_xp_points):
        self.enemy_type = enemy_type
        self.health = enemy_health
        self.weapon = enemy_weapon
        self.strength = enemy_strength
        self.endurance = enemy_endurance
        self.dexterity = enemy_dexterity
        self.intelligence = enemy_intelligence
        self.wisdom = enemy_wisdom
        self.charisma = enemy_charisma
        self.attack = enemy_weapon.attack
        self.gold = enemy_gold
        self.xp = enemy_xp_points
        self.inventory = {}
        enemy_attack = weapon.attack(self,enemy_weapon)
        
    def gen_random_enemy(enemy_type, enemy_health, enemy_weapon, enemy_attack, enemy_strength, enemy_endurance, enemy_dexterity, enemy_intelligence, enemy_wisdom, enemy_charisma, enemy_gold, enemy_xp_points):
        random.choice(list(enemy_info.keys()))
        
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
            
class weapon:
    def __init__(self, weapon_type, min_damage, max_damage, weapon_stat_mod, weapon_value, weapon_user):
        self.weapon_type         = weapon_type
        self.min_damage          = min_damage
        self.max_damage          = max_damage
        self.weapon_stat_mod     = weapon_stat_mod
        self.weapon_value        = weapon_value
        self.user                = weapon_user
        

    def attack(self, user):
        if self.weapon_stat_mod == "strength":
            modifier = self.user.strength if self.user else 0
        elif self.weapon_stat_mod == "dexterity":
            modifier = self.user.dexterity if self.user else 0
        elif self.weapon_stat_mod == "intelligence":
            modifier = self.user.intelligence if self.user else 0
        else:
            modifier = 0
        attack = random.randint(self.min_damage, self.max_damage)
        attack += modifier
        print(f"{self.weapon_type} does {attack} damage")
        print_debug_message("DEBUG: class:weapon func_attack attack =", attack)
        return attack

class Spells:
    def __init__(self, spell_name, min_damage, max_damage, health_cost):
        self.spell_name  = spell_name
        self.min_damage  = min_damage
        self.max_damage  = max_damage
        self.health_cost = health_cost

    def attack(self, user,target):
        if user == player.self:
            int_mod = player.intelligence
            return int_mod
        if user == enemy.self:
            int_mod = enemy.self
            return int_mod
        attack = random.randint(self.min_damage, self.max_damage)
        user_health_damage = random.randint(1, self.health_cost) - int_mod
        user.health -= user_health_damage
        target.health -= attack
        print(f"{self.spell_name} does {attack} damage to {target.name}")
        print(f"{target.name} has {target.health} health left")
        print(f"{user.name} lost {user_health_damage} health as a result of using {self.spell_name}")

    def use(self, user, target):
        if user.health < self.health_cost:
            print(f"{user.name} does not have enough health to use {self.spell_name}")
        else:
            self.attack(user, target)
    
##############################
#                            #
#         functions          #
#                            #
##############################

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

def game_introduction():
    print("Welcome Adventurer to Bleak Falls!")
    print("Will you be able to escape the cave and return to town in one piece?")
    print("What is your name adventurer?")
    player_name = input(">")
    print("A hardy hello to you " + player_name + ", are you ready for adventure?")
    while True:
        ready_state = input(">").lower().split(' ')
        if any(word in ready_state for word in ["ready", "yes"]):
            print("Lets begin the adventure of " + player_name + " in Bleak Falls!")
            break
        else:
            print("I'm sorry I did not understand you advernturer. Please say Ready or Yes when you want to begin!")
        
def game_start():
    current_location = player_location
    print(locations[current_location]["description"])

def move_player(player_location, direction):
    if direction in locations[player_location]["exits"]:
        print_debug_message("DEBUG: move_player player_loocation 1 = " + str(player_location))
        player_location = locations[player_location]["exits"][direction]
        print(locations[player_location]["description"])
        print(Fore.GREEN, "location choices: " + str(list(locations[player_location]["exits"].keys())) + Style.RESET_ALL)
        print_debug_message("DEBUG: move_player player_loocation 2 = " + str(player_location))
        return player_location
    else:
        print("You cannot go that way.")
        print_debug_message("DEBUG: move_player player_loocation 3 = " + str(player_location))
        return player_location

def player_health_change(current_location, player_health):
    health_change = None
    for word in locations[current_location]["description"].split():
        if word == "health":
            # Find all the integers in the description
            digits = ""
            for char in locations[current_location]["description"]:
                if char.isdigit():
                    digits += char
                else:
                    if digits:
                        health_change = int(digits)
                        break
                    else:
                        digits = ""

            if digits:
                health_change = int(digits)
                break

    if health_change:
        player_health -= health_change
        print("You have lost " + str(health_change) + " health. You now have " + str(player_health) + " health.")
    return player_health

def collect_gold(current_location, player_inventory):
    last_digit = None
    for word in locations[current_location]["description"].split():
        if word == "gold":
            # Find the last whole digit before the reference to "gold"
            for i in range(len(locations[current_location]["description"])):
                if locations[current_location]["description"][i:i+4] == "gold":
                    j = i - 2
                    while j >= 0 and locations[current_location]["description"][j].isdigit():
                        j -= 1
                    last_digit = int(locations[current_location]["description"][j+1:i])
                    break
            break
    if last_digit:
        inventory["gold pieces"] += last_digit
        print(Fore.BLUE, "You have collected " + str(last_digit) + " gold pieces. You now have " + str(inventory["gold pieces"]) + " gold pieces." + Style.RESET_ALL)
    return inventory

def combat_loop(player_location, player_health, player_stats,player_attacks, locations, inventory, user_input,player_init_roll,enemy_init_roll, enemy_to_fight,damage):
    print_debug_message("DEBUG: combat_loop player_location = " + str(player_location))
    enemies_in_location = locations[player_location]["enemies"]
    enemies_in_location = str(enemies_in_location).lower()
    print_debug_message("DEBUG: combat_loop enemies_in_location = " + str(enemies_in_location))
    while len(list(enemies_in_location)) >= 2:
        if user_input.lower() == "print_player_location":
            print_debug_message("DEBUG: player current location is " + str(player_location))
        print(Fore.BLUE, "There are " + " " + ", ".join(locations[player_location]["enemies"]) + " here!" + Style.RESET_ALL)
        print_debug_message("DEBUG: comabt_loop enemie_in_location  = " + str(enemies_in_location))
        enemy_to_fight = input(Fore.RED + "Please select an enemy to fight\n> " + Style.RESET_ALL).lower()
        if enemy_to_fight in enemies_in_location:
            print(Fore.RED + "You have selected to fight " + str(enemy_to_fight) + " first!" + Style.RESET_ALL)
            print_debug_message("DEBUG: combat_loop enemy_to_fight = " + str(enemy_to_fight))
            break
        else:
            print_error_message("ERROR: That enemy is not here, please select another!")
    if len(enemies_in_location) < 2:
        print(Fore.BLUE + "There is " + str(len(enemies_in_location)) + " " + str(list(locations[player_location]["enemies"]["name"].keys())) + " here!" + Style.RESET_ALL)
        enemy_to_fight = enemies_in_location[0]
        print(Fore.RED + "You have no choice but to fight " + str(enemy_to_fight) + " first!" + Style.RESET_ALL)

    while player_init_roll != int:
#        player_init_roll = input("""Please roll for your combat initiative
#                                > """).lower()
#        if "roll initiative" != player_init_roll:
#            print_error_message("ERROR: Please roll initiative!")
#        else:
#            "roll initiative" == player_init_roll
#            player_init_roll = random.randint(1,20)+int(player_stats["dexterity"])
#            print_debug_message("DEBUG: combat_loop player_init_roll = " + str(player_init_roll))
            player_init_roll = 1
            print_debug_message("DEBUG: combat_loop player_init_roll = " + str(player_init_roll))
            break
           
    
    while enemy_init_roll != int:
        #enemy_init_roll = random.randint(1,20)
        enemy_init_roll = 300 
        print_debug_message("DEBUG: combat_loop enemy_init_roll = " + str(enemy_init_roll))
        break
    
    while enemies_in_location is not False:
        print_debug_message("DEBUG: check if player init is higher than enemy int" + str(player_init_roll > enemy_init_roll))
        if player_init_roll > enemy_init_roll:
            print(Fore.BLUE, "You have the upperhand and get to act first!" + Style.RESET_ALL)
            player_combat_loop(enemy_to_fight,player_attacks,inventory)
            return player_health
        else:
            if player_init_roll < enemy_init_roll:
                print(Fore.BLUE, "You are caught off guard and the " + str(enemy_to_fight) + " is first to act!" + Style.RESET_ALL)
                enemy_combat_loop(enemy_to_fight,player_health,player_location,enemies_in_location)
                return player_health
    
    return player_init_roll, enemy_init_roll, enemy_to_fight,
        
def player_combat_loop(enemy_to_fight, player_attacks, inventory, player_health):
    if enemy_to_fight != None:
        weapon_select = input("""Please select the weapon to attack with!\n> """)
        if weapon_select != len[0]:
            weapon_select = weapon_select.lower().split(' ')
        print_debug_message("DEBUG: player_combat_loop enemy_to_fight weapon_select = " +str(weapon_select))
        print_debug_message("DEBUG: player_combat_loop enemy_to_fight weapon = " +str(weapon_select))
        for weapon in weapon_select:
            if weapon in inventory:
                weapon_select = weapon
                return weapon_select
        print_debug_message("DEBUG: player_combat_location weapon_select = " + str(weapon_select))
        if weapon_select in inventory:
            print_error_message("ERROR: Weapon not found in inventory!")
            print_debug_message("DEBUG: player_combat_loop enemy_to_fight weapon_select = " + str(weapon_select))
        elif weapon_select in player_attacks:
            print_error_message("ERROR: That is not a weapon to fight with!")
        else:
            damage_range = player_attacks[weapon_select].split(",")
            damage_roll = random.randint(int(damage_range)[0]), int(damage_range)[1]
            print(Fore.BLUE + "You use your " + str(weapon_select) + " and deal " + str(damage_roll) + " damage to " + str(enemy_to_fight) + Style.RESET_ALL)
            locations[player_location]["enemies"][enemy_to_fight]["health"] -= damage_roll
            if locations[player_location]["enemies"][enemy_to_fight]["health"] <= 0:
                print(Fore.GREEN + "You have defeated " + str(enemy_to_fight) + "!" + Style.RESET_ALL)
                del locations[player_location]["enemies"][enemy_to_fight]
                if len(locations[player_location]["enemies"]) == 0:
                    print(Fore.GREEN + "You have defeated all enemies in this location!" + Style.RESET_ALL)
                    return

def enemy_combat_loop(enemy_to_fight, player_health, player_location, enemies_in_location):
    print_debug_message("DEBUG: enemy_combat_loop arguments = " + str(enemy_to_fight) + " : " + str(player_health) +" : " + str(player_location))
    print_debug_message("DEBUG: enemy_combat_loop enemies_in_location = " +str(enemies_in_location))
    enemy_weapon = locations[player_location]["enemies"][enemy_to_fight].weapon
    print_debug_message("DEBUG: enemy_combat_loop enemy_weapon = "  + str(enemy_weapon))    
    if enemy_weapon:
        damage = enemy_weapon.attack()
        player_health -= damage
        if player_health > 0:
            print(Fore.RED, f"The {enemy_to_fight} dealt you {damage} damage, you have {player_health} left! Be careful!" + Style.RESET_ALL)
        else:
            print(Fore.RED, f"The {enemy_to_fight} dealt you {damage} damage and you have died! Better luck next time!" + Style.RESET_ALL)
            return
    return player_health
##############################
#                            #
#        Dictionaries        #
#                            #
##############################

weapon_type = {
    "sword": weapon("sword", 1, 6, "strength", 10, None),
    "axe": weapon("axe", 1, 9, "strength", 10, None),
    "bow": weapon("bow", 1, 10, "dexterity", 10, None),
    "wand": weapon("wand", 1, 7, "intelligence", 10,None )
}

enemy_info = {
    "cave goblin" : ("cave goblin", random.randint(4,6), random.choice(list(weapon_type.keys())), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(-1,0), random.randint(0,1), random.randint(-2,0), random.randint(0,3), 50),
    "forrest goblin" : ("cave goblin", random.randint(4,6), random.choice(list(weapon_type.keys())), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(-1,0), random.randint(0,1), random.randint(-2,0), random.randint(0,3), 50)
}

enemy_type = {
    "goblin": {
        "health_range": (5, 7)
    },
    "orc": {
        "health_range": (7, 10)
    }
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
            "continue": "forest",
            "turn around": "starting room"
        }
    },
    "right passageway": {
      "description": "You begin to walk down the passageway and notice that the air is becoming more and more stale the further you go. In the distance you swear you can hear the sound of something moving. Do you continue or turn around?",
      "exits": {
          "continue": "main cave hub",
          "turn around": "starting room"
      }  
    },
    "forest": {
        "description": "You see the blinding light of day growing brighter and brighter as you move quickly up the passageway until you finally emerge from the cave. Taking a second to drinkn in your surroundings you find yourself in a dense thick forrest, the sound of wild life can be heard all around. You notice an opening in the tree line straight a head and a climbable tree to the right of you. What do you do?",
        "exits": {
            "forward": "forest opening",
            "right": "tree climb",
            "turn around": "cave return"
        }
    },
    "main cave hub": {
        "description": "You step into a gaint canverness room. Water dripping from the ceiling splashes around you as you examine the area. Out of the corner of your eye you spot a green flash dart into the darkness. What do you do?",
        "exits": {
            "follow": "goblin chase",
            "turn around": "starting room"
        }
    },
    "goblin chase": {
        "description": f"Not wanting to let the mystery figure escape you begin to chase after it. Running fast through the cave, your foot steps echoing as you go, you begin to gain ground on it. Your blood is thumping in your ears as you turn a corner and finally see the figures cornered in a deadend. You are now face to face with a pair of {locations_enemy_description}. What do you do?",
        "exits": {
            "talk": "goblin talk",
            "flee": "running away",
        },
        "enemies": {
            f"goblin {i+1}": enemy(random.randint(*enemy_type["goblin"]["health_range"]), "goblin")
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

actions = {
    "go": "move",
    "move": "move",
    "walk": "move",
    "run": "move",
    "continue": "move",
    "follow": "move",
    "look": "look",
    "inspect": "look",
    "examine": "look",
    "talk": "talk",
    "speak": "talk",
    "fight": "fight",
    "attack": "fight",
    "hit": "fight"
}

inventory = {
    'sword' : 'The trusted companion for most adventurers, it is lucky you have yours with you',
    'bandages' : 'A staple of any first aid kit, try to make sure you dont need to use them!',
    'gold pieces' : 10
}

player_attacks = {
    "sword" : "1,6",
    "punch" : "1,4"
    
}   
    
player_commands = {
    'check health' : 'displays the players current health"',
    'help' : 'print the list of commands',
    'check inventory' : 'print a list of the players inventory',
    'player_teleport' : 'teleport the player to any location in the game',
    'player_set_health' : 'sets the current health of the player',
    'quit' : 'will quit the game and close it down'
}

player_stats = {
    "strength" : 2,
    "dexterity" : 3,
    "constitution" : 2,
    "intelligence" : 1,
    "wisdom" : 0,
    "charisma" : 3    
}


# game_introduction()
# game_start()

# Move the player to the new location

while True:
    #prompt the player for an input
    user_input = input("""What do you want to do?
    >""").lower()

    # Check if any of the words in the input match a key in the dictionary
    valid_direction = None
    for direction in locations[player_location]["exits"]:
        if direction in user_input:
            valid_direction = direction
            break

    # Move the player to the new location if a valid direction was found
    if valid_direction:
        player_location = move_player(player_location, valid_direction)
        player_health_change(player_location,player_health)
        #print("DEBUG: current_location = " + str(current_location))
        collect_gold(player_location,player.player_inventory)

    #player command to quit the game
    elif user_input == "quit":
        print(Fore.RED, "Thank you for playing!" + Style.RESET_ALL)
        break

    #player command to check health
    elif "check health" in user_input or "health" in user_input or "hp" in user_input:
        print("Your current health is " + str(player_health))

    #player command to show list of commands
    elif user_input == "help":
        print(Fore.BLUE, "Here is a list of commands for you: " + str(player_commands) + Style.RESET_ALL)

    #player command to set health to any value
    elif user_input.startswith("player_set_health"):
        try:
            player_health = int(user_input.split()[-1])
            print(Fore.BLUE, "Player health set to " + str(player_health) + Style.RESET_ALL)
        except ValueError:
            print("Invalid input. Please enter a valid integer value.")

    #player command to teleport to any location in the game
    elif user_input.startswith("player_teleport"):
        # Get the substring starting from the index after the first space
        teleport_location = user_input[len("player_teleport")+1:]
        # Check if the teleport location exists in the locations dictionary
        if teleport_location in locations:
            current_location = teleport_location
            player_location = current_location
            print(Fore.BLUE, "Player teleported to " + current_location + Style.RESET_ALL)
            print(locations[current_location]["description"])
        else:
            print("Invalid location!")
        
    #prints users inventory
    elif "check inventory" in user_input or "inventory" in user_input or "inv" in user_input:
        print(Fore.BLUE, 'You currently have: ' + Style.RESET_ALL)
        if len(inventory) == 0:
            print(Fore.RED, "Nothing" + Style.RESET_ALL + Fore.BLUE + "in your inventory" + Style.RESET_ALL)
        else:
            for item in inventory:
                if item != "gold pieces":
                    print(Fore.GREEN, item + Style.RESET_ALL)
                if item == "gold pieces":
                    item = str(inventory["gold pieces"]) + (" gold pieces")
                    print(Fore.GREEN, item + Style.RESET_ALL)
            print(Fore.BLUE + " in your inventory" + Style.RESET_ALL)

    #player command to add gold to the player
    elif user_input.startswith("player_add_gp"):
        try:
            inventory["gold pieces"] += int(user_input.split()[-1])
            print(Fore.BLUE, "player gold is now " + str(inventory["gold pieces"]) + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED, "Not a valid interger, please try again!" + Style.RESET_ALL)

        #Checks to see if player wants to fight
    
    #player wants to fight
    
    elif "fight" in user_input:
        try:
            if "enemies" in player_location:
                locations_enemy_description = " and ".join([enemy.enemy_type for enemy in locations[player_location]["enemies"]])
        except NameError:
            locations_enemy_description = "some enemies"
        player_init_roll = ()
        enemy_init_roll = ()
        enemy_to_fight = ()
        damage = 0
        if "enemies" not in locations[player_location]:
            print_error_message("ERROR: There are no enemies here to fight, calm down!")
            enemy_to_fight = None
        else:    
            # Call combat_loop() and assign the returned value to enemy_to_fight
            combat_result = combat_loop(player_location, player_health, player_stats, player_attacks, locations, inventory, user_input, player_init_roll, enemy_init_roll, enemy_to_fight,damage)
            if isinstance(combat_result, int):
                player_init_roll, enemy_init_roll = combat_result, combat_result
            else:
                player_init_roll, enemy_init_roll, enemy_to_fight = combat_result
            print_debug_message("DEBUG: main_loop fight enemy_to_fight = " + str(enemy_to_fight))
            if enemy_to_fight is not False:
                # Call combat_loop() again with the updated enemy_to_fight value
                combat_result = combat_loop(player_location, player_health, player_stats, player_attacks, locations, inventory, user_input, player_init_roll, enemy_init_roll, enemy_to_fight,damage)
                if isinstance(combat_result, int):
                    player_init_roll, enemy_init_roll = combat_result, combat_result
                else:
                    player_init_roll, enemy_init_roll, enemy_to_fight = combat_result
                # Update player location after the fight
                player_location = list(locations[player_location]["end_of_fight"].keys())[0]
                print_debug_message("DEBUG: player current location is " + str(player_location))
                print_debug_message("DEBUG: player_location = " + str(player_location))
                print_debug_message("DEBUG: locations[player_location]['end_of_fight] = " + str(locations[player_location]['exits']))
                print_debug_message("DEBUG: updated player_location = " + str(player_location))
        
    #command to allow player to spawn enemy
    elif user_input.startswith("player_spawn_enemy"):
        enemy_to_spawn = user_input[len("player_spawn_enemy")+1:]
        if current_location not in locations:
            locations[current_location] = {}
        if "enemies" not in locations[current_location]:
            locations[current_location]["enemies"] = {}
        if enemy_to_spawn in enemy_info:
            locations[current_location]["enemies"][enemy_to_spawn] = enemy_info[enemy_to_spawn]
            print(f"You have spawned a {enemy_to_spawn} in {current_location}")
            print(locations[current_location])
        else:
            print(f"Can not spawn a {enemy_to_spawn} in {current_location}")

    #command to print player location
    elif user_input.lower() == "print_player_location":
        print_debug_message("DEBUG: player current location is " + str(player_location))
        

    #prints error message if the location is not correct
    else:
        print("You cannot go that way.")

    #ends the game if the player health falls to or below 0
    if player_health <= 0:
        print(Fore.RED, "Game over!" + Style.RESET_ALL)
        break



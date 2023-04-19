# Systems to impliment

# Magic system
    - [x] Magic uses player or enemy health to cast magic. More power than normal weapons but costly.
    - [ ] new spells can be learnt in the game at key points

# journal system
    - [ ] allows player to keep track of the story and what hey should be doing next
    - [ ] updated at key points in the story
    - [ ] possibly open in new window
    - [ ] different transportation types

# looting mechanics
    - [ ] able to loot areas if they have items in them
        - [ ] possible to find hidden locations by 'searching' around the room
    - [ ] able to get loot from battles

# shopping
    - [ ] shops can be found in towns and cities
        - [ ] also found in special locations

# random encounters during journeys 
    - [ ] when travelling through large areas or between towns/cities
    - [ ] randomised enemies at encounters 

# enemies stats
    - [x] all enemy types have stats
    - [x] stats influence the damage of enemies

# armour system
    - [ ] armour can be 'worn' if in inventory
    - [ ] armour values are subtracted from damage rolls to help 'block' some damage
    - [ ] add ability to reduce certain types of damage

# healing mechanics 
    - [ ] items can heal the player
        - [ ] items have a range they can heal
        - [ ] randomised everytime they are used
        - [ ] Int or wis added to roll

# player leveling
    - [ ] all enemies have a 'xp' value
    - [ ] when defeated 'xp' added to player 'xp'
    - [ ] xp resets after certain thresh hold met
        - [ ] thresh hold increases everytime it is met

# resting mechanic
    - [ ] regain any lost health
    - [ ] requires camping gear in invetory
        - [ ] or inn nearby

# additional weapon affects
    - [ ] enchanted weapons can do more damage of a different type
        - [ ] these types can by pass standard armour defences


# Magic system:
You could create a Player and Enemy class with attributes such as health and magic_power. When a player or enemy uses magic, their health decreases by a certain amount depending on the power of the spell. You could also create a Spell class that has attributes such as name, power, and cost. The player could learn new spells by interacting with NPCs or by finding spell books in the game world.

# Journal system:
You could create a separate Journal class that allows the player to keep track of the story and objectives. You could update the journal at key points in the story by printing out relevant information to the player or by prompting them to update their journal. You could also provide an option for the player to open the journal in a new window.

# Looting mechanics:
You could create a Room class that contains a list of items that can be looted. You could also add a search method to the Room class that allows the player to search for hidden items. You could randomly generate loot drops from defeated enemies as well.

# Shopping:
You could create a Shop class that has a list of items that the player can purchase using in-game currency. You could also add shops to certain locations in the game world and make certain items available only in certain shops.

# Random encounters during journeys:
You could create a Map class that contains a list of locations that the player can travel to. When the player travels between locations, you could randomly generate encounters with enemies. You could also create a Travel class that allows the player to make decisions during their journey that affect the outcome of the encounter.

# Enemies stats:
You could create an Enemy class with attributes such as name, health, and damage. The enemy's stats could be used to determine how much damage they can deal to the player.

# Armour system:
You could create an Armour class with attributes such as name and defence. When the player wears armour, the defence value could be subtracted from the enemy's damage rolls to reduce the amount of damage taken.

# Healing mechanics:
You could create a HealingItem class with attributes such as name and healing_power. The healing item's healing power could be randomized each time it is used, and the player's intelligence or wisdom could be added to the healing roll to determine the amount of healing received.

# Player leveling:
You could add an xp attribute to the Player class and increment it by the enemy's xp value when the player defeats an enemy. When the player reaches a certain xp threshold, you could reset their xp and increase the threshold to make it harder to level up. You could also add a level attribute to the Player class that increases each time the player levels up, and grants them new abilities or attributes.
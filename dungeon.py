
import random


hero_stats = {
    "name" : "hero",
    "strength" : 7,
    "health" : 100.0,
}
hero_max_health = 100.0

health_potion_strength = 5 
hero_inventory = ["rope","sword","health potion","health potion"]

def quit():
    print ("You chose to Flee")
    print ("GAME OVER")
    return False

def player_stats ():
    print ("You are:")
    for key , value in hero_stats.items():
        print(f"{key} : {value}" )
    
def take_damage():
    hero_stats["health"] = hero_stats["health"] - 35
    return 

def player_move():
    print("\nYou Moved\n")

def player_attack():
    strength = (hero_stats["strength"])
    print(strength)
    crit = random.randint(1,2)
    damage = str(strength * crit) 
    print("\nYou Attacked and did", damage, "damage.\n")

def player_use():
    pass

def player_heal(item_name):

    print(f"You have", {hero_inventory.count("health potion")},f"{item_name}s")

    if (hero_inventory.count("health potion") <= 0):
        print(f"You don't have any {item_name}s")
        return
    
    elif (hero_stats["health"] >= hero_max_health):
        print("You've already reached max health")
        hero_stats["health"] = hero_max_health
        return

    hero_stats["health"] = hero_stats["health"] + (health_potion_strength * 4)

    if (hero_stats["health"] > hero_max_health):
        hero_stats["health"] = hero_max_health

    print(f"Your health is now {hero_stats['health']}")
    hero_inventory.remove("health potion") 
    print(f"Your inventory now is: {hero_inventory}")


def use_item():
    item_name = input(f"What item do you want to use? {hero_inventory}\n").lower()
    print (f"The item you want to use is {item_name}")
    
    match item_name: 
        case "sword":
            pass
        case "health potion":
           player_heal(item_name)
        case "rope":
            pass
        case _:
            print(f"{item_name} is not in your invetory")

isPlaying = True

while(isPlaying):

    print("\nSTART OF LOOP\n")

    attacked = random.randint(0,1)
    if (attacked == 1):
        print("You have been attacked")
        take_damage()
        if (hero_stats["health"] <= 0 ):
            print("You have died")
        print(f"You now have {hero_stats['health']} health")

    player_stats()
    
    action = input ("\nSelect Action: Attack, Use item, Move & Flee\n").lower()

    print(f"Player Action: {action}")

    if (action == "flee"):
        isPlaying = quit() #isPlaying = false
    
    elif (action == "move"):
         player_move()
    
    elif (action == "use item"):
        use_item() 

    elif (action == "attack"):
        player_attack()

    else:
        print("INVALID ACTION")

print ("END OF LOOP")
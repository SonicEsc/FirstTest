
hero_stats = {
    "name" : "hero",
    "strength" : 7,
    "health" : 100.0,
}

def quit():
    print ("You chose to Flee")
    print ("GAME OVER")
    return False

def player_stats ():
    print ("You are:")
    for key , value in hero_stats.items():
        print(f"{key} : {value}" )
    
def player_move():
    print("\nYou Moved\n")

def player_attack():
    print("\nYou Attacked\n")

isPlaying = True

while(isPlaying):

    print("\nSTART OF LOOP\n")

    player_stats()
    
    action = input ("\nSelect Action: Attack, Move & Flee\n").lower()

    print(f"Player Action: {action}")

    if (action == "flee"):
        isPlaying = quit() #isPlaying = false
    
    elif (action == "move"):
         player_move()

    elif (action == "attack"):
        player_attack()

    else:
        print("INVALID ACTION")

print ("END OF LOOP")
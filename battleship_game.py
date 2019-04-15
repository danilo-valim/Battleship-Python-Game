# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 21:09:52 2018

@author: DANILO SALES VALIM
@website: http://danilovalim.com

Purpose:
    Development of the classic board game called Battleship in order to 
    implement the concepts of functions, matrices, string manipulation,
    dataframes, lists and  loops. The game has three stages where 
    the player has to guess where the ships are located in the enemy matrix. 
    If the guess is correct, the player sinks the enenmy ship, if not, the bot 
    will randomly guess a position in the player's matrix. Whoever sinks the 
    whips first, win. The last stage, the player has to guess in wich row the 
    ship is, for each column of the matrix.
"""

#Function to install/import the packages required
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

#CALL THE REQUIRED PACKAGES
install_and_import('pandas')
install_and_import('os')
install_and_import('string')
install_and_import('random')
install_and_import('sys')
install_and_import('colorama')
install_and_import('string')

#DEFINE KEY VARIABLES
water = '~~~~'
ship = '◄■◙■'
hit = '☼☼☼☼'
not_hit = '   '

#SET GLOBAL VARIABLES
global player_sea, enemy_sea, enemy_sea_display, player, mission, sea_sizer

#RANDOMLY POPULATE A MATRIX WITH SHIPS AND WATER
def sea_builder(size, hidden):
    row = []
    if hidden == True:
        for i in range(0, size):
            row.append(water)
        return(row)
    else:
        for i in range(0, size):
            row.append(random.choice([water]*80 + [ship]*20))
        return(row)

#PLACE THE SHIPS RANDOMLY ON THE MAP (SEA)
def spawn_ships(sea):
    i = 0
    while i < len(sea):
        selection = []
        row = random.choice(range(0,len(sea)))
        col = random.choice(range(0,len(sea)))
        selection.append([row, col])
        if sea[int(row)][int(col)] == water:
           sea[int(row)][int(col)] = ship
           i += 1

#PRINT THE MAPS
def show_maps(map1, map2, cls):
    global mission
    if cls == True:
        clear()

    print(f"""{colorama.Fore.BLACK}{colorama.Back.WHITE}
            \\BATTLESHIP/ Mission {mission}                   
{colorama.Style.RESET_ALL}
_____________________________________________________
{colorama.Fore.WHITE}{colorama.Back.BLUE}
   U.S {colorama.Style.RESET_ALL} Navy Fleet = {remaining_ships(map1)} {ship}

{pandas.DataFrame(map1)}
_____________________________________________________
{colorama.Fore.WHITE}{colorama.Back.RED}
   URSS {colorama.Style.RESET_ALL} Navy Fleet = {remaining_ships(enemy_sea)} {ship} (enemy)

{pandas.DataFrame(map2)}
_____________________________________________________
  {water} Water | {ship} Ship | {hit} Destroyed Ship
  
  """)

#CHECK IF MATRIX HAS SHIPS
def remaining_ships(sea):
    result = 0
    for i in range(0,len(sea)):
        result += sea[i].count(ship)
    return result

#RANDOMLY SELECT MATRIX FOR THE ENEMY TURN
def bot_turn():
    selection = []
    show_maps(player_sea, enemy_sea_display, True)
    row = random.randint(0, sea_size-1)
    col = random.randint(0, sea_size-1)
    selection.append([row, col])
    
    if [row, col] in selection:
        if player_sea[int(row)][int(col)] == ship:
            #RANDOM COORDINATE IS A SHIP
            player_sea[int(row)][int(col)] = hit
            #REFRESH THE SCREEN WITH NEW MAPS
            show_maps(player_sea, enemy_sea_display, True)
            print("\nEnemy's turn")
            print(f"\n{colorama.Fore.WHITE}{colorama.Back.RED}"+
            "Uh-oh! Enemy torpedo sank one of our ship!"+
            f"{colorama.Style.RESET_ALL}")
            #bot_turn()
        elif player_sea[int(row)][int(col)] == hit:
            #RANDOM COORDINATE HAS BEEN CHOSEN YET
            player_sea[int(row)][int(col)] = hit
            print("\nURSS fired back")
            print("\nLuckly, their torpedo hit a sunk ship!")
        else:
            #RANDOM COORDINATE IS WATER
            player_sea[int(row)][int(col)] = not_hit
            #REFRESH THE SCREEN WITH NEW MAPS
            show_maps(player_sea, enemy_sea_display, True)
            print("\nURSS fired back")
            print(f"\nLuckly, their torpedo hit the water!")
        
#CLEAR THE SCREEN BOTH FOR WINDOWS AND MAC OS
def clear():
    if os.name == 'nt':
        #WINDOWS
        os.system('cls')
    else:
        #MAC 
        os.system('clear')


################################## INITIAL PAGE ###############################

def game_start():

    clear()
    #sys.stdout.write("\x1b[8;{rows};{cols}t".format(cols=100, rows = 55))
    print(f"""
    ▄▄▄   ▄▄  ▄▄▄ ▄▄▄ ▄  ▄▄▄ ▄▄▄ ▄  ▄ ▄ ▄▄▄                          _   _____\|/____   _
    █  █ █  █  █   █  █  █   █   █  █ ▄ █  █                  _=====| | |            | | |====
    █  █ █▄▄█  █   █  █  █▄  █▄▄ █▄▄█ █ █  █            =====| |.---------------------------.
    █▀▀▄ █  █  █   █  █  █     █ █  █ █ █▀▀     <--------------'    o     o     o     o     '--------------/
    █  █ █  █  █   █  █  █     █ █  █ █ █        \                                                 URSS   /
    ▀▀▀  ▀  ▀  ▀   ▀  ▀▀ ▀▀▀ ▀▀▀ ▀  ▀ ▀ ▀         \______________________________________________________/
          ©Danilo Valim - 2018                      \|/   
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~_~~~~~~~~~~~~~~~~~~~U~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                    /_\                  |
                                                    |_|                  |
                                                    |_|                 _|__                    o
                                                    /v\                |_|   \                   __o
                                                    o                  |      \                |X__>
                                                      o        ________|_______\__________
                                                 __o__________/                           \____________    _
                                                /                                                      \  (_)
                                                \       0    0     0                           USA      >--)
                                                 \_____________________________________________________/  (_)


    """)
    #ASK FOR PLAYER'S NAME
    global player
    player = input("Please insert player's name: ")
    clear()

    #STORY INTRODUCTION
    print(f"""
          
    Welcome {player}!
                                                        _________
    The U.S. Navy is glad to have have you             |░ ░ ░ ░ ░|
    as a Fleet Commander!                              |░ ░ ░ ░ ░|         ||* * * * * * ░░░░░░░░░░░░░░░░░░░░░
                                                       |░ ░ ░ ░ ░|         || * * * * *
    URSS ships are planning an attack against          |░ ░ ░ ░ ░|         ||* * * * * * ░░░░░░░░░░░░░░░░░░░░░
    our nation. We have to stop them by destroying     |░ ░ ░ ░ ░|         || * * * * *
    all their ships. Your job is to give the           |░ ░ ░ ░ ░|         ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    coordinates where you think the enemy ships       ===============      ||
    are so that we can launch torpedos against them.   // _   _ \\\         ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                       (| O   O |)         ||
    Once you hit a ship, you can launch                /|   U   |\         ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    a second one before they have the chance            |  \=/  |          ||
    to fire back. If you miss the shot, then they        \_..._/           ||
    will launch torpedo against our fleet.               _|\\v/|_           ||
                                                 _______/\| v |/\_______   ||
                                                /       \ \   / /       \  ||
    {colorama.Fore.WHITE}{colorama.Back.BLUE} U.S  {colorama.Style.RESET_ALL} table shows your fleet              |         \ | | /         | ||
    {colorama.Fore.WHITE}{colorama.Back.RED} URSS {colorama.Style.RESET_ALL} table shows enemy fleet             |          ||o||          | ||
                                               |    |     ||o||     |    | ||
                                               |    |     ||o||     |    | ||
    """)
    input("\n                              <Press Enter to start the mission>")
    
    #STARTS FIRST MISSION
    global sea_size
    stage1_starts(sea_size)

######################## STAGE 1 AND 2 (MISSION 1 AND 2)#######################

def stage1_starts(sea_size):
    clear()
    
    #SET KEY VARIABLES
    global player_sea, enemy_sea, enemy_sea_display, player, mission
    mission += 1
    player_sea = []
    enemy_sea = []
    enemy_sea_display = []
    
    #CREATE PLAYER'S MAP AND BOT'S MAP (ONE HIDDEN AND ONE ACTUAL MAP)
    for i in range(0, sea_size):
        #CREATES PLAYER'S MAP
        player_sea.append(sea_builder(sea_size, True))
        #CREATES BOT'S MAP (THE ONE THAT PLAYER CAN'T SEE)
        enemy_sea.append(sea_builder(sea_size, True))
        #CREATES BOT'S MAP (THE ONE THAT PLAYER SEES ON THE SCREEN)
        enemy_sea_display.append(sea_builder(sea_size, True))

    #SPWAN THE SHIPS RANDOMLY ON THE MAP
    spawn_ships(player_sea)
    spawn_ships(enemy_sea)

    #
    keep_playing = 'Y'
    while keep_playing != 'N':
        #DISPLAYS THE MAPS
        show_maps(player_sea, enemy_sea_display, True)
        
        #ASK THE PLAYER FOR THE COORDINATES
        print("\nThat's your turn to launch a torpedo")
        rowIndex = input("\nEnter the row coordinate:")
        colIndex = input("Enter the column coordinate:")
        
        #CHECK IF INPUT IS VALID (NOT CHAR AND WITHIN MAP RANGE)
        while rowIndex.isnumeric() is not True or int(rowIndex) not in range(0, sea_size):
            print(f"\nInvalid coordinates Sir! Please enter coordinates "+
                  f"between 0 and {sea_size-1}. Roger!")
            rowIndex = input("\nEnter the ROW coordinate:")
        
        #CHECK IF INPUT IS VALID (NOT CHAR AND WITHIN MAP RANGE)
        while colIndex.isnumeric() is not True or int(colIndex) not in range(0, sea_size):
            print(f"\nInvalid coordinates Sir! Please enter coordinates"+
                  f"between 0 and {sea_size-1}. Roger!")
            colIndex = input("\nEnter the COL coordinate:")
                            
        #CHECK IF COORDINATE HITS A ENEMY'S SHIP
        if enemy_sea[int(rowIndex)][int(colIndex)] == ship:
                enemy_sea[int(rowIndex)][int(colIndex)] = hit
                enemy_sea_display[int(rowIndex)][int(colIndex)] = hit
                #REFRESH THE MAP
                show_maps(player_sea, enemy_sea_display, True)
                print(f"\n{colorama.Fore.WHITE}{colorama.Back.BLUE}Nice job "+
                      f"{player}! Your torpedo sank an enemy ship!"+
                      f"{colorama.Style.RESET_ALL}")
                input("\n<Continue>")
                #CHECK IF PLAYER WINS
                if remaining_ships(enemy_sea) < 1:
                    clear()
                    stage1_ends()
                    break
        
        #CHECK IF COORDINATE HITS A HIT SHIP (PLAY AGAIN)
        elif enemy_sea[int(rowIndex)][int(colIndex)] == hit:
                 enemy_sea[int(rowIndex)][int(colIndex)] = hit
                 print("\nWe hit a sunk ship Sir, "+
                       "try again before anybody notice it")

        else:   #CHECK IF COORDNATE HITS WATER (BOT'S TURN STARTS)
                enemy_sea_display[int(rowIndex)][int(colIndex)] = not_hit
                #REFRESH THE MAP
                show_maps(player_sea, enemy_sea_display, True)
                print("\nBad shot Sir, your torpedo did not hit an "+
                      "enemy ship! Copy.")
                input("\n<Continue>")
                #STARTS BOT'S TURN
                bot_turn()
                
        #CHECK IF GAME IS OVER
        if remaining_ships(player_sea) < True:
            clear()
            fail()
            #STOP LOOP
            keep_playing = 'N'
            break
        keep_playing = input("\n<Continue>")


#STAGE 1 PR 2 PASSED
def stage1_ends():
    global player
    
    global sea_size
    
    #STAGE 2 PASSED
    if sea_size >= 4:
        #STARTS LAST STAGE
        last_mission_starts()
    
    print(f"""

    Mission Passed!
    Good job {player}!
                                                         _________
    You have secessfuly destroyed all the enemy ships!  |░ ░ ░ ░ ░|          ||* * * * * * ░░░░░░░░░░░░░░░░░░░░░
                                                        |░ ░ ░ ░ ░|          || * * * * *
    However, our secret service descovered that URSS is |░ ░ ░ ░ ░|          ||* * * * * * ░░░░░░░░░░░░░░░░░░░░░
    planning a second attack. This time their fleet     |░ ░ ░ ░ ░|          || * * * * *
    is larger. We have positioned the same number       |░ ░ ░ ░ ░|          ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    of U.S. ships in the region. Your job is to       ===============        ||
    do the same as before: destroy them all!            // _   _ \\\          ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                        (| O   O |)          ||
                                                        /|   U   |\          ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                         |  \=/  |           ||
                                                          \_..._/            ||
                                                          _|\\v/|_            ||
                                                  _______/\| v |/\_______    ||
                                                 /       \ \   / /       \   ||
                                                |         \ | | /         |  ||
                                                |          ||o||          |  ||
                                                |    |     ||o||     |    |  ||
                                                |    |     ||o||     |    |  ||
    """)
    input("\n                              <Press Enter to start the mission>")
    
    sea_size += 2
    if sea_size <= 4:
        stage1_starts(sea_size)

#LAST STAGE FUNCTION
def last_mission_starts():
    global player
    
    #STAGE INTRO
    print(f"""

    Mission Passed!
    Good job {player}!
                                                         _________
    You seemed to have destroyed all the enemy ships!   |░ ░ ░ ░ ░|          ||* * * * * * ░░░░░░░░░░░░░░░░░░░░░
                                                        |░ ░ ░ ░ ░|          || * * * * *
    However, our radar identified that one URSS ship    |░ ░ ░ ░ ░|          ||* * * * * * ░░░░░░░░░░░░░░░░░░░░░
    scaped and it is moving towards our coast. The      |░ ░ ░ ░ ░|          || * * * * *
    ship is moving in Zip-Zags. Our radar is no longer  |░ ░ ░ ░ ░|          ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    working fine and we have only 7 torpedos left,    ===============        ||
    so only you have 7 chances to sink the ship        // _   _ \\\           ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    before it reaches the limit of our radar range.     (| O   O |)          ||
                                                        /|   U   |\          ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                         |  \=/  |           ||
     ' ↑ ' shows the latitude the ship is located.        \_..._/            ||
     You have to give the longitude coordinate.           _|\\v/|_            ||
                                                  _______/\| v |/\_______    ||
                                                 /       \ \   / /       \   ||
                                                |         \ | | /         |  ||
                                                |          ||o||          |  ||
                                                |    |     ||o||     |    |  ||
                                                |    |     ||o||     |    |  ||
    """)
    input("\n                              <Press Enter to start the mission>")
    last_mission()

#LAST STAGE STARTS
def last_mission():
    clear()
    ship = '■◙■►'
    hit = '☼☼☼☼'
    #NUMBER OF ROWS
    depth = 4
    depth_list = list(range(depth))
    depth_list.append('')
    
    #LIST TO CONVERT NUMERICAL COORDINATES INTO CHAR COORDINATES
    alphabet = list(string.ascii_uppercase)
    
    #STATIC MAP (5 ROWS X 8 COLS)
    river = {'A':['~~~~','~~~~','~~~~','~~~~',' ↑ '],
              'B':['~~~~','~~~~','~~~~','~~~~',''], 
              'C':['~~~~','~~~~','~~~~','~~~~',''], 
              'D':['~~~~','~~~~','~~~~','~~~~',''], 
              'E':['~~~~','~~~~','~~~~','~~~~',''],
              'F':['~~~~','~~~~','~~~~','~~~~',''],
              'G':['~~~~','~~~~','~~~~','~~~~',''],
              '':depth_list}
    
    #TRANSFORM MAP INTO A DATAFRAME     
    river_df = pandas.DataFrame(river).set_index('')
    
    #GIVES THE PLAYER 8 CHANGES TO HIT THE SHIP
    for i in river_df.columns:
        #ADJUST THE ARROW POSITION THAT INDICATES THE COLUMN TO GUESS
        if alphabet.index(i) > 0:
            river_df[alphabet[alphabet.index(i)-1]][depth] = ''
        if alphabet.index(i) in range(1, len(river_df.columns)):
            river_df[alphabet[alphabet.index(i)]][depth] = ' ↑ '
        
        #DISPLAYS THE MAP
        print(river_df)
        #RANDOMLY SPAWNS A SHIP IN THE I COLUMN
        rand = random.randint(0,depth-1)
        river_df[i][rand] = ship
        
        #ASKS PLAYER TO INPUT GUESS
        row = input(f"\n{player}, choose the row (between 0 and {depth-1}): ")
        
        #CHECK IF PLAYER'S INPUT IS NUMERIC AND WITHIN THE RANGE
        while row.isnumeric() is not True or int(row) not in range(0, depth):
                print(f"\nInvalid coordinates Sir! Please enter coordinate "+
                      f"between 0 and {depth-1}. Roger!")          
                row = input(f"\n{player}, choose the row (between 0 and "+
                            f"{depth-1}): ")
        
        clear()
        
        #CHECK IF PLAYER'S GUESS HAS HIT A SHIP
        if river_df[i][int(row)] == ship:
            river_df[i][int(row)] = hit
            print(river_df)
            input(f"{colorama.Fore.WHITE}{colorama.Back.BLUE}Congratulations "+
                  f"{player}! You destroyed the remaining ship "+
                  f"{colorama.Style.RESET_ALL}")
            win()
            break
        else:
            print(f"\n{colorama.Fore.WHITE}{colorama.Back.RED}"+
                  f"You missed the shot Sir, the ship was in Longitude "+
                  f"{rand} and still moving forward{colorama.Style.RESET_ALL}")
            
            #CHECK IF GAME IS OVER
            if i == 'G':
                fail()
                break
        

#PLAYER WINS THE GAME
def win():
    global player, mission, sea_size
    clear()
    
    print(f"""                                                           
    |░░░░|     |░░░░|                                             
    \░░░░|     |░░░░/       Nice Job {player}! YOU WON!                     
     \░░░|     |░░░/                                              
      \░░|_____|░/          You conquered the peace for our nation.
           (O)              Here is your medal as a recognition for
         .--""--.           your amazing job!             
       /'  *  *  `\	                                              
      |~ COMBATANT |        
      | ~  AWARD ~ | 
       \ * ~~~~ * /  
        `.______,'	
     

   Remeber:        
   "We make war that we may live in peace" 
                              - Aristotle


""")
    #OPTION TO PLAY AGAIN
    decision = input(" Choose:\n 1 = I want more war, I mean...more peace\n "+
                     "2 = I want to retire\n:>")
    if decision == '1':
        #RESTART STAGE CONTROL VARIABLES
        mission = 0
        sea_size = 2        
        game_start()
    else:
        exit()
        
     
#PLAYER FAILS THE GAME
def fail():
    global player, mission, sea_size
    print(f"""
        
     Mission Failed {player}!
                                                             _________
     You were not able to stop the attack.                  |░ ░ ░ ░ ░|       ||
                                                            |░ ░ ░ ░ ░|       ||
                                                            |░ ░ ░ ░ ░|       ||
                                                            |░ ░ ░ ░ ░|       ||
                                                            |░ ░ ░ ░ ░|       ||* * * * * * ░░░░░░░░░░░░░░░░░░░░░
                                                          ===============     || * * * * *
                                                              /*****\         ||* * * * * * ░░░░░░░░░░░░░░░░░░░░░
                                                             | x   x |        || * * * * *
                                                             (   0   )        ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                              \ ### /         ||
                                                               \___/          ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                                 8            ||
                                                            ____ 8 ____       ||░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                                          /      8     \      ||
                                                         |       8      |     ||
                                                         |       8      |     ||
                                                         |       8      |     ||
                                                        /|\      8     /|\    || """)
    
    #OPTION TO PLAY AGAIN
    decision = input("1)Play again\n2)Retire\n")
    if decision == '1':
        #RESET STAGE CONTROL VARIABLES
        mission = 0
        sea_size = 2        
        game_start()
    else:
        exit()
    

#VARIABLES FOR STAGE CONTROL
mission = 0
sea_size = 2

#STARTS THE GAME
game_start()
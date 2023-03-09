import Pokemon
import random

# Intro to game
print('\nWelcome to Pokemon Colosseum!\n')

# Insert player name
playerName = input('Enter your name: ')
print('\n')

# Assigns random numbers 0 - 81 for a, b, c, x, y, z to store pokemon value
a = random.randint(0, 81)
b = random.randint(0, 81)
while b == a:
    b = random.randint(0, 81)
c = random.randint(0, 81)
while c == a or c == b:
    c = random.randint(0, 81)

x = random.randint(0, 81)
y = random.randint(0, 81)
while y == x:
    y = random.randint(0, 81)
z = random.randint(0, 81)
while z == x or z == y:
    z = random.randint(0, 81)

# Finds attributes for selected move
def movesList(moveSelected):
    movesList.moves = Pokemon.mname # assigned move names in an array
    tick = 0

    while movesList.moves[tick] != moveSelected and tick < 50:
        tick = tick + 1 # Ticks through array until finds a match with move selected
        try:
            moveSelected = moveSelected.replace(' ', '')
        except AttributeError:
            continue
        try:
            movesList.moves[tick] = movesList.moves[tick].replace(' ', '')
        except AttributeError:
            continue
    return tick # Returns location of move

# Declares team Rockets pokemon in play
def teamRocketPokemon():
    teamRocketPokemon.rocketPoke = [a, b, c]
    teamRocketPokemon.rocketType = [a, b, c]
    teamRocketPokemon.rocketDef = [a, b, c]
    teamRocketPokemon.rocketAtt = [a, b, c]
    teamRocketPokemon.rocketHP = [a, b, c]
    teamRocketPokemon.rocketPower = [a, b, c]

# Determines which move team rocket will use and blocks them from using the same moves within 5 turns
def teamRocketMoves(rocketBlock, mov):
    if mov == 0:
        rocketMoves = Pokemon.pmoves[a].split(',')
    elif mov == 1:
        rocketMoves = Pokemon.pmoves[b].split(',')
    elif mov == 2:
        rocketMoves = Pokemon.pmoves[c].split(',')

    t = 0
    while t <= 4:
        try:
            rocketMoves[t] = rocketMoves[t].replace("'", "")
        except AttributeError:
            continue

        try:
            rocketMoves[t] = rocketMoves[t].replace("[", "")
        except AttributeError:
            continue

        try:
            rocketMoves[t] = rocketMoves[t].replace("]", "")
        except AttributeError:
            continue

        try:
            rocketMoves[t] = rocketMoves[t].replace('"', "")
        except AttributeError:
            continue
        t += 1

    choice = random.randint(1, 5) # Chooses random move

    n = 0
    # Checks if move has been used
    while n == 0:
        if choice == 1 and rocketBlock[0] == 1:
            choice = random.randint(1, 5)
        elif choice == 1 and rocketBlock[0] == 0:
            n = 1
        if choice == 2 and rocketBlock[1] == 2:
            choice = random.randint(1, 5)
        elif choice == 2 and rocketBlock[1] == 0:
            n = 1
        if choice == 3 and rocketBlock[2] == 3:
            choice = random.randint(1, 5)
        elif choice == 3 and rocketBlock[2] == 0:
            n = 1
        if choice == 4 and rocketBlock[3] == 4:
            choice = random.randint(1, 5)
        elif choice == 4 and rocketBlock[3] == 0:
            n = 1
        if choice == 5 and rocketBlock[4] == 5:
            choice = random.randint(1, 5)
        elif choice == 5 and rocketBlock[4] == 0:
            n = 1

        if rocketBlock == [1, 2, 3, 4, 5]:
            rocketBlock = [0, 0, 0, 0, 0]
        if choice == 1:
            rocketBlock[0] = 1
        if choice == 2:
            rocketBlock[1] = 2
        if choice == 3:
            rocketBlock[2] = 3
        if choice == 4:
            rocketBlock[3] = 4
        if choice == 5:
            rocketBlock[4] = 5

    # Returns random move selected
    match choice:
        case 1:
            return rocketMoves[0]
        case 2:
            return rocketMoves[1]
        case 3:
            return rocketMoves[2]
        case 4:
            return rocketMoves[3]
        case 5:
            return rocketMoves[4]

# Declares player pokemon
def playerPokemon():
    playerPokemon.playerPoke = [x, y, z]
    playerPokemon.playerType = [x, y, z]
    playerPokemon.playerDef = [x, y, z]
    playerPokemon.playerAtt = [x, y, z]
    playerPokemon.playerHP = [x, y, z]

# Determines which move team rocket will use and blocks them from using the same moves within 5 turns
def teamPlayerMoves(blocked, mov):
    if mov == 0:
        playerMoves = Pokemon.pmoves[x].split(',')
    elif mov == 1:
        playerMoves = Pokemon.pmoves[y].split(',')
    elif mov == 2:
        playerMoves = Pokemon.pmoves[z].split(',')
    t = 0
    while t <= 4:
        try:
            playerMoves[t] = playerMoves[t].replace("'", "")
        except AttributeError:
            continue

        try:
            playerMoves[t] = playerMoves[t].replace("[", "")
        except AttributeError:
            continue

        try:
            playerMoves[t] = playerMoves[t].replace("]", "")
        except AttributeError:
            continue

        try:
            playerMoves[t] = playerMoves[t].replace('"', "")
        except AttributeError:
            continue
        t += 1
    # Checks if user has used a move and blocks it
    if blocked == [0, 0, 0, 0, 0]:
        blocked = [1, 2, 3, 4, 5]

    if blocked[0] == 0:
        print('1. ' + playerMoves[0] + '(N/A)')
    else:
        print('1. ' + playerMoves[0])
    if blocked[1] == 0:
        print('2.' + playerMoves[1] + '(N/A)')
    else:
        print('2.' + playerMoves[1])

    if blocked[2] == 0:
        print('3.' + playerMoves[2] + '(N/A)')
    else:
        print('3.' + playerMoves[2])

    if blocked[3] == 0:
        print('4.' + playerMoves[3] + '(N/A)')
    else:
        print('4.' + playerMoves[3])

    if blocked[4] == 0:
        print('5.' + playerMoves[4] + '(N/A)')
    else:
        print('5.' + playerMoves[4])

    choice = input()
    m = 0
    while m == 0:
        if choice == '1' and blocked[0] == 0:
            choice = input('Please enter a move that has not been used yet: ')
        elif choice == '1' and blocked[0] == 1:
            break
        if choice == '2' and blocked[1] == 0:
            choice = input('Please enter a move that has not been used yet: ')
        elif choice == '2' and blocked[1] == 2:
            break
        if choice == '3' and blocked[2] == 0:
            choice = input('Please enter a move that has not been used yet: ')
        elif choice == '3' and blocked[2] == 3:
            break
        if choice == '4' and blocked[3] == 0:
            choice = input('Please enter a move that has not been used yet: ')
        elif choice == '4' and blocked[3] == 4:
            break
        if choice == '5' and blocked[4] == 0:
            choice = input('Please enter a move that has not been used yet: ')
        elif choice == '5' and blocked[4] == 5:
            break

        # Prompts user to enter a number if their previous choice was outside 1 - 5 or a letter
        if 65 <= ord(choice) <= 90 or 97 <= ord(choice) <= 122 or int(choice) < 1 or int(choice) > 5:
            if 65 <= ord(choice) <= 90 or 97 <= ord(choice) <= 122:
                print('Please do not enter a letter, a number 1 - 5 is all that is required.')
            choice = input('\nPlease select a number that is provided above: ')

    # Blocks move if used
    if choice == '1':
        blocked[0] = 0
    if choice == '2':
        blocked[1] = 0
    if choice == '3':
        blocked[2] = 0
    if choice == '4':
        blocked[3] = 0
    if choice == '5':
        blocked[4] = 0


    print('Team ' + playerName + "'s choice: ", choice)
    # returns move
    match choice:
        case '1':
            return playerMoves[0]
        case '2':
            return playerMoves[1]
        case '3':
            return playerMoves[2]
        case '4':
            return playerMoves[3]
        case '5':
            return playerMoves[4]

# Chooses which player goes first 50/50
def coinToss():
    teamRocket = 0
    teamPlayer = 1

    winner = random.randint(0, 1)
    if winner == teamRocket:
        return teamRocket
    if winner == teamPlayer:
        return teamPlayer


teamRocketPokemon()
playerPokemon()

# Calculates the damage of an attack
def damageEq(P, A, D, attType, attPokeType, defPokeType):
    TE = 1
    STAB = 1
    P = int(P)
    A = int(A)
    D = int(D)
    # Determines if move type is the same as attacking pokemon type
    if attType == attPokeType:
        STAB = 1.5

    # Determines if move should be increased/decreased base of move type and defense pokemon type
    if attType == 'Fire' and defPokeType == 'Fire':
        TE = .5
    if attType == 'Fire' and defPokeType == 'Water':
        TE = .5
    if attType == 'Fire' and defPokeType == 'Grass':
        TE = 2

    if attType == 'Water' and defPokeType == 'Fire':
        TE = 2
    if attType == 'Water' and defPokeType == 'Water':
        TE = .5
    if attType == 'Water' and defPokeType == 'Grass':
        TE = .5

    if attType == 'Electric' and defPokeType == 'Electric':
        TE = .5
    if attType == 'Electric' and defPokeType == 'Water':
        TE = 2
    if attType == 'Electric' and defPokeType == 'Grass':
        TE = .5

    if attType == 'Grass' and defPokeType == 'Fire':
        TE = .5
    if attType == 'Grass' and defPokeType == 'Water':
        TE = 2
    if attType == 'Grass' and defPokeType == 'Grass':
        TE = .5

    # Assigns random decimal
    r = random.uniform(.5, 1)
    # Calculates damage
    damage = P * (A / D) * STAB * TE * r
    # Returns Damage
    return damage

# Func that delivers the gameplay
def gamePlay():
    turn = coinToss()
    playerPokeCount = 3 # Keeps count on living pokemon
    rocketPokeCount = 3 # Keeps count on living pokemon
    blocked = [1, 2, 3, 4, 5]
    rocketBlock = [0, 0, 0, 0, 0]
    e = 0 # is used to call specific pokemon based off the variables a, b, c
    f = 0 # is used to call specific pokemon based off the variables x, y, z
    temp = 0
    if turn == 0:
        print('Coin toss goes to ---- Team Rocket to start the attack')
    if turn == 1:
        print('Coin toss goes to ---- Team ' + playerName + ' to start the attack')

    # Displays each teams pokemon
    print('\nTeam Rocket enters with ' + Pokemon.pname[teamRocketPokemon.rocketPoke[0]] + ', ' + Pokemon.pname[
        teamRocketPokemon.rocketPoke[1]] + ', and ' + Pokemon.pname[teamRocketPokemon.rocketPoke[2]] + '.\n')
    print('Team ' + playerName + ' enters with ' + Pokemon.pname[playerPokemon.playerPoke[0]] + ', ' + Pokemon.pname[
        playerPokemon.playerPoke[1]] + ', and ' + Pokemon.pname[playerPokemon.playerPoke[2]] + '.\n')

    # Loops gameplay until a winner is determined
    while playerPokeCount != 0 or rocketPokeCount != 0:
        if turn == 0:

            move = teamRocketMoves(rocketBlock, e) # Selects a move
            try:
                move = move.replace("'", "")
            except AttributeError:
                continue

            try:
                move = move.replace("[", "")
            except AttributeError:
                continue

            try:
                move = move.replace("]", "")
            except AttributeError:
                continue

            try:
                move = move.replace('"', "")
            except AttributeError:
                continue

            count = movesList(move) # Sends move to get its power and type
            print('Team Rockets ' + Pokemon.pname[teamRocketPokemon.rocketPoke[e]] + ' cast',
                  movesList.moves[count] + ' to ',
                  Pokemon.pname[playerPokemon.playerPoke[f]] + ':')
            # Assigns damage to rockDmg
            rockDmg = damageEq(Pokemon.power[count], Pokemon.pattack[teamRocketPokemon.rocketAtt[e]],
                               Pokemon.pdefense[playerPokemon.playerDef[f]],
                               Pokemon.mtype[count],
                               Pokemon.ptype[teamRocketPokemon.rocketType[e]],
                               Pokemon.ptype[playerPokemon.playerType[f]])
            print('Damage to ' + Pokemon.pname[playerPokemon.playerPoke[f]] + ' is', int(rockDmg + 1))
            # changes defensive pokemons HP
            Pokemon.php[playerPokemon.playerHP[f]] = int(Pokemon.php[playerPokemon.playerHP[f]]) - int(rockDmg + 1)

            # Changes Player pokemon if HP drops below 0
            if Pokemon.php[playerPokemon.playerHP[f]] <= 0:
                print('Now ' + Pokemon.pname[teamRocketPokemon.rocketPoke[e]] + ' has',
                      Pokemon.php[teamRocketPokemon.rocketHP[e]],
                      'HP and ' + Pokemon.pname[playerPokemon.playerPoke[f]] + ' faints back to poke ball.')
                f = f + 1
                temp = 1
                if temp == 1:
                    blocked = [1, 2, 3, 4, 5]
                    temp = 0
                playerPokeCount = playerPokeCount - 1
                if playerPokeCount == 0:
                    break
                # Prompts players turn
                print('\nNext for Team ' + playerName + ', ' + Pokemon.pname[
                    playerPokemon.playerPoke[f]] + ' enters battle!')
            else:
                # Displays both living pokemons HP
                print('Now ' + Pokemon.pname[teamRocketPokemon.rocketPoke[e]] + ' has',
                      Pokemon.php[teamRocketPokemon.rocketHP[e]],
                      'HP and ' + Pokemon.pname[playerPokemon.playerPoke[f]] + ' has',
                      Pokemon.php[playerPokemon.playerHP[f]], 'HP')
            # Changes turns
            turn = 1

        if turn == 1:

            print('Choose the move for ' + Pokemon.pname[playerPokemon.playerPoke[f]] + ':')

            move = teamPlayerMoves(blocked, f) # prompts play to select a move

            count = movesList(move) # Sends move to get its power and type

            print(
                Pokemon.pname[playerPokemon.playerPoke[f]] + ' cast ' + movesList.moves[count] + ' to ' + Pokemon.pname[
                    teamRocketPokemon.rocketPoke[e]] + ':')
            # Assigns damage to playDmg
            playDmg = damageEq(Pokemon.power[count], Pokemon.pattack[playerPokemon.playerAtt[f]],
                               Pokemon.pdefense[teamRocketPokemon.rocketDef[e]],
                               Pokemon.mtype[count],
                               Pokemon.ptype[playerPokemon.playerType[f]],
                               Pokemon.ptype[teamRocketPokemon.rocketType[e]])
            print('Damage to ' + Pokemon.pname[teamRocketPokemon.rocketPoke[e]] + ' is', int(playDmg + 1))
            # changes defensive pokemons HP
            Pokemon.php[teamRocketPokemon.rocketHP[e]] = int(Pokemon.php[teamRocketPokemon.rocketHP[e]]) - int(
                playDmg + 1)

            if Pokemon.php[teamRocketPokemon.rocketHP[e]] <= 0:
                print('Now ' + Pokemon.pname[playerPokemon.playerPoke[f]] + ' has',
                      Pokemon.php[playerPokemon.playerHP[f]],
                      'HP and ' + Pokemon.pname[teamRocketPokemon.rocketPoke[e]] + ' faints back to poke ball.')
                e = e + 1
                rocketPokeCount = rocketPokeCount - 1
                if rocketPokeCount == 0:
                    break
                # Prompts players turn
                print('\nNext for Team Rocket, ' + Pokemon.pname[
                    teamRocketPokemon.rocketPoke[e]] + ' enters battle!')
            else:
                # Displays both living pokemons HP
                print('Now ' + Pokemon.pname[playerPokemon.playerPoke[f]] + ' has',
                      Pokemon.php[playerPokemon.playerHP[f]],
                      'HP and ' + Pokemon.pname[teamRocketPokemon.rocketPoke[e]] + ' has',
                      Pokemon.php[teamRocketPokemon.rocketHP[e]], 'HP')
            # Changes turns
            turn = 0
    # Displays winner
    if playerPokeCount == 0:
        print('\nAll of Team ' + playerName + "'s pokemon fainted, and Team Rocket prevails!")

    elif rocketPokeCount == 0:
        print("\nAll of Team Rocket's pokemon fainted, and Team " + playerName + ' prevails!')


gamePlay()

# Boter Kaas en Eieren Sogyo.

# classes.py wordt geïmporteerd, deze classes bevatten alle functies van het spel.
from classes import *


# Het boter kaas en eieren spel. Het spel wordt aangestuurd door een 'Game' en 'Board' object.
# Deze zijn gedefinieerd onder de boter kaas en eieren main function.
def boter_kaas_eieren():

    # win is de variabel dat de while loop van het spel draaiend houdt. Wanneer win = True, wordt de while loop
    # verbroken en wordt de speler gevraagd of deze het spel opnieuw wil spelen.

    win = False

    print("Welcome to boter kaas en eieren!")
    print("")

    # Game object 'game_instance' roept de functions 'generate_teams()' en 'pick_starter()' aan om de teams (X en O) en
    # een nummer (0 of 1) aan een player te geven. Deze worden dan gepaard in de dictionary gezet van player 1 en 2.
    # Dit wordt gedaan zodat de nummer later kan worden opgeroepen om te beslissen wie er het eerst de beurt krijgt.
    # Game_instance roept dan de announce_starting_turn functie aan, om een bericht te printen met wie er begint.
    game_instance.generate_teams()
    game_instance.pick_starter()
    player1 = dict({'number': game_instance.number1, 'team': game_instance.team1})
    player2 = dict({'number': game_instance.number2, 'team': game_instance.team2})
    game_instance.announce_starting_turn(player1)

    # Game object 'playing_board' roept de functie 'generate_new_board()' aan om een nieuwe list te genereren.
    playing_board.generate_new_board()

    # Nu begint de while loop. Gedurende deze loop wordt er voor en na elke beurt van de speler gekeken of er een
    # winnaar is of dat het gelijkspel is. Wanneer dat wel zo is, returnt check_board() True, waarna de while loop
    # wordt afgebroken.
    while not win:
        # Winnaar check #1, ook roept 'playing_board' de print_board() functie aan om de lijst visueel verspreid in het
        # bord te laten zien.
        playing_board.print_board()
        win = playing_board.check_board(player1, player2)
        if win is True:
            break

        # De speler met het nummer 0 krijgt hier de eerste beurt in de while loop. Als player 1 number 0 heeft, krijgt
        # die als eerste de beurt, anders krijgt player 2 de eerste beurt.
        if player1['number'] is 0:
            playing_board.player1_turn(player1)
        else:
            playing_board.player2_turn(player2)

        # Winnaar check #2 en het bord word opnieuw geprint met de nieuwe value in de lijst.
        playing_board.print_board()
        win = playing_board.check_board(player1, player2)
        if win is True:
            break

        # De speler dat nummer 1 is aangewezen, is hier als laatste aan de beurt in de loop. Hierna begint de loop weer
        # opnieuw.
        if player1['number'] is 1:
            playing_board.player1_turn(player1)
        else:
            playing_board.player2_turn(player2)

    # Er is een winnaar!.. Of het is gelijk spel. De gebruiker wordt gevraagd of die het spel opnieuw wilt
    # spelen of niet. De while loop zorgt ervoor dat de main functie alleen eindigdt wanneer de gebruiker 'n' invoerd.
    # Wanneer er 'y' wordt ingevoerd heft de loop op en wordt de main boter kaas en eieren functie opnieuw uitgevoerd.

    check = False
    while check is False:
        print('Play again (y/n)?')
        choice = input()
        if choice is 'y':
            check = True
            print()
            boter_kaas_eieren()
        if choice is'n':
            break
        if choice != 'n' or choice != 'y':
            print('Please only insert y or n.')


# game_instance en playing_board instances van de Game en Board class. Board heeft een lege list omdat deze een
# list met nummers 1 tot en met 9 wordt aangewezen. Wanneer de game opnieuw wordt gestart wordt deze volle lijst
# vervangen met een nieuwe ververste lijst in generate_board().
game_instance = Game()
playing_board = Board([])

# Main.py wordt hier op het begin uitgevoerd.
boter_kaas_eieren()

# Random wordt hier geïmporteerd.
import random


# De Game Class heeft een constructor met 4 variabelen, team 1-2 en nummer 1-2. Deze worden gebruikt zodat als een
# Game object (Boter Kaas en Eieren (verder als BKE) in dit geval) gemaakt is, het deze 4 variabelen heeft. Omdat er
# twee teams en twee nummers binnen één object worden samengesteld, is er geen nodigheid voor een parameter naast self.
class Game:
    def __init__(self):
        self.team1 = ''
        self.team2 = ''
        self.number1 = None
        self.number2 = None

    # Generate_teams() geeft de gebruiker de functionaliteit om het team te kiezen dat hij of zij wil spelen. Wanneer de
    # while loop actief is, kan deze alleen verbroken worden wanneer de gebruiker 'X' of 'O' invoert, om fouten te
    # voorkomen.
    def generate_teams(self):
        check = False
        while check is False:
            print('Player 1, please choose your team: ( X or O ).')
            self.team1 = input()
            if self.team1 is 'X' or self.team1 is 'O':
                check = True
            else:
                print("Reminder, you can only select X or O!")
                check = False

        # Wanneer player 1 een team heeft gekozen, krijgt player 2 automatisch het andere team toegewezen.
        if self.team1 is 'X':
            self.team2 = 'O'
        else:
            self.team2 = 'X'
        print('Player 2 will be on team ( ' + self.team2 + ' )!')

    # Pick_starter() genereert een nummer tussen de 0 en 1. Wanneer number1 0 is, krijgt number2 1 toegewezen
    # en omgekeerd hetzelfde. Deze worden dan in de object variabelen opgeslagen.
    def pick_starter(self):
        self.number1 = random.randint(0, 1)
        if self.number1 is 1:
            self.number2 = 0
        if self.number1 is 0:
            self.number2 = 1

    # Functie om aan te geven wie er het eerste aan de beurt is. Wanneer een player de nummer 0 heeft, is die altijd als
    # eerste aan de beurt in de loop. VB: Als player1 nummer 1 heeft, is player 2 automatisch 0 en dus eerst.
    @staticmethod
    def announce_starting_turn(player1):
        if player1['number'] is 0:
            print('Player 1 will be going first! Good luck!')
        if player1['number'] is 1:
            print('Player 2 will be going first! Good luck!')


# De Board Class heeft een constructor met cells. Elk vakje in het BKE spel wordt hier gerepresenteerd als een cell.
class Board:
    def __init__(self, cells):
        self.cells = cells

    # Wanneer een Board instance generate_new_board() aanroept krijgt deze een nieuwe lijst tussen de range van 1 en 10.
    # (1 t/m 9) wat de nummers in de vakken van het BKE bord representeren. Ook wanneer de lijst al een
    # lijst heeft met waarden, wordt deze vervangen.
    def generate_new_board(self):
        self.cells = list(range(1, 10))

    # Print_board() print het BKE bord uit in de terminal. Elke cell index staat voor de positie van een value in de
    # list. Op deze manier wanneer een er een vakje wordt gekozen, veranderd deze cell naar 'X' of 'O' en is het
    # vervolgens te zien in het bord als deze weer geprint wordt.
    def print_board(self):
        print('     |     |     ')
        print('  %s  |  %s  |  %s  ' % (self.cells[6], self.cells[7], self.cells[8]))
        print('     |     |     ')
        print('-----------------')
        print('     |     |     ')
        print('  %s  |  %s  |  %s  ' % (self.cells[3], self.cells[4], self.cells[5]))
        print('     |     |     ')
        print('-----------------')
        print('     |     |     ')
        print('  %s  |  %s  |  %s  ' % (self.cells[0], self.cells[1], self.cells[2]))
        print('     |     |     ')

    # Check_board() checkt na elke beurt of de geplaatste 'X's of 'O's voldoen aan een van de combinaties in
    # win_combinations. Als een van de combinaties alle 3 de indexen teruggeeft vanuit de list van de Board als de
    # speler zijn of haar teamletter, heeft de speler gewonnen en geeft de functie True terug wat de while loop in
    # main.py verbreekt, samen met het bericht wie er gewonnen heeft en of het gelijkspel is.
    def check_board(self, player1, player2):
        win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        count = 0
        for a in win_combinations:
            if self.cells[a[0]] == self.cells[a[1]] == self.cells[a[2]] == player1['team']:
                print('Player 1 Wins!')
                print('Congratulations!')
                return True

            if self.cells[a[0]] == self.cells[a[1]] == self.cells[a[2]] == player2['team']:
                print('Player 2 Wins!')
                print('Congratulations!')
                return True

        # Als alle cells in het Board object een player team teruggeeft, is het bord vol en is het dus gelijkspel.
        for a in range(9):
            if self.cells[a] == player1['team'] or self.cells[a] == player2['team']:
                count += 1
            if count == 9:
                print('The game ends in a Tie!')
                return True

    # player1_turn() print uit dat het player 1 zijn of haar beurt is. Vervolgens wordt pick gelijkgesteld aan de
    # number_picker functie. In deze functie moet de gebruiker een input geven die wordt gecheckt. Als het nummer is
    # gekozen wordt deze gereturned en is pick dat nummer. Vervolgens wordt de lijst van de Board object gecheckt om te
    # zien of iemand er al iets heeft geplaatst.
    def player1_turn(self, player1):
        print('Player 1, choose where to place your ( ' + player1['team'] + ' )')
        pick = self.number_picker()
        if self.cells[pick] is 'X' or self.cells[pick] is 'O':
            print("You can't place your (" + player1['team'] + " ) here!")
            self.player1_turn(player1)
        else:
            self.cells[pick] = player1['team']
        print()

    # Hetzelfde als player1_turn() maar dan voor player 2.
    def player2_turn(self, player2):
        print('Player 2, choose where to place your ( ' + player2['team'] + ' )')
        pick = self.number_picker()
        if self.cells[pick] is 'X' or self.cells[pick] is 'O':
            print("You can't place your ( " + player2['team'] + " ) here!")
            self.player2_turn(player2)
        else:
            self.cells[pick] = player2['team']
        print()

    # number_picker() vraagt de gebruiker voor een input die wordt gebruikt in de speler zijn of haar beurt. Wanneer
    # deze is ingevoerd wordt er zeker gemaakt dat het een integer is (1 t/m 9) en wordt de invoer met 1 verminderd.
    # De lijst is immers 1 t/m 9, maar de indexen lopen van 0 tot en met 8. Dus een invoer van 9 hoort eigenlijk 8 te
    # zijn. Wanneer het geen nummer tussen de 0 of 8 is, of überhaupt geen nummer is wordt er een error geprint.
    @staticmethod
    def number_picker():
        while True:
            while True:
                num = input()
                try:
                    num = int(num)
                    num -= 1
                    if num in range(0, 9):
                        return num
                    else:
                        print("That number is not on the board. Please try again.")
                        continue
                except ValueError:
                    print("That's not a number. Please type in a number and try again.")
                    continue

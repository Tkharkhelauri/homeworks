table = ["?", "?", "?",
         "?", "?", "?",
         "?", "?", "?"]

def display_table():
    """Prints Table"""
    print(table[0] + "|" + table[1] + "|" + table[2] + "         " + '1|2|3')
    print(table[3] + "|" + table[4] + "|" + table[5] + "         " + '4|5|6')
    print(table[6] + "|" + table[7] + "|" + table[8] + "         " + '7|8|9')

def players():
    """Chooses Player"""
    print('Choose Player (X/O)')
    player1 = input("Player1: ").lower()
    player2 = ''

    if player1 == "x":
        player2 = "O"
        print(f"Player2: {player2}")

    elif player1 == "O":
        player2 = "X"
        print(f"Player2: {player2}")

    else:
        print("Invalid input!")


current_player = "X"
run = True

def player_position():
    """Chooses position for X or O on the table"""
    global run
    print("Current Player: " + current_player)
    position = input("Choose (1/9): ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose (1/9): ")

        position = int(position) - 1

        if table[position] == "?":
            valid = True
        else:
            print("Position is taken!")

    table[position] = current_player
    display_table()


def flip_player():
    """Changes Current Player"""
    global current_player

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def check_winner():
    """Checks the Winner"""
    global run
    if table[0] == table[1] == table[2] != '?':
        run = False
        print(table[0] + " WON!")

    elif table[3] == table[4] == table[5] != '?':
        run = False
        print(table[3] + " WON!")

    elif table[6] == table[7] == table[8] != '?':
        run = False
        print(table[6] + " WON!")

    elif table[0] == table[3] == table[6] != '?':
        run = False
        print(table[0] + " WON!")

    elif table[1] == table[4] == table[7] != '?':
        run = False
        print(table[1] + " WON!")

    elif table[2] == table[5] == table[8] != '?':
        run = False
        print(table[2] + " WON!")

    elif table[0] == table[4] == table[8] != '?':
        run = False
        print(table[0] + " WON!")

    elif table[2] == table[4] == table[6] != '?':
        run = False
        print(table[2] + " WON!")

    elif "?" not in table:
        run = False
        print("Tie!")


def play_game():
    """Starts The Game"""
    print("TicTacToe Starts!")
    display_table()
    players()

    while run:
        player_position()

        flip_player()

        check_winner()


play_game()
print('Welcome to "Tic-tac-toe" game!')
player1 = input('Player 1, enter your name: ')
player2 = input('Player 2, enter your name: ')

win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turn = 1


def get_choice(player_name):
    while True:
        choice = input(f'{player_name}, enter a number from 0 to 8: ')
        if not choice.isdigit():
            raise TypeError('The entered data is not a number.')

        choice = int(choice)
        if choice < 0 or choice > 8:
            raise ValueError(f'Entered number must be between 0 and 8, but {choice} was given.')
        elif field[choice] != ' ':
            print('This position has already been taken. Try again.')
        else:
            return choice


def print_field(field):
    print('_____________')
    print(f'| {field[0]} | {field[1]} | {field[2]} |')
    print(f'| {field[3]} | {field[4]} | {field[5]} |')
    print(f'| {field[6]} | {field[7]} | {field[8]} |')
    print('_____________')


def check(field, turn, player1, player2):
    for c in win_combinations:
        if field[c[0]] == field[c[1]] == field[c[2]] != ' ':
            print(f'Hooray! We have the winner: {player1 if turn == 2 else player2}')
            print_field(field)
            return True

    if ' ' not in field:
        print('Oops! We have a draw!')
        print_field(field)
        return True

    return False


is_win = False
while not is_win:
    print_field(field)
    if turn == 1:
        choice = get_choice(player1)
        field[choice] = 'X'
        turn = 2
    else:
        choice = get_choice(player2)
        field[choice] = 'O'
        turn = 1

    is_win = check(field, turn, player1, player2)

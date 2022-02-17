game_field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
winning_combos = [('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'),
                  ('1', '4', '7'), ('2', '5', '8'), ('3', '6', '9'),
                  ('1', '5', '9'), ('3', '5', '7')]

playground = [['-', '|', '-', '|', '-'], ['-', '|', '-', '|', '-'], ['-', '|', '-', '|', '-']]
playground_tutorial = ['1 | 2 | 3', '4 | 5 | 6', '7 | 8 | 9']

step_count = 0
all_player_x_choices = []
all_player_o_choices = []


def player_x_step():
    while True:
        player_x_choice = input('Where to put a "X"? (1-9): ')
        if player_x_choice in game_field and player_x_choice not in (all_player_x_choices or all_player_o_choices):
            all_player_x_choices.append(player_x_choice)
            if player_x_choice == '1':
                playground[0][0] = 'X'
            elif player_x_choice == '2':
                playground[0][2] = 'X'
            elif player_x_choice == '3':
                playground[0][4] = 'X'
            elif player_x_choice == '4':
                playground[1][0] = 'X'
            elif player_x_choice == '5':
                playground[1][2] = 'X'
            elif player_x_choice == '6':
                playground[1][4] = 'X'
            elif player_x_choice == '7':
                playground[2][0] = 'X'
            elif player_x_choice == '8':
                playground[2][2] = 'X'
            elif player_x_choice == '9':
                playground[2][4] = 'X'
            break
        else:
            print('Hmmm..., please try again')


def player_o_step():
    while True:
        player_o_choice = input('Where to put a "O"? (1-9): ')
        if player_o_choice in game_field and player_o_choice not in (all_player_x_choices or all_player_o_choices):
            all_player_o_choices.append(player_o_choice)
            if player_o_choice == '1':
                playground[0][0] = 'O'
            elif player_o_choice == '2':
                playground[0][2] = 'O'
            elif player_o_choice == '3':
                playground[0][4] = 'O'
            elif player_o_choice == '4':
                playground[1][0] = 'O'
            elif player_o_choice == '5':
                playground[1][2] = 'O'
            elif player_o_choice == '6':
                playground[1][4] = 'O'
            elif player_o_choice == '7':
                playground[2][0] = 'O'
            elif player_o_choice == '8':
                playground[2][2] = 'O'
            elif player_o_choice == '9':
                playground[2][4] = 'O'
            break
        else:
            print('Hmmm..., please try again')


def win_check():
    for li in winning_combos:
        if li[0] in all_player_x_choices and li[1] in all_player_x_choices and li[2] in all_player_x_choices:
            print("--------------------------------\nCONGRATS 'X', YOU WIN!\n--------------------------------")
            return True

    for li in winning_combos:
        if li[0] in all_player_o_choices and li[1] in all_player_o_choices and li[2] in all_player_o_choices:
            print("--------------------------------\nCONGRATS 'O', YOU WIN!\n--------------------------------")
            return True


def show_table():
    for line in playground:
        print('        ', *line)

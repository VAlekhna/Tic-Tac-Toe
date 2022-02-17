import logic
from logic import *

print("--------------------------------\nWELCOME TO THE TIC TAC TOE GAME!\n--------------------------------")
print("       YOUR PLAYGROUND: \n        (remember it)\n")


for line in playground_tutorial:
    print(f"         {line}")
print("")

game_over = False

while not game_over:
    while True:
        player_x_step()
        show_table()
        if win_check():
            break
        step_count += 1
        if step_count == 9:
            print("--------------------------------\nDRAW!\n--------------------------------")
            break
        player_o_step()
        show_table()
        if win_check():
            break
        step_count += 1

    game_repeat = input('Do you want to play again? (Y/N): ')
    all_player_x_choices.clear()
    all_player_o_choices.clear()

    logic.playground = [['-', '|', '-', '|', '-'], ['-', '|', '-', '|', '-'], ['-', '|', '-', '|', '-']]
    logic.step_count = 0
    if game_repeat.lower() == 'n':
        game_over = True

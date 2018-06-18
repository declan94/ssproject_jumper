from jumper import *


def main():
    while True:
        im = read_image()
        im.save("./autojump.png")
        #piece_x, piece_y, board_x, board_y = find_piece_and_board(im)
        distance = jumper()
        press_time = jump(distance)
        click_screen(press_time)
        time.sleep(2)
        # if check_if_has_reset_button():
        #     print('Game Over')
        #     break
        # time.sleep(1)


if __name__ == '__main__':
    main()

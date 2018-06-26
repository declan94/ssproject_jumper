from jumper import *


def main():
    while True:
        read_image()
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

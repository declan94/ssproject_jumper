while (1)
    im = read_image();
	imwrite(im, "autojump.png");
    distance = jumper();
    press_time = jump(distance);
    
    click_screen(press_time);
    pause(2);
end
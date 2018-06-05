% submit your code here ###################################################
while (1)
    im = read_image();
    [piece_x, piece_y, board_x, board_y]=find_piece_and_board(im);
    press_time = jump(sqrt((board_x-piece_x)^2+(board_y-piece_y)^2));
    
    click_screen(press_time);
    pause(2);
end
% #########################################################################
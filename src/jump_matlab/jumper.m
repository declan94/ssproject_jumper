function dis = jumper();
screenshot = imread('./autojump.png');
% submit your code here ###################################################
[piece_x, piece_y, board_x, board_y]=find_piece_and_board(im);
dis = sqrt((board_x-piece_x)^2+(board_y-piece_y)^2);
% #########################################################################
end
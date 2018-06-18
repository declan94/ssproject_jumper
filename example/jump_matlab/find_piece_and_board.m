function [ piece_x, piece_y, board_x, new_board_y ] = find_piece_and_board( im )
%FIND_PIECE_AND_BOARD 此处显示有关此函数的摘要
%   此处显示详细说明
    piece_base_height_1_2 = 50;
    piece_body_width = 50;

    [h,w,c]=size(im);

    piece_x_sum=0;
    piece_x_c=0;
    piece_y_max=0;
    board_x=0;
    board_y=0;
    board_x_c=0;
    
    left_value=0;
    left_count=0;
    right_value=0;
    right_count=0;
    from_left_find_board_y=0;
    from_right_find_board_y=0;
    
    scan_x_border=int16(w/8);
    scan_start_y=1;
    for i=int16(h/3):50:int16(h*2/3)
        last_pixel=im(i,1,:);
        % not sure of the loop bound
        for j=2:w
            pixel=im(i,j,:);
            if (pixel(1,1,1) ~= last_pixel(1,1,1))||(pixel(1,1,2)~=last_pixel(1,1,2))||(pixel(1,1,3)~=last_pixel(1,1,3))
                scan_start_y = i-50;
                break;
            end
        end
        if scan_start_y~=1
            break
        end
    end
    
    for i=scan_start_y:int16(h*2/3)
        for j=scan_x_border:(w-scan_x_border)
            pixel=im(i,j,:);
            if (50<pixel(1,1,1))&&(pixel(1,1,1)<60)&&(pixel(1,1,2)>53)&&(pixel(1,1,2)<63)&&(95<pixel(1,1,3))&&(pixel(1,1,3)<110)
                piece_x_sum=piece_x_sum+j;
                piece_x_c=piece_x_c+1;
                piece_y_max=max(i,piece_y_max);
            end
        end
    end
    
    if (piece_x_sum==0)||(piece_x_c==0)
        piece_x=0;
        piece_y=0;
        board_x=0;
        new_board_y=0;
        return
    end
    
    piece_x=double(piece_x_sum)/double(piece_x_c);
    piece_y=piece_y_max-piece_base_height_1_2;
    
    for i=int16(h/3):int16(h*2/3)
        last_pixel=im(i,1,:);
        [h,s,v]=rgb2hsv(last_pixel(1,1,1),last_pixel(1,1,2),last_pixel(1,1,3));
        [r,g,b]=hsv2rgb(h,s,v*0.7);
        
        if from_left_find_board_y && from_right_find_board_y
            break
        end
        
        if ~board_x
            board_x_sum=0;
            board_x_c=0;
            
            for j=1:w
                pixel=im(i,j,:);
                if abs(j-piece_x)<piece_body_width
                    continue
                end
                
                if abs(pixel(1,1,1)-last_pixel(1,1,1)) + abs(pixel(1,1,2)-last_pixel(1,1,2)) + abs(pixel(1,1,3)-last_pixel(1,1,3)) > 10
                    board_x_sum=board_x_sum+j;
                    board_x_c=board_x_c+1;
                end
            end
            if board_x_sum
                board_x = double(board_x_sum) / double(board_x_c);
            end
        else
            for j=1:w
                pixel=im(i,j,:);
                if abs(j-piece_x)<piece_body_width
                    continue
                end
                if (abs(pixel(1,1,1)-last_pixel(1,1,1))+abs(pixel(1,1,2)-last_pixel(1,1,2))+abs(pixel(1,1,3)-last_pixel(1,1,3))>10) && (abs(pixel(1,1,1)-r)+abs(pixel(1,1,2)-g)+abs(pixel(1,1,3)-b)>10)
                    if left_value==j
                        left_count=left_count+1;
                    else
                        left_value=j;
                        left_count=1;
                    end
                    
                    if left_count>3
                        from_left_find_board_y = i-3;
                    end
                    break;
                end
            end
%             for j=1:w:-1
            for j=w:-1:1
                pixel=im(i,j,:);
                if abs(j-piece_x)<piece_body_width
                    continue
                end
                if (abs(pixel(1,1,1)-last_pixel(1,1,1))+abs(pixel(1,1,2)-last_pixel(1,1,2))+abs(pixel(1,1,3)-last_pixel(1,1,3))>10)&&(abs(pixel(1,1,1)-r)+abs(pixel(1,1,2)-g)+abs(pixel(1,1,3)-b)>10)
                    if right_value==j
                        right_count=left_count+1;
                    else
                        right_value=j;
                        right_count=1;
                    end
                    
                    if right_count>3
                        from_right_find_board_y=i-3;
                    end
                    break
                end
            end
        end
    end
 
    if board_x_c>5
        from_left_find_board_y = from_left_find_board_y+board_x_c/3;
        from_right_find_board_y=from_right_find_board_y+board_x_c/3;
    end
    board_y=piece_y-abs(board_x-piece_x)*sqrt(3)/3.;
    if abs(board_y-from_left_find_board_y)>abs(from_right_find_board_y)
        new_board_y=from_right_find_board_y;
    else
        new_board_y=from_left_find_board_y;
    end
            
    if (board_x==0)||(board_y==0)
        piece_x=0;
        piece_y=0;
        board_x=0;
        new_board_y=0;
        return
    end 
end
    


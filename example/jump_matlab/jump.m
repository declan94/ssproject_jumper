function [ press_time ] = jump( distance )
%JUMP 此处显示有关此函数的摘要
%   此处显示详细说明
    press_coefficiet = 4.10;
    press_time = distance * press_coefficiet;
    press_time = max(press_time, 200);  

end


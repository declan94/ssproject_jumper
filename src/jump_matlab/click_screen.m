function [  ] = click_screen(  )
%click_screen 此处显示有关此函数的摘要
%   此处显示详细说明
% if your OS is windows   
system("../../dependency/platform-tools-windows/adb.exe swipe 50 50 50 50 " + num2str(int16(press_time)));
%% if your OS is mac  
% system("../../dependency/platform-tools-macos/adb swipe 50 50 50 50 " + num2str(int16(press_time)));
end


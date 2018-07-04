function [  ] = click_screen(press_time)

% if your OS is windows   
system("../../dependency/platform-tools-windows/adb.exe swipe 50 50 50 50 " + num2str(int16(press_time)));
%% if your OS is mac  
% system("../../dependency/platform-tools-macos/adb swipe 50 50 50 50 " + num2str(int16(press_time)));
end


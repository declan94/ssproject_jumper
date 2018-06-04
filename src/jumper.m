time_coeff = 1.392

function y = get_screenshot()
% Change 'adb.exe' to 'adb' on macOS
system('../dependency/adb.exe shell screencap -p /sdcard/autojump.png')
system('../dependency/adb.exe pull /sdcard/autojump.png .')
end

fuction y = press_screen(distance)
% Change 'adb.exe' to 'adb' on macOS
press_time = floor(distance * time_coeff / 1000)
system(strcat('../dependency/adb.exe shell input swipe 500 1600 500 1602 ', int2str(press_time)))
end

% Code here

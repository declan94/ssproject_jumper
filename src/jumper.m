time_coeff = 1.392

function y = get_screenshot()
% Change 'platform-tools-windows' to 'platform-tools-macos' and 'adb.exe' to './adb' on macOS; you may need to use `chmod +X ../dependency/platform-tools-macos/adb` first
system('cd ../dependency/platform-tools-windows/ && adb.exe shell screencap -p /sdcard/autojump.png')
system('cd ../dependency/platform-tools-windows/ && adb.exe pull /sdcard/autojump.png ../../src/')
end

fuction y = press_screen(distance)
% Change 'platform-tools-windows' to 'platform-tools-macos' and 'adb.exe' to './adb' on macOS; you may need to use `chmod +X ../dependency/platform-tools-macos/adb` first
press_time = floor(distance * time_coeff)
system(strcat('cd ../dependency/platform-tools-windows/ && adb.exe shell input swipe 500 1600 500 1602 ', int2str(press_time)))
end

% Code here

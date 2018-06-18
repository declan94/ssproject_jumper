#include <iostream>
#include <string>
#include <sstream>

const double timeCoeff = 1.392;

std::string toString(int number)
{
    std::ostringstream ss;
    ss << number;
    return ss.str();
}

/**
 * A screenshot will be saved to your working directory
 */
void getScreenshot()
{
    // Change 'platform-tools-windows' to 'platform-tools-macos' and 'adb.exe' to 'adb' on macOS; you may need to use `chmod +X /dependency/platform-tools-macos/adb` first
    system("../dependency/platform-tools-windows/adb.exe shell screencap -p /sdcard/autojump.png");
    system("../dependency/platform-tools-windows/adb.exe pull /sdcard/autojump.png .");
}

void pressScreen(double distance)
{
    // Change 'platform-tools-windows' to 'platform-tools-macos' and 'adb.exe' to 'adb' on macOS; you may need to use `chmod +X /dependency/platform-tools-macos/adb` first
    int pressTime = distance * timeCoeff / 1000;
    system(("../dependency/platform-tools-windows/adb.exe shell input swipe 500 1600 500 1602 " + toString(pressTime)).c_str());
}

int main()
{
    // Code here
}

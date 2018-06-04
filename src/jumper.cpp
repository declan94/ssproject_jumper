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
    // Change 'adb.exe' to 'adb' on macOS
    system("../dependency/adb.exe shell screencap -p /sdcard/autojump.png");
    system("../dependency/adb.exe pull /sdcard/autojump.png .");
}

void pressScreen(double distance)
{
    // Change 'adb.exe' to 'adb' on macOS
    int pressTime = distance * timeCoeff / 1000;
    system(("../dependency/adb.exe shell input swipe 500 1600 500 1602 " + toString(pressTime)).c_str());
}

int main()
{
    // Code here
}

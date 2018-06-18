#include <iostream>
#include <boost/gil/extension/io/jpeg_io.hpp>
#include <string>
#include <windows.h>
#include "jump.h"
namespace gil = boost::gil;
using namespace std;

gil::rgb8_image_t read_image()
{
	// if your OS is win
	system("../../dependency/platform-tools-windows/adb.exe shell screencap -p autojump.png");
	system("../../dependency/platform-tools-windows/adb.exe pull /sdcard/autojump.png .");
	//// if your OS is mac
	// system("../../dependency/platform-tools-macos/adb shell screencap -p autojump.png");
	// system("../../dependency/platform-tools-macos/adb pull /sdcard/autojump.png .");
	gil::rgb8_image_t img;
	gil::jpeg_read_image("autojump.jpg", img);
	return img;
}

string Int_to_String(int n)
{
	stringstream stream;
	stream << n;
	return stream.str();
}

void click_screen(int press_time)
{
	std::string press_time_string = Int_to_String(press_time);
	// if your OS is windows
	std::string command("../../dependency/platform-tools-windows/adb.exe swipe 50 50 50 50 ");
	// // else if your OS is mac
	// std::string command ("../../dependency/platform-tools-macos/adb swipe 50 50 50 50 ");
	std::string final_cmd = command + press_time_string;
	system(final_cmd.c_str());
}

int main()
{
	//while (1) {
	//	gil::rgb8_image_t im = read_image();
	//	double* pos = find_piece_and_board(im);
	//	double piece_x = pos[0];
	//	double piece_y = pos[1];
	//	double board_x = pos[2];
	//	double board_y = pos[3];
	//	double press_time = jump(sqrt((board_x - piece_x)*(board_x - piece_x) + (board_y - piece_y)*(board_y - piece_y)));
	//	click_screen(press_time);
	//	Sleep(2000); //2000ms
	//}
	double distance = 0.0;
	gil::rgb8_image_t im;
	gil::jpeg_read_image("autojump.jpg", img);
	// ************************
	// start your code here
	double *pos = find_piece_and_board(im);
	double piece_x = pos[0];
	double piece_y = pos[1];
	double board_x = pos[2];
	double board_y = pos[3];
	//double press_time = jump(sqrt((board_x - piece_x)*(board_x - piece_x) + (board_y - piece_y)*(board_y - piece_y)));
	distance = sqrt((board_x - piece_x) * (board_x - piece_x) + (board_y - piece_y) * (board_y - piece_y));
	// ************************

	//将距离保存在文件中
	freopen("output.txt", "a", stdout);
	printf("%lf", distance);
	return 0;
}
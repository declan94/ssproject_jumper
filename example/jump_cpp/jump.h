#pragma once
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <boost/gil/extension/io/jpeg_io.hpp>
namespace gil = boost::gil;
using namespace std;
#define EPSILON_ 1e-6

// hyper-parameters
int wc_top = 0;
int wc_left = 0;
int wc_width = 540;
int wc_height = 960;
int piece_base_height_1_2 = 50;
int piece_body_width = 50;
double press_coefficient = 4.10;

//double max(double a, double b) {
//	if (a > b) return a;
//	else return b;
//}

//double min(double a, double b) {
//	if (a < b) return a;
//	else return b;
//}

double *rgb2hsv(int r, int g, int b)
{
	r = r / 255.0;
	g = g / 255.0;
	b = b / 255.0;
	int mx = max(r, g);
	mx = max(mx, b);
	int mn = min(r, g);
	mn = min(mn, b);
	double df = mx - mn;
	double h = 0;
	double s = 0;
	double v = 0;
	if (mx == mn)
		h = 0;
	else if (mx == r)
		h = int(60 * ((g - b) / df) + 360) % 360;
	else if (mx == g)
		h = int(60 * ((b - r) / df) + 120) % 360;
	else if (mx == b)
		h = int(60 * ((r - g) / df) + 240) % 360;

	if (mx == 0)
		s = 0;
	else
		s = df / mx;
	v = mx;
	double *return_arr = new double[3];
	return_arr[0] = h;
	return_arr[1] = s;
	return_arr[2] = v;
	return return_arr;
}

int *hsv2rgb(double h, double s, double v)
{
	double h60 = h / 60.0;
	double h60f = floor(h60);
	int hi = int(h60f) % 6;
	double f = h60 - h60f;
	double p = v * (1 - s);
	double q = v * (1 - f * s);
	double t = v * (1 - (1 - f) * s);
	int r = 0;
	int g = 0;
	int b = 0;
	if (hi == 0)
	{
		r = v;
		g = t;
		b = p;
	}
	else if (hi == 1)
	{
		r = q;
		g = v;
		b = p;
	}
	else if (hi == 2)
	{
		r = p;
		g = v;
		b = t;
	}
	else if (hi == 3)
	{
		r = p;
		g = q;
		b = v;
	}
	else if (hi == 4)
	{
		r = t;
		g = p;
		b = v;
	}
	else if (hi == 5)
	{
		r = v;
		g = p;
		b = q;
	}
	r = int(r * 255);
	g = int(g * 255);
	b = int(b * 255);
	int *return_arr = new int[3];
	return_arr[0] = r;
	return_arr[1] = g;
	return_arr[2] = b;
	return return_arr;
}

double *find_piece_and_board(gil::rgb8_image_t im)
{
	double w = im.width();
	double h = im.height();

	int piece_x_sum = 0;
	int piece_x_c = 0;
	int piece_y_max = 0;
	int board_x = 0;
	int board_y = 0;
	int board_x_sum = 0;
	int board_x_c = 0;

	int left_value = 0;
	int left_count = 0;
	int right_value = 0;
	int right_count = 0;
	int from_left_find_board_y = 0;
	int from_right_find_board_y = 0;

	int scan_x_boarder = int(w / 8);
	int scan_start_y = 0;
	int i, j;
	for (i = int(h / 3); i <= int(h * 2 / 3); i += 50)
	{
		gil::rgb8_pixel_t last_pixel = *const_view(im).at(0, i);
		for (j = 1; j < w; j++)
		{
			gil::rgb8_pixel_t pixel = *const_view(im).at(j, i);
			if ((pixel[0] != last_pixel[0]) && (pixel[1] != last_pixel[1]) && (pixel[2] != last_pixel[2]))
			{
				scan_start_y = i - 50;
				break;
			}
		}
		if (scan_start_y)
			break;
	}

	for (i = scan_start_y; i < int(h * 2 / 3); i++)
	{
		for (j = scan_x_boarder; j < w - scan_x_boarder; j++)
		{
			gil::rgb8_pixel_t pixel = *const_view(im).at(j, i);
			if ((50 < pixel[0]) && (pixel[0] < 60) && (pixel[1] > 53) && (pixel[1] < 63) && (95 < pixel[2]) && (pixel[2] < 110))
			{
				piece_x_sum += j;
				piece_x_c += 1;
				piece_y_max = max(i, piece_y_max);
			}
		}
	}

	if (piece_x_sum == 0 || piece_x_c == 0)
	{
		double *return_arr;
		return_arr[0] = 0;
		return_arr[1] = 0;
		return_arr[2] = 0;
		return_arr[3] = 0;
		return return_arr;
	}

	double piece_x = piece_x_sum / piece_x_c;
	double piece_y = piece_y_max - piece_base_height_1_2;

	for (i = int(h / 3); i < int(h * 2 / 3); i++)
	{
		gil::rgb8_pixel_t last_pixel = *const_view(im).at(0, i);
		double *tmp = rgb2hsv(last_pixel[0], last_pixel[1], last_pixel[2]);
		double h = tmp[0];
		double s = tmp[1];
		double v = tmp[2];
		int *tmp2 = hsv2rgb(h, s, v * 0.7);
		int r = tmp2[0];
		int g = tmp2[1];
		int b = tmp2[2];

		if (from_left_find_board_y && from_right_find_board_y)
			break;

		if (!board_x)
		{
			board_x_sum = 0;
			board_x_c = 0;
			for (j = 0; j < w; j++)
			{
				gil::rgb8_pixel_t pixel = *const_view(im).at(j, i);
				if (fabs(j - piece_x) < piece_body_width)
					continue;

				if (fabs(pixel[0] - last_pixel[1]) + fabs(pixel[1] - last_pixel[1]) + fabs(pixel[2] - last_pixel[2]) > 10)
				{
					board_x_sum += j;
					board_x_c += 1;
				}
			}
			if (board_x_sum)
				board_x = board_x_sum / board_x_c;
		}
		else
		{
			for (j = 0; j < w; j++)
			{
				gil::rgb8_pixel_t pixel = *const_view(im).at(j, i);
				if (fabs(j - piece_x) < piece_body_width)
					continue;
				if ((fabs(pixel[0] - last_pixel[0]) + fabs(pixel[1] - last_pixel[1]) + fabs(pixel[2] - last_pixel[2]) > 10) && (fabs(pixel[0] - r) + fabs(pixel[1] - g) + fabs(pixel[2] - b) > 10))
				{
					if (left_value == j)
						left_count = left_count + 1;
					else
					{
						left_value = j;
						left_count = 1;
					}

					if (left_count > 3)
						from_left_find_board_y = i - 3;
					break;
				}
			}
			for (j = w - 1; j >= 0; j--)
			{
				gil::rgb8_pixel_t pixel = *const_view(im).at(j, i);
				if (fabs(j - piece_x) < piece_body_width)
					continue;
				if ((fabs(pixel[0] - last_pixel[0]) + fabs(pixel[1] - last_pixel[1]) + fabs(pixel[2] - last_pixel[2]) > 10) && (fabs(pixel[0] - r) + fabs(pixel[1] - g) + fabs(pixel[2] - b) > 10))
				{
					if (right_value == j)
						right_count = left_count + 1;
					else
					{
						right_value = j;
						right_count = 1;
					}

					if (right_count > 3)
						from_right_find_board_y = i - 3;
					break;
				}
			}
		}
	}
	if (board_x_c > 5)
	{
		from_left_find_board_y = from_left_find_board_y + board_x_c / 3;
		from_right_find_board_y = from_right_find_board_y + board_x_c / 3;
	}
	board_y = piece_y - fabs(board_x - piece_x) * sqrt(3) / 3;
	double new_board_y = 0;
	if (fabs(board_y - from_left_find_board_y) > abs(from_right_find_board_y))
	{
		new_board_y = from_right_find_board_y;
	}
	else
	{
		new_board_y = from_left_find_board_y;
	}

	if (board_x == 0 || board_y == 0)
	{
		double *return_arr = new double[4];
		return_arr[0] = 0;
		return_arr[1] = 0;
		return_arr[2] = 0;
		return_arr[3] = 0;
		return return_arr;
	}
	double *return_arr = new double[4];
	return_arr[0] = piece_x;
	return_arr[1] = piece_y;
	return_arr[2] = board_x;
	return_arr[3] = new_board_y;
	return return_arr;
}

int jump(double distance)
{
	int press_time = distance * press_coefficient;
	press_time = max(press_time, 200);
	return press_time;
}
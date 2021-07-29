"""
File: sierpinski.py
Name: 吳采曄 Judy Wu
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	This function recursively prints the Sierpinski triangle on GWindow.
	The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
	It is a self similar structure that occurs at different levels of iterations.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: The number that recursion happens (the level of Sierpinski Triangle shown).
	:param length: The length of each Sierpinski Triangle
	:param upper_left_x: The upper left x coordinate of each Sierpinski Triangle
	:param upper_left_y: The upper left y coordinate of each Sierpinski Triangle
	:return: Draw Sierpinski Triangles to the order we assign.
	"""
	if order == 0:						# base case is order == 0, and no more recursion happens.
		pass

	else:								# when order hasn't reached base case
		# the upper line of the order 1 triangle
		triangle_upper = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		# the lower left line of the order 1 triangle
		triangle_left = GLine(upper_left_x, upper_left_y, upper_left_x + length / 2, upper_left_y + length * 0.866)
		# the lower right line of the order 1 triangle
		triangle_right = GLine(upper_left_x + length / 2, upper_left_y + length * 0.866, upper_left_x + length, upper_left_y)
		window.add(triangle_upper)
		window.add(triangle_left)
		window.add(triangle_right)
		pause(100)

		# Add upper left triangles
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)

		# Add upper right triangles
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)

		# Add lower triangles
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 4, upper_left_y + length * 0.433)


if __name__ == '__main__':
	main()
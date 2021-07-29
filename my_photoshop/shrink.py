"""
File: shrink.py
Name: 吳采曄 Judy Wu
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image.
    :return: The new image with half width and height of the original image.
    """
    original = SimpleImage(filename)
    after_shrink = SimpleImage.blank(original.width // 2, original.height // 2)   # Make a blank image which has half width and height from original.

    for x in range(original.width):
        for y in range(original.height):
            if x % 2 == 0 and y % 2 == 0:                           # If x and y are even.
                x1 = x // 2                                         # Assign x1 as half of x.
                y1 = y // 2                                         # Assign y1 as half of y.
                original_pixel = original.get_pixel(x, y)           # Get pixel from original image, pixel position (x, y)
                shrink_pixel = after_shrink.get_pixel(x1, y1)       # Get pixel from new, shrinked image, pixel position (x1, y1)
                shrink_pixel.red = original_pixel.red               # Assign red value of shrink_pixel as red value of original_pixel whose position is 2 times width and height.
                shrink_pixel.green = original_pixel.green           # Assign green value of shrink_pixel as green value of original_pixel whose position is 2 times width and height.
                shrink_pixel.blue = original_pixel.blue             # Assign blue value of shrink_pixel as blue value of original_pixel whose position is 2 times width and height.
    return after_shrink


def main():
    """
    Show original image.
    Make a shrink image with half of width and height from original image but still shows the content of it.
    And show the shrink image.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()

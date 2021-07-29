"""
File: mirror_lake.py
Name: 吳采曄 Judy Wu
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image.
    :return: Make a blank image by doubling the height of the original file.
     Fill the upper part with original pixels and the lower part is mirrored by flipping each pixel vertically.
    """
    original = SimpleImage(filename)
    reflected = SimpleImage.blank(original.width, original.height * 2)         # Make a blank image by doubling the height of original file.

    for x in range(original.width):
        for y in range(original.height):
            original_pixel = original.get_pixel(x, y)                          # Each pixel from original image.
            reflected_p1 = reflected.get_pixel(x, y)                           # reflected pixel 1 (the upper part)
            reflected_p2 = reflected.get_pixel(x, reflected.height - 1 - y)    # reflected pixel 2 (the lower mirrored part)

            reflected_p1.red = original_pixel.red
            reflected_p1.green = original_pixel.green
            reflected_p1.blue = original_pixel.blue

            reflected_p2.red = original_pixel.red
            reflected_p2.green = original_pixel.green
            reflected_p2.blue = original_pixel.blue

    return reflected


def main():
    """
    This function shows the original image, and then shows the reflected image.
    In the reflected image we doubled the pixels from original file and flipped each pixel vertically.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()

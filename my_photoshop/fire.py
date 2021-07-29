"""
File: fire.py
Name: 吳采曄 Judy Wu
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original colored image.
    :return: Make the pixels that are recognized as fire into red, while other pixels turned to gray.
    """
    highlight_fire = SimpleImage(filename)
    for pixel in highlight_fire:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.red > avg*HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return highlight_fire


def main():
    """
    This function shows the original colored image, and then shows the processed image (highlighted_fire).
    In the highlighted_fire image we make the pixels that are recognized as fire into red,
    while other pixels turned to gray to better visualize the fire positions.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()

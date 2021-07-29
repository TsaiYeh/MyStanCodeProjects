"""
File: green_screen.py
Name: 吳采曄 Judy Wu
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image.
    :param figure_img: SimpleImage, the figure image with green screen background.
    :return: updated figure_img which the green screen pixels are replaced by pixels of background image.
    """
    for x in range(background_img.width):
        for y in range(background_img.height):
            bg_pixel = background_img.get_pixel(x, y)
            fig_pixel = figure_img.get_pixel(x, y)
            bigger = max(fig_pixel.red, fig_pixel.blue)
            if fig_pixel.green > bigger * 2:
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return figure_img


def main():
    """
    This function conducts green screen replacement
    which is able to photoshop a person onto other backgrounds.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()

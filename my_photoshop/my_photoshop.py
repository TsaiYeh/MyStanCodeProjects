"""
File: best_photoshop_award.py
Name: 吳采曄 Judy Wu
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.26

# Controls the upper bound for black pixel
BLACK_PIXEL = 130


def combine(background, figure):
    """
    :param background: SimpleImage, the background image.
    :param figure: SimpleImage, the figure image with green screen background.
    :return: updated figure_img which the green screen pixels are replaced by pixels of background image.
    """
    background.make_as_big_as(figure)
    for x in range(background.width):
        for y in range(background.height):
            bg_pixel = background.get_pixel(x, y)
            fig_pixel = figure.get_pixel(x, y)

            avg = (fig_pixel.red + fig_pixel.blue + fig_pixel.green) // 3
            total = fig_pixel.red + fig_pixel.blue + fig_pixel.green
            if fig_pixel.green > avg * THRESHOLD and total > BLACK_PIXEL:
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return figure


def main():
    """
    I'm introducing an art which there's another person introducing the art inside the art.
    He says "Look!" and I say "See!"
    """
    art = SimpleImage("image_contest/art.jpg")
    me = SimpleImage("image_contest/me.jpg")
    result = combine(art, me)
    result.show()


if __name__ == '__main__':
    main()

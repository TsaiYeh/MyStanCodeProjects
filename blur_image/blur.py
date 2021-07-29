"""
File: blur.py
Name: 吳采曄 Judy Wu
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image that will be blurred.
    :return: The new image that is blurred by making each pixel's RGB value
    become the average value from itself and its surrounding pixels.
    """
    new_img = SimpleImage.blank(img.width, img.height)      # Make a blank image whose size is the same as the original image.
    for x in range(img.width):
        for y in range(img.height):
            total_red = 0                                   # Int, the sum of red value from chosen pixels.
            total_green = 0                                 # Int, the sum of green value from chosen pixels.
            total_blue = 0                                  # Int, the sum of blue value from chosen pixels.
            count = 0                                       # Int, the number of pixels counted.

            for i in range(-1, 2):                          # Check left, same-width, and right pixels.
                for j in range(-1, 2):                      # Check upper, same-height, and lower pixels.
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            pixel = img.get_pixel(pixel_x, pixel_y)     # Get pixel from original image.
                            total_red += pixel.red                      # Calculate sum of red value of these pixels.
                            total_green += pixel.green                  # Calculate sum of green value of these pixels.
                            total_blue += pixel.blue                    # Calculate sum of blue value of these pixels.
                            count += 1
            new_pixel = new_img.get_pixel(x, y)              # Get pixel from new image.
            new_pixel.red = total_red / count                # Red value of new pixel is the average of its neighbors.
            new_pixel.green = total_green / count            # Green value of new pixel is the average of its neighbors.
            new_pixel.blue = total_blue / count              # Blue value of new pixel is the average of its neighbors.
    return new_img


def main():
    """
    This function shows the original image(smiley-face.png) first, and then its blurred image.
    We blur the image by turning each pixel's RGB value into the average of itself and its surrounding pixels.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()

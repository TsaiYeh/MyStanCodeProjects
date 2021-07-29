"""
File: stanCodoshop.py
Name: 吳采曄 Judy
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's Ghost assignment by Jerry Liao.

-----------------------------------------------
This program computes and displays a Ghost solution image from a list of images shot in the same scene.
"""

import os
import sys
from simpleimage import SimpleImage
import math


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    pixel = (pixel.red, pixel.green, pixel.blue)                # Pixel consists a tuple of its RGB values.
    # Calculate the distance between red, green, and blue values from the given average RGB values.
    dist = math.sqrt((red - pixel[0]) ** 2 + (green - pixel[1]) ** 2 + (blue - pixel[2]) ** 2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    # rgb = [0, 0, 0]                                             # Define rgb as a list of red, green, blue values.
    rgb = []
    total_r = 0                                                 # total_r initial value is 0.
    total_g = 0                                                 # total_g initial value is 0.
    total_b = 0                                                 # total_b initial value is 0.
    for pixel in pixels:
        pixel = (pixel.red, pixel.green, pixel.blue)
        total_r += pixel[0]                                     # total_r is total red values added from each pixel.
        total_g += pixel[1]                                     # total_g is total green values added from each pixel.
        total_b += pixel[2]                                     # total_b is total blue values added from each pixel.
    # rgb[0] = total_r // len(pixels)                           # Calculate average red value.
    # rgb[1] = total_g // len(pixels)                           # Calculate average green value.
    # rgb[2] = total_b // len(pixels)                           # Calculate average blue value.

    rgb.append(total_r // len(pixels))
    rgb.append(total_g // len(pixels))
    rgb.append(total_b // len(pixels))

    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    candidate = []                                              # candidate is a list of all input pixels.
    rgb = get_average(pixels)                                   # rgb is a list of average red, green, blue values from pixels.
    for pixel in pixels:
        dist = get_pixel_dist(pixel, rgb[0], rgb[1], rgb[2])    # calculate each pixel's distance from rgb.
        candidate.append((pixel, dist))                         # add each pixel and its dist into candidate list.
    best_candidate = min(candidate, key=lambda ele: ele[1])     # best_candidate is the pixel with the minimum dist.
    best = best_candidate[0]                                    # only return the best pixel. Its dist no need.
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect

    for x in range(width):
        for y in range(height):
            pixels = []                                         # pixels is the list of all input pixels.
            for image in images:
                image_pixel = image.get_pixel(x, y)             # get pixel at the position(x,y) from each image.
                pixels.append(image_pixel)                      # add each pixel into the pixels list.
            best = get_best_pixel(pixels)                   # find out the best pixel
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best.red                         # add the best pixel's red value onto the result image.
            result_pixel.green = best.green                     # add the best pixel's green value onto the result image
            result_pixel.blue = best.blue                       # add the best pixel's blue value onto the result image.

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()

"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by Jerry Liao.

Draw a line chart showing the rankings of searched names in each year to compare the popularity of baby names.
"""

import tkinter
import babynames
import babygraphicsgui as gui

# Constant
FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year in the YEARS list,
    returns the x coordinate of the vertical line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated with the specified year.
    """
    column_width = (width - 2 * GRAPH_MARGIN_SIZE) // len(YEARS)                # Width between 2 vertical fixed lines
    x_coordinate = int(column_width * year_index + GRAPH_MARGIN_SIZE)           # X-position of the specific year's line
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')                                                # delete all existing lines from the canvas

    # Write your code below this line
    #################################

    # Create the upper horizontal fixed line.
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, (CANVAS_WIDTH - GRAPH_MARGIN_SIZE), GRAPH_MARGIN_SIZE)

    # Create the lower horizontal fixed line.
    canvas.create_line(GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE), (CANVAS_WIDTH - GRAPH_MARGIN_SIZE),
                       (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE))

    # Create vertical lines and texxts for each year in the YEARS list
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE),
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)                                            # draw the fixed background grid

    # Write your code below this line
    #################################
    row_height = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000         # space of y-position (height) between each rank

    for i in range(len(lookup_names)):                                  # draw each name in the lookup_names list
        name = lookup_names[i]                                          # define name as elements in lookup_names list
        color = COLORS[i % 4]                                           # define color as elements in the COLORS list
        for j in range(len(YEARS)):                                     # draw each year ranking of the names
            year1 = str(YEARS[j])                                       # define year1 as current year
            year0 = str(YEARS[j-1])                                     # define year1 as previous year

            if year1 in name_data[name]:                                # if year1 exists in the name_data[name] dict
                rank1 = name_data[name][year1]                          # get the value (rank1) from the key (year1)
            else:                                                       # if year1 not exist (not ranked inside 1000)
                rank1 = '1001'                                          # define rank1 as 1001.

            if year0 in name_data[name]:                                # if year0 exists in the name_data[name] dict
                rank0 = name_data[name][year0]                          # get the value (rank0) from the key (year0)
            else:                                                       # if year0 not exist (not ranked inside 1000)
                rank0 = '1001'                                          # define rank0 as 1001.

            # if rank1 inside 1000 ranking, mark the name and ranking in each year.
            if int(rank1) <= 1000:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX,
                                   (GRAPH_MARGIN_SIZE + row_height * int(rank1)),
                                   text=name+' '+str(rank1), anchor=tkinter.SW, fill=color)
            # if rank1 not inside 1000 ranking, mark the name and '*' in each year.
            else:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j) + TEXT_DX,
                                   (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE), text=name + ' *', anchor=tkinter.SW, fill=color)

            # if j > 0 (we have data of current year and previous year), draw the line.
            if j > 0:
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j - 1), (GRAPH_MARGIN_SIZE + row_height * int(rank0)),
                                   get_x_coordinate(CANVAS_WIDTH, j), (GRAPH_MARGIN_SIZE + row_height * int(rank1)),
                                   width=LINE_WIDTH, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()

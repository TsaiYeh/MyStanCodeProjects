"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by Jerry Liao.

Organize the data of baby names from 1900 to 2010, and integrate them into a dictionary to draw charts.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    if name not in name_data:                                   # if the entered name not exist in name_data dict
        new = {year: rank}                                      # treat it as new name with key (year) and value (rank)
        name_data[name] = new                                   # add the new name dict into name_data dict, name is key
    else:                                                       # if the entered name already exists in name_data dict
        if year not in name_data[name]:                         # check if year not exist as a key of name
            name_data[name][year] = rank                        # add year (key) and its rank (value)
        else:                                                   # if year exists
            if int(rank) < int(name_data[name][year]):          # if new rank higher than existing rank
                name_data[name][year] = rank                    # replace the rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    count = 0                                                       # define count as the number of line read
    with open(filename, 'r') as f:
        for line in f:
            count += 1
            if count == 1:                                          # if it's the first line of the filename
                year = line.split()[0]                              # assign the 0-index word as year
            else:                                                   # from the second line till the end
                lst = line.split(',')
                rank = lst[0].strip()                               # assign the 0-index word as rank
                name1 = lst[1].strip()                              # assign the 1-index word as name1
                name2 = lst[2].strip()                              # assign the 2-index word as name2
                add_data_for_name(name_data, year, rank, name1)     # add name1 in name_data dict
                add_data_for_name(name_data, year, rank, name2)     # add name2 in name_data dict


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}                                                  # Define name_data as an empty dict
    for filename in filenames:
        add_file(name_data, filename)                               # add each file's data into name_data
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain the target string
    """
    names = []                                                      # define names as an empty list
    for name in name_data:
        if target in name.lower():                                  # if target exists in name dict (case-insensitive)
            names.append(name)                                      # add the matched name into names list
    return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()

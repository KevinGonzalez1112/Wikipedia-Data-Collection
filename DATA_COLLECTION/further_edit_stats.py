
import numpy as np


"""
----------------------------------------------------------------------------
    Creating the functions that will extract the Revision
    further statistics.
----------------------------------------------------------------------------
"""


def get_major_or_minor(revisions):

    major_edits = 0

    minor_edits = 0

    # Loop through the list of revisions

    for Revision in revisions:

        # If the edit is tagged as minor increment the counter by 1

        if Revision.minor:

            minor_edits = minor_edits + 1

        # Then if it's not increment the other counter by 1

        else:

            major_edits = major_edits + 1

    # Return the number of major and minor edits

    return major_edits, minor_edits


def get_edit_size_stats(revisions):

    # Creating a blank array to store the size for each edit

    edit_sizes = []

    # Loop through the list of revisions

    for rev in revisions:

        # Add the edit size to the array

        edit_sizes.append(rev.size)

    # Using the created array and numpy to calculate the median and quartiles

    lower_percentile = float(np.percentile(edit_sizes, 25))

    median = float(np.median(edit_sizes))

    upper_percentile = float(np.percentile(edit_sizes, 75))

    # Return the median and quartiles

    return lower_percentile, median, upper_percentile


import pywikibot as pwb
from datetime import datetime
import pandas as pd
import numpy as np


"""
----------------------------------------------------------------------------
    Creating the functions that will extract the page
    temporal statistics.
----------------------------------------------------------------------------
"""


def get_page_age(article):

    site = pwb.Site("en", "wikipedia")

    page = pwb.Page(site, article)

    # Get the page creation revision

    creation_time = page.oldest_revision.timestamp

    # Subtract that date from today to get page age

    page_age = datetime.now() - creation_time

    # Return the age of the article

    return page_age


def get_avg_time_between_edits(revisions):

    # Create a DataFrame with the edit times

    df = pd.DataFrame({
        'timestamp': [rev['timestamp'] for rev in revisions]
    })

    # Reverse the index to put oldest revision first

    df = df.reindex(index = df.index[::-1])

    # Convert the timestamp column to datetime format

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Calculate the time difference between consecutive rows

    df['time_diff'] = df['timestamp'].diff()

    # Creating a blank array to add the time differences to

    time_between = []

    # Loop through the dataframe column

    for row in df['time_diff']:

        # Add the time difference to the array

        time_between.append(row)

    # Using the created array and numpy to calculate the median and quartiles

    lower_percentile = np.percentile(time_between, 25)

    median = np.median(time_between)

    upper_percentile = np.percentile(time_between, 75)

    # Return the median and quartiles

    return lower_percentile, median, upper_percentile


def get_lull_stats(revisions):

    import datetime

    # Create a DataFrame with the edit times

    df = pd.DataFrame({
        'timestamp': [rev['timestamp'] for rev in revisions]
    })

    # Reverse the index to put oldest revision first

    df = df.reindex(index=df.index[::-1])

    # Convert the timestamp column to datetime format

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Calculate the time difference between consecutive rows

    df['time_diff'] = df['timestamp'].diff()

    # Creating a blank array to store the lull duration times

    lull_duration = []

    lull_count = 0

    # Loop through the dataframe column

    for row in df['time_diff']:

        # If the time difference is above 2 weeks consider this a lull

        if row > datetime.timedelta(days=14):
            # Then add this duration to the lull array

            lull_duration.append(row)

            # And increment the counter by 1

            lull_count = lull_count + 1

    # Using the created array and numpy to calculate the median and quartiles

    lower_percentile = np.percentile(lull_duration, 25)

    median = np.median(lull_duration)

    upper_percentile = np.percentile(lull_duration, 75)

    # Return the median and quartiles

    return lull_count, lower_percentile, median, upper_percentile


def get_avg_edits_per(revisions):

    # Create a DataFrame with the edit times

    df = pd.DataFrame({
        'timestamp': [rev['timestamp'] for rev in revisions]
    })

    # Reverse the index to put oldest revision first

    df = df.reindex(index = df.index[::-1])

    # Convert the timestamp column to datetime format

    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Calculate the time difference between consecutive rows

    df['time_diff'] = df['timestamp'].diff()

    df = df.set_index(['timestamp'])

    # Using the created array and numpy to calculate the median and quartiles

    monthly = df.groupby([df.index.year, df.index.month]).count()

    m_lower_percentile = np.percentile(monthly.values, 25)

    m_median = np.median(monthly.values)

    m_upper_percentile = np.percentile(monthly.values, 75)

    yearly = df.groupby([df.index.year]).count()

    y_lower_percentile = np.percentile(yearly.values, 25)

    y_median = np.median(yearly.values)

    y_upper_percentile = np.percentile(yearly.values, 75)

    # Return the median and quartiles

    return (m_lower_percentile, m_median, m_upper_percentile,
            y_lower_percentile, y_median, y_upper_percentile)

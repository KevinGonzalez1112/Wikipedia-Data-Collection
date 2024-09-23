
import json


"""
----------------------------------------------------------------------------
    Creating the function that will extract the article titles
    from the JSON files created.
----------------------------------------------------------------------------
"""


def get_articles(json_file):

    # Create empty array to store the titles

    articles = []

    # Open the JSON File with article links

    file = open(json_file)

    # Convert JSON into Dictionaries

    file_data = json.load(file)

    # Add the Titles to the array

    for row in file_data['titles']:

        articles.append(row)

    # Return the list of article titles

    return articles
